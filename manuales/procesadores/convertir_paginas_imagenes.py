"""
convertir_paginas_imagenes.py - Convierte páginas de PDF a imágenes y las mejora
"""
import os
import sys
import cv2
import numpy as np
import fitz
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

BASE_DIR = Path(__file__).parent.parent.parent
PDF_DIR = BASE_DIR / "manuales" / "pdf"
OUTPUT_DIR = BASE_DIR / "manuales" / "procesados"


def mejorar_imagen_cv2(img_path: Path) -> Path:
    """Aplica mejoras de contraste y nitidez a una imagen."""
    img = cv2.imread(str(img_path))
    if img is None:
        return img_path
    
    # Aplicar CLAHE para mejorar contraste
    lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    l = clahe.apply(l)
    lab = cv2.merge([l, a, b])
    img = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)
    
    # Aplicar sharpening
    kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]]) / 9.0
    img = cv2.filter2D(img, -1, kernel)
    
    # Guardar versión mejorada
    mejorada_path = img_path.parent / f"mejorada_{img_path.name}"
    cv2.imwrite(str(mejorada_path), img)
    
    return mejorada_path


def convertir_pdf_a_imagenes(pdf_path: Path, output_dir: Path) -> list:
    """Convierte todas las páginas de un PDF a imágenes mejoradas."""
    doc = fitz.open(str(pdf_path))
    imagenes = []
    
    for page_num in range(len(doc)):
        page = doc[page_num]
        # Renderizar a 2x para mejor calidad
        pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))
        
        # Guardar imagen original
        img_path = output_dir / f"pagina_{page_num + 1}.png"
        pix.save(str(img_path))
        
        # Mejorar imagen
        mejorada = mejorar_imagen_cv2(img_path)
        imagenes.append(mejorada)
    
    doc.close()
    return imagenes


def main():
    logger.info("Convirtiendo PDFs a imágenes mejoradas...")
    
    pdfs = list(PDF_DIR.glob("*.pdf"))
    logger.info(f"Total PDFs: {len(pdfs)}")
    
    for pdf_path in pdfs:
        doc_name = pdf_path.stem.strip()  # Limpiar espacios
        # Sanitizar nombre para path
        safe_name = "".join(c for c in doc_name if c.isalnum() or c in (' ', '-', '_')).rstrip()
        imagenes_dir = OUTPUT_DIR / safe_name / "imagenes"
        
        # Verificar si ya tiene imágenes
        if imagenes_dir.exists():
            existing = list(imagenes_dir.glob("pagina_*.png"))
            if len(existing) > 5:  # Si tiene más de 5 páginas, saltar
                logger.info(f"SALTANDO {doc_name}: ya tiene {len(existing)} imágenes")
                continue
        
        imagenes_dir.mkdir(parents=True, exist_ok=True)
        
        logger.info(f"Procesando: {doc_name}")
        try:
            imagenes = convertir_pdf_a_imagenes(pdf_path, imagenes_dir)
            logger.info(f"  -> {len(imagenes)} páginas convertidas y mejoradas")
        except Exception as e:
            logger.error(f"Error en {doc_name}: {e}")


if __name__ == "__main__":
    main()