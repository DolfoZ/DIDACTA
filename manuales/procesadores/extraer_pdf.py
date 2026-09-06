"""
extraer_pdf.py - Convierte PDFs a Markdown y extrae imágenes
Parte del pipeline de procesamiento Didacta
"""
import os
import sys
import sqlite3
import hashlib
import logging
from pathlib import Path
from datetime import datetime

# Configuración de logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Rutas del proyecto
BASE_DIR = Path(__file__).parent.parent.parent
PDF_DIR = BASE_DIR / "manuales" / "pdf"
OUTPUT_DIR = BASE_DIR / "manuales" / "procesados"

# Intentar importar dependencias opcionales
TRY_IMPORT = {}
try:
    import fitz  # pymupdf
    TRY_IMPORT['fitz'] = True
except ImportError:
    TRY_IMPORT['fitz'] = False
    logger.warning("pymupdf no instalado. pip install pymupdf")

try:
    from pdf2image import convert_from_path
    TRY_IMPORT['pdf2image'] = True
except ImportError:
    TRY_IMPORT['pdf2image'] = False
    logger.warning("pdf2image no instalado. pip install pdf2image")

try:
    import pytesseract
    from PIL import Image
    TRY_IMPORT['pytesseract'] = True
except ImportError:
    TRY_IMPORT['pytesseract'] = False
    logger.warning("pytesseract no instalado. pip install pytesseract")


def crear_base_datos(doc_name: str) -> Path:
    """Crea la estructura de base de datos para un documento."""
    doc_dir = OUTPUT_DIR / doc_name
    doc_dir.mkdir(parents=True, exist_ok=True)
    
    db_path = doc_dir / "conocimiento.db"
    
    conn = sqlite3.connect(str(db_path))
    cursor = conn.cursor()
    
    # Tabla de documentos
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS documentos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            tipo TEXT DEFAULT 'pdf',
            fuente TEXT,
            contenido_markdown TEXT,
            path_markdown TEXT,
            fecha_procesamiento TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    
    # Tabla de conocimiento estructurado
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS conocimiento (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            documento_id INTEGER REFERENCES documentos(id),
            categoria TEXT,
            nombre TEXT,
            descripcion TEXT,
            especificaciones TEXT,
            tags TEXT,
            nivel_confianza REAL DEFAULT 0.5,
            fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    
    # Tabla de imágenes
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS imagenes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            documento_id INTEGER REFERENCES documentos(id),
            conocimiento_id INTEGER REFERENCES conocimiento(id),
            nombre TEXT,
            path_local TEXT,
            tipo_contenido TEXT,
            width INTEGER,
            height INTEGER
        )
    """)
    
    # Tabla de metadatos del procesamiento
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS procesamiento (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            documento_id INTEGER REFERENCES documentos(id),
            etapa TEXT,
            estado TEXT,
            mensaje TEXT,
            fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    
    conn.commit()
    conn.close()
    
    logger.info(f"Base de datos creada: {db_path}")
    return db_path


def extraer_texto_fitz(pdf_path: Path) -> str:
    """Extrae texto usando pymupdf (fitz)."""
    if not TRY_IMPORT.get('fitz'):
        return "[ERROR: pymupdf no disponible]"
    
    try:
        doc = fitz.open(str(pdf_path))
        texto = ""
        
        for page_num, page in enumerate(doc):
            texto += f"\n\n--- Página {page_num + 1} ---\n\n"
            texto += page.get_text("text")
        
        doc.close()
        return texto
    except Exception as e:
        logger.error(f"Error extrayendo texto con fitz: {e}")
        return f"[ERROR: {str(e)}]"


def extraer_texto_ocr(image_path: Path, lang: str = 'eng+spa') -> str:
    """Extrae texto usando OCR con pytesseract."""
    if not TRY_IMPORT.get('pytesseract'):
        return "[ERROR: pytesseract no disponible]"
    
    try:
        from PIL import Image
        img = Image.open(str(image_path))
        texto = pytesseract.image_to_string(img, lang=lang)
        return texto
    except Exception as e:
        logger.error(f"Error en OCR: {e}")
        return f"[ERROR OCR: {str(e)}]"


def convertir_pdf_imagenes(pdf_path: Path, output_dir: Path) -> list:
    """Convierte PDF a imágenes usando pdf2image."""
    imagenes = []
    
    if not TRY_IMPORT.get('pdf2image'):
        logger.warning("pdf2image no disponible, intentando con fitz")
        if TRY_IMPORT.get('fitz'):
            try:
                doc = fitz.open(str(pdf_path))
                for page_num in range(len(doc)):
                    page = doc[page_num]
                    pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))  # 2x zoom
                    img_path = output_dir / f"pagina_{page_num + 1}.png"
                    pix.save(str(img_path))
                    imagenes.append(img_path)
                doc.close()
            except Exception as e:
                logger.error(f"Error convirtiendo con fitz: {e}")
        return imagenes
    
    try:
        from pdf2image import convert_from_path
        paginas = convert_from_path(str(pdf_path), dpi=200)
        
        for i, pagina in enumerate(paginas):
            img_path = output_dir / f"pagina_{i + 1}.png"
            pagina.save(str(img_path), "PNG")
            imagenes.append(img_path)
        
        logger.info(f"Convertidas {len(imagenes)} páginas a imágenes")
    except Exception as e:
        logger.error(f"Error convirtiendo PDF a imágenes: {e}")
    
    return imagenes


def extraer_imagenes_pdf(pdf_path: Path, output_dir: Path) -> list:
    """Extrae imágenes embebidas del PDF."""
    imagenes_extraidas = []
    
    if not TRY_IMPORT.get('fitz'):
        return imagenes_extraidas
    
    try:
        doc = fitz.open(str(pdf_path))
        
        for page_num, page in enumerate(doc):
            for img_index, img in enumerate(page.get_images()):
                xref = img[0]
                base_image = doc.extract_image(xref)
                image_bytes = base_image["image"]
                image_ext = base_image["extension"]
                
                img_path = output_dir / f"embed_{page_num + 1}_{img_index + 1}.{image_ext}"
                with open(img_path, "wb") as f:
                    f.write(image_bytes)
                
                imagenes_extraidas.append({
                    'path': img_path,
                    'page': page_num + 1,
                    'index': img_index + 1
                })
        
        doc.close()
        logger.info(f"Extraídas {len(imagenes_extraidas)} imágenes embebidas")
    except Exception as e:
        logger.error(f"Error extrayendo imágenes: {e}")
    
    return imagenes_extraidas


def limpiar_texto(texto: str) -> str:
    """Limpia y formatea el texto extraído."""
    # Eliminar líneas muy cortas o vacías repetidas
    lineas = texto.split('\n')
    lineas_limpias = []
    
    for linea in lineas:
        linea = linea.strip()
        if linea and len(linea) > 2:
            lineas_limpias.append(linea)
    
    # Unir con saltos de línea normales
    return '\n\n'.join(lineas_limpias)


def convertir_a_markdown(texto: str, titulo: str) -> str:
    """Convierte texto a formato Markdown básico."""
    md = f"# {titulo}\n\n"
    md += f"*Documento procesado el {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*\n\n"
    md += "---\n\n"
    md += texto
    return md


def procesar_pdf(pdf_path: Path) -> dict:
    """Procesa un PDF completo y genera Markdown + extrae imágenes."""
    doc_name = pdf_path.stem
    logger.info(f"Procesando: {doc_name}")
    
    # Crear estructura de carpetas
    doc_dir = OUTPUT_DIR / doc_name
    markdown_dir = doc_dir / "markdown"
    imagenes_dir = doc_dir / "imagenes"
    
    markdown_dir.mkdir(parents=True, exist_ok=True)
    imagenes_dir.mkdir(parents=True, exist_ok=True)
    
    # Crear base de datos
    db_path = crear_base_datos(doc_name)
    
    # Extraer texto
    logger.info("Extrayendo texto...")
    texto = extraer_texto_fitz(pdf_path)
    
    # Si el texto está vacío o es muy corto, intentar OCR
    if len(texto.strip()) < 100 and TRY_IMPORT.get('pdf2image'):
        logger.info("Texto insuficiente, intentando OCR...")
        imagenes_paginas = convertir_pdf_imagenes(pdf_path, imagenes_dir)
        
        texto_ocr = ""
        for img_path in imagenes_paginas:
            texto_ocr += extraer_texto_ocr(img_path) + "\n\n"
        
        if len(texto_ocr.strip()) > len(texto.strip()):
            texto = texto_ocr
    
    # Limpiar texto
    texto_limpio = limpiar_texto(texto)
    
    # Convertir a Markdown
    markdown_content = convertir_a_markdown(texto_limpio, doc_name.replace('_', ' '))
    
    # Guardar Markdown
    md_path = markdown_dir / f"{doc_name}.md"
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(markdown_content)
    
    # Extraer imágenes embebidas
    logger.info("Extrayendo imágenes...")
    imagenes_extraidas = extraer_imagenes_pdf(pdf_path, imagenes_dir)
    
    # Convertir páginas a imágenes (para referencia)
    if TRY_IMPORT.get('pdf2image'):
        logger.info("Convirtiendo páginas a imágenes...")
        convertir_pdf_imagenes(pdf_path, imagenes_dir)
    
    # Guardar en base de datos
    conn = sqlite3.connect(str(db_path))
    cursor = conn.cursor()
    
    # Insertar documento
    cursor.execute("""
        INSERT INTO documentos (nombre, tipo, fuente, contenido_markdown, path_markdown)
        VALUES (?, ?, ?, ?, ?)
    """, (doc_name, 'pdf', str(pdf_path), texto_limpio[:50000], str(md_path)))
    
    doc_id = cursor.lastrowid
    
    # Insertar imágenes
    for img in imagenes_extraidas:
        cursor.execute("""
            INSERT INTO imagenes (documento_id, path_local, tipo_contenido)
            VALUES (?, ?, ?)
        """, (doc_id, str(img['path']), 'embedida'))
    
    # Registrar procesamiento
    cursor.execute("""
        INSERT INTO procesamiento (documento_id, etapa, estado, mensaje)
        VALUES (?, ?, ?, ?)
    """, (doc_id, 'extraccion', 'completado', f'Páginas procesadas'))
    
    conn.commit()
    conn.close()
    
    logger.info(f"Completado: {doc_name} - {len(imagenes_extraidas)} imágenes extraídas")
    
    return {
        'documento': doc_name,
        'markdown': str(md_path),
        'imagenes': len(imagenes_extraidas),
        'db': str(db_path)
    }


def obtener_lang_tesseract() -> str:
    """Obtiene el código de idioma para tesseract."""
    # Intentar usar español e inglés
    return 'eng+spa'


def main():
    """Procesa todos los PDFs en la carpeta pdf/."""
    logger.info("=" * 60)
    logger.info("INICIANDO EXTRACCIÓN DE PDFs")
    logger.info("=" * 60)
    
    # Verificar que existe la carpeta de PDFs
    if not PDF_DIR.exists():
        logger.error(f"No existe la carpeta: {PDF_DIR}")
        return
    
    # Obtener lista de PDFs
    pdfs = list(PDF_DIR.glob("*.pdf"))
    
    if not pdfs:
        logger.warning("No se encontraron PDFs en la carpeta")
        return
    
    logger.info(f"Encontrados {len(pdfs)} PDFs para procesar")
    
    resultados = []
    for pdf_path in pdfs:
        try:
            resultado = procesar_pdf(pdf_path)
            resultados.append(resultado)
        except Exception as e:
            logger.error(f"Error procesando {pdf_path.name}: {e}")
    
    # Resumen
    logger.info("=" * 60)
    logger.info("RESUMEN DEL PROCESAMIENTO")
    logger.info("=" * 60)
    
    for r in resultados:
        logger.info(f"  ✓ {r['documento']}: {r['imagenes']} imágenes, DB: {r['db']}")
    
    logger.info(f"\nTotal procesados: {len(resultados)}/{len(pdfs)}")


if __name__ == "__main__":
    # Agregar el directorio actual al path para importaciones
    sys.path.insert(0, str(BASE_DIR))
    main()