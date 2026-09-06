"""
convertir_html.py - Convierte HTMLs de Didacta a Markdown
Parte del pipeline de procesamiento Didacta
"""
import os
import sys
import sqlite3
import logging
from pathlib import Path
from datetime import datetime
from bs4 import BeautifulSoup
import re

# Configuración de logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Rutas del proyecto
BASE_DIR = Path(__file__).parent.parent.parent
DIDACTA_DIR = BASE_DIR / "Didacta"
HTML_OUTPUT_DIR = BASE_DIR / "manuales" / "html"
OUTPUT_DIR = BASE_DIR / "manuales" / "procesados"

# Intentar importar dependencias
TRY_BS4 = True
TRY_HTML2TEXT = True

try:
    import html2text
except ImportError:
    TRY_HTML2TEXT = False
    logger.warning("html2text no instalado. pip install html2text")


def crear_base_datos_html(doc_name: str) -> Path:
    """Crea la estructura de base de datos para HTMLs."""
    doc_dir = OUTPUT_DIR / f"html_{doc_name}"
    doc_dir.mkdir(parents=True, exist_ok=True)
    
    db_path = doc_dir / "conocimiento.db"
    
    conn = sqlite3.connect(str(db_path))
    cursor = conn.cursor()
    
    # Tabla de documentos
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS documentos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            tipo TEXT DEFAULT 'html',
            fuente TEXT,
            contenido_markdown TEXT,
            path_markdown TEXT,
            fecha_procesamiento TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    
    # Tabla de conocimiento
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS conocimiento (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            documento_id INTEGER REFERENCES documentos(id),
            categoria TEXT,
            nombre TEXT,
            descripcion TEXT,
            especificaciones TEXT,
            tags TEXT,
            nivel_confianza REAL DEFAULT 0.8,
            fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    
    # Tabla de imágenes (si hay)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS imagenes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            documento_id INTEGER REFERENCES documentos(id),
            conocimiento_id INTEGER REFERENCES conocimiento(id),
            nombre TEXT,
            path_local TEXT,
            tipo_contenido TEXT
        )
    """)
    
    conn.commit()
    conn.close()
    
    return db_path


def extraer_titulo(soup: BeautifulSoup) -> str:
    """Extrae el título del documento HTML."""
    # Buscar en título, h1, o meta
    if soup.title:
        return soup.title.string or "Sin título"
    
    h1 = soup.find('h1')
    if h1:
        return h1.get_text(strip=True)
    
    meta = soup.find('meta', attrs={'name': 'title'})
    if meta and meta.get('content'):
        return meta['content']
    
    return "Documento sin título"


def detectar_categoria(nombre_archivo: str, contenido: str) -> str:
    """Detecta la categoría del documento basedo en nombre y contenido."""
    nombre = nombre_archivo.lower()
    
    # Categorías basadas en el nombre del archivo
    if 'cartridge' in nombre:
        return 'cartucho'
    elif 'projectile' in nombre:
        return 'proyectil'
    elif 'propelling' in nombre or 'charge' in nombre:
        return 'carga'
    elif 'fuze' in nombre or 'espoleta' in nombre:
        return 'espoleta'
    elif 'biblioteca' in nombre:
        return 'biblioteca'
    elif 'carousel' in nombre:
        return 'index'
    else:
        # Buscar en contenido
        if '155mm' in contenido:
            return 'calibre_155'
        elif '105mm' in contenido:
            return 'calibre_105'
        return 'general'


def extraer_especificaciones(soup: BeautifulSoup) -> dict:
    """Extrae especificaciones técnicas del HTML."""
    specs = {}
    
    # Buscar tablas
    tablas = soup.find_all('table')
    for i, tabla in enumerate(tablas):
        filas = tabla.find_all('tr')
        if filas:
            spec_key = f"tabla_{i + 1}"
            spec_data = []
            for fila in filas[:10]:  # Limitar a 10 filas
                celdas = fila.find_all(['td', 'th'])
                if len(celdas) >= 2:
                    clave = celdas[0].get_text(strip=True)
                    valor = celdas[1].get_text(strip=True)
                    if clave and valor:
                        spec_data.append(f"{clave}: {valor}")
            if spec_data:
                specs[spec_key] = spec_data
    
    # Buscar listas de datos
    listas = soup.find_all(['ul', 'ol'])
    if listas:
        specs['listas'] = []
        for lista in listas[:3]:
            items = [item.get_text(strip=True) for item in lista.find_all('li')[:5]]
            if items:
                specs['listas'].append(items)
    
    return specs


def convertir_a_markdown(html_content: str, titulo: str) -> str:
    """Convierte HTML a Markdown."""
    if not TRY_HTML2TEXT:
        # Fallback básico
        soup = BeautifulSoup(html_content, 'html.parser')
        return soup.get_text(separator='\n\n')
    
    try:
        # Configurar html2text
        h = html2text.HTML2Text()
        h.body_width = 0  # No limitar ancho de línea
        h.unicode_snob = True
        h.ignore_links = False
        h.ignore_images = False
        h.ignore_emphasis = False
        
        md = h.handle(html_content)
        
        # Agregar título al inicio
        md = f"# {titulo}\n\n*Documento convertido el {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*\n\n---\n\n{md}"
        
        return md
    except Exception as e:
        logger.error(f"Error convirtiendo a markdown: {e}")
        soup = BeautifulSoup(html_content, 'html.parser')
        return f"# {titulo}\n\n{soup.get_text(separator='\n\n')}"


def procesar_html(html_path: Path, html_output_dir: Path) -> dict:
    """Procesa un archivo HTML individual."""
    doc_name = html_path.stem
    logger.info(f"Procesando HTML: {doc_name}")
    
    # Leer contenido HTML
    try:
        with open(html_path, 'r', encoding='utf-8', errors='ignore') as f:
            html_content = f.read()
    except Exception as e:
        logger.error(f"Error leyendo {html_path.name}: {e}")
        return None
    
    # Parsear HTML
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Extraer título
    titulo = extraer_titulo(soup)
    
    # Detectar categoría
    categoria = detectar_categoria(html_path.name, html_content)
    
    # Extraer especificaciones
    especificaciones = extraer_especificaciones(soup)
    
    # Convertir a Markdown
    markdown_content = convertir_a_markdown(html_content, titulo)
    
    # Guardar Markdown
    md_path = html_output_dir / f"{doc_name}.md"
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(markdown_content)
    
    # Crear base de datos para este grupo de HTMLs
    db_path = crear_base_datos_html("didacta_html")
    
    # Guardar en base de datos
    conn = sqlite3.connect(str(db_path))
    cursor = conn.cursor()
    
    # Insertar documento
    cursor.execute("""
        INSERT INTO documentos (nombre, tipo, fuente, contenido_markdown, path_markdown)
        VALUES (?, ?, ?, ?, ?)
    """, (doc_name, 'html', str(html_path), markdown_content[:50000], str(md_path)))
    
    doc_id = cursor.lastrowid
    
    # Insertar conocimiento
    cursor.execute("""
        INSERT INTO conocimiento (documento_id, categoria, nombre, descripcion, especificaciones, tags)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        doc_id,
        categoria,
        titulo[:100],
        f"Documento HTML de Didacta: {doc_name}",
        str(especificaciones),
        f"{categoria},didacta,html"
    ))
    
    conn.commit()
    conn.close()
    
    return {
        'documento': doc_name,
        'categoria': categoria,
        'markdown': str(md_path),
        'db': str(db_path)
    }


def main():
    """Procesa todos los HTMLs de Didacta."""
    logger.info("=" * 60)
    logger.info("INICIANDO CONVERSIÓN DE HTMLs")
    logger.info("=" * 60)
    
    # Verificar que existe la carpeta de Didacta
    if not DIDACTA_DIR.exists():
        logger.error(f"No existe la carpeta: {DIDACTA_DIR}")
        return
    
    # Crear carpeta de salida
    HTML_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    
    # Obtener lista de HTMLs (excluyendo biblioteca y carousel)
    htmls = [f for f in DIDACTA_DIR.glob("*.html") 
             if f.name not in ['biblioteca.html', 'carousel.html']]
    
    if not htmls:
        logger.warning("No se encontraron HTMLs en Didacta")
        return
    
    logger.info(f"Encontrados {len(htmls)} HTMLs para procesar")
    
    resultados = []
    for html_path in htmls:
        try:
            resultado = procesar_html(html_path, HTML_OUTPUT_DIR)
            if resultado:
                resultados.append(resultado)
        except Exception as e:
            logger.error(f"Error procesando {html_path.name}: {e}")
    
    # Resumen
    logger.info("=" * 60)
    logger.info("RESUMEN DE CONVERSIÓN HTML")
    logger.info("=" * 60)
    
    # Agrupar por categoría
    categorias = {}
    for r in resultados:
        cat = r.get('categoria', 'unknown')
        if cat not in categorias:
            categorias[cat] = 0
        categorias[cat] += 1
    
    for cat, count in categorias.items():
        logger.info(f"  {cat}: {count} documentos")
    
    logger.info(f"\nTotal procesados: {len(resultados)}/{len(htmls)}")
    logger.info(f"Markdown guardado en: {HTML_OUTPUT_DIR}")


if __name__ == "__main__":
    sys.path.insert(0, str(BASE_DIR))
    main()