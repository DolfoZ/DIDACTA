"""
mejorar_imagenes.py - Mejora la calidad de imágenes extraídas de PDFs
Aplica contraste, nitidez y opcionalmente upscaling
Parte del pipeline de procesamiento Didacta
"""
import os
import sys
import sqlite3
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
OUTPUT_DIR = BASE_DIR / "manuales" / "procesados"

# Verificar disponibilidad de OpenCV
TRY_OPENCV = True
try:
    import cv2
    import numpy as np
    from PIL import Image
except ImportError:
    TRY_OPENCV = False
    logger.warning("opencv-python no instalado. pip install opencv-python pillow")


def cargar_imagen(ruta: Path):
    """Carga una imagen usando OpenCV o PIL."""
    if not TRY_OPENCV:
        return None
    
    try:
        img = cv2.imread(str(ruta))
        if img is None:
            # Intentar con PIL
            pil_img = Image.open(ruta)
            img = cv2.cvtColor(np.array(pil_img), cv2.COLOR_RGB2BGR)
        return img
    except Exception as e:
        logger.error(f"Error cargando imagen {ruta}: {e}")
        return None


def guardar_imagen(img, ruta: Path):
    """Guarda una imagen usando OpenCV."""
    if not TRY_OPENCV:
        return False
    
    try:
        cv2.imwrite(str(ruta), img)
        return True
    except Exception as e:
        logger.error(f"Error guardando imagen {ruta}: {e}")
        return False


def mejorar_contraste(img, clip_limit=2.0, tile_size=8):
    """Aplica mejora de contraste usando CLAHE."""
    if img is None or not TRY_OPENCV:
        return img
    
    try:
        # Convertir a LAB
        lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
        l, a, b = cv2.split(lab)
        
        # Aplicar CLAHE
        clahe = cv2.createCLAHE(clipLimit=clip_limit, tileGridSize=(tile_size, tile_size))
        l = clahe.apply(l)
        
        # Unir canales
        lab = cv2.merge([l, a, b])
        result = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)
        
        return result
    except Exception as e:
        logger.error(f"Error mejorando contraste: {e}")
        return img


def mejorar_nitidez(img, kernel_size=(3, 3)):
    """Aplica sharpening para mejorar nitidez."""
    if img is None or not TRY_OPENCV:
        return img
    
    try:
        # Kernel de sharpening
        kernel = np.array([
            [-1, -1, -1],
            [-1,  9, -1],
            [-1, -1, -1]
        ]) / 9.0
        
        sharpened = cv2.filter2D(img, -1, kernel)
        return sharpened
    except Exception as e:
        logger.error(f"Error mejorando nitidez: {e}")
        return img


def ajustar_brillo_contraste(img, alpha=1.1, beta=10):
    """Ajusta brillo (beta) y contraste (alpha)."""
    if img is None or not TRY_OPENCV:
        return img
    
    try:
        # alpha: control de contraste (1.0-3.0)
        # beta: control de brillo (0-100)
        return cv2.convertScaleAbs(img, alpha=alpha, beta=beta)
    except Exception as e:
        logger.error(f"Error ajustando brillo/contraste: {e}")
        return img


def convertir_a_escala_grises(img):
    """Convierte a escala de grises si es beneficial."""
    if img is None or not TRY_OPENCV:
        return img
    
    try:
        # Verificar si es mejor convertir a gris
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        # Aplicar CLAHE a gris
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
        enhanced = clahe.apply(gray)
        
        # Convertir de vuelta a BGR
        return cv2.cvtColor(enhanced, cv2.COLOR_GRAY2BGR)
    except Exception as e:
        logger.error(f"Error convirtiendo a grises: {e}")
        return img


def aplicar_mejoras_completas(img_path: Path, opciones: dict = None) -> Path:
    """Aplica el pipeline completo de mejoras a una imagen."""
    if opciones is None:
        opciones = {
            'contraste': True,
            'nitidez': True,
            'brillo': True,
            'escala_grises': False
        }
    
    if not TRY_OPENCV:
        logger.warning("OpenCV no disponible, saltando mejora")
        return img_path
    
    # Cargar imagen
    img = cargar_imagen(img_path)
    if img is None:
        logger.error(f"No se pudo cargar: {img_path}")
        return img_path
    
    original_shape = img.shape
    
    # Aplicar mejoras en orden
    if opciones.get('contraste'):
        img = mejorar_contraste(img)
    
    if opciones.get('brillo'):
        img = ajustar_brillo_contraste(img, alpha=1.1, beta=5)
    
    if opciones.get('nitidez'):
        img = mejorar_nitidez(img)
    
    if opciones.get('escala_grises'):
        img = convertir_a_escala_grises(img)
    
    # Guardar imagen mejorada
    mejorada_path = img_path.parent / f"mejorada_{img_path.name}"
    if guardar_imagen(img, mejorada_path):
        logger.info(f"Imagen mejorada guardada: {mejorada_path}")
        return mejorada_path
    
    return img_path


def procesar_carpeta_imagenes(carpeta: Path, opciones: dict = None) -> dict:
    """Procesa todas las imágenes en una carpeta."""
    if not carpeta.exists():
        logger.warning(f"Carpeta no existe: {carpeta}")
        return {'total': 0, 'mejoradas': 0, 'errores': 0}
    
    # Extensiones de imagen válidas
    extensiones = ['.png', '.jpg', '.jpeg', '.bmp', '.tiff', '.webp']
    
    imagenes = []
    for ext in extensiones:
        imagenes.extend(carpeta.glob(f"*{ext}"))
        imagenes.extend(carpeta.glob(f"*{ext.upper()}"))
    
    logger.info(f"Encontradas {len(imagenes)} imágenes en {carpeta}")
    
    resultados = {'total': len(imagenes), 'mejoradas': 0, 'errores': 0}
    
    for img_path in imagenes:
        try:
            mejorada = aplicar_mejoras_completas(img_path, opciones)
            if mejorada != img_path:
                resultados['mejoradas'] += 1
        except Exception as e:
            logger.error(f"Error procesando {img_path.name}: {e}")
            resultados['errores'] += 1
    
    return resultados


def actualizar_base_datos(db_path: Path, documento_id: int, img_original: str, img_mejorada: str):
    """Actualiza la base de datos con las rutas de imágenes mejoradas."""
    if not db_path.exists():
        return
    
    try:
        conn = sqlite3.connect(str(db_path))
        cursor = conn.cursor()
        
        cursor.execute("""
            UPDATE imagenes 
            SET path_local = ? 
            WHERE documento_id = ? AND path_local LIKE ?
        """, (img_mejorada, documento_id, f"%{img_original}%"))
        
        conn.commit()
        conn.close()
    except Exception as e:
        logger.error(f"Error actualizando BD: {e}")


def main():
    """Procesa todas las carpetas de imágenes en procesados/."""
    logger.info("=" * 60)
    logger.info("INICIANDO MEJORA DE IMÁGENES")
    logger.info("=" * 60)
    
    if not OUTPUT_DIR.exists():
        logger.error(f"No existe la carpeta: {OUTPUT_DIR}")
        return
    
    # Opciones de mejora
    opciones = {
        'contraste': True,  # CLAHE para mejorar contraste
        'nitidez': True,    # Sharpening
        'brillo': True,     # Ajuste leve de brillo
        'escala_grises': False  # Opcional, solo si hay problemas de calidad
    }
    
    # Procesar cada documento
    carpetas = [d for d in OUTPUT_DIR.iterdir() if d.is_dir()]
    
    logger.info(f"Encontradas {len(carpetas)} carpetas de documentos")
    
    total_resultados = []
    for carpeta in carpetas:
        imagenes_dir = carpeta / "imagenes"
        if imagenes_dir.exists():
            logger.info(f"Procesando: {carpeta.name}")
            resultado = procesar_carpeta_imagenes(imagenes_dir, opciones)
            resultado['documento'] = carpeta.name
            total_resultados.append(resultado)
    
    # Resumen
    logger.info("=" * 60)
    logger.info("RESUMEN DE MEJORAS")
    logger.info("=" * 60)
    
    total_img = sum(r['total'] for r in total_resultados)
    total_mejoradas = sum(r['mejoradas'] for r in total_resultados)
    total_errores = sum(r['errores'] for r in total_resultados)
    
    logger.info(f"Total imágenes: {total_img}")
    logger.info(f"Mejoradas: {total_mejoradas}")
    logger.info(f"Errores: {total_errores}")
    
    logger.info("\nPor documento:")
    for r in total_resultados:
        logger.info(f"  {r['documento']}: {r['mejoradas']}/{r['total']}")


if __name__ == "__main__":
    sys.path.insert(0, str(BASE_DIR))
    main()