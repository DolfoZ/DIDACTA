"""
fusionar_bd.py - Fusiona todas las bases de datos en la base central
Crea la red neural de conocimiento unificada
Parte del pipeline de procesamiento Didacta
"""
import os
import sys
import sqlite3
import logging
import shutil
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
CENTRAL_DB = BASE_DIR / "persistencia" / "conocimiento.db"


def crear_base_central():
    """Crea la base de datos central con la estructura completa."""
    if CENTRAL_DB.exists():
        # Hacer backup
        backup = BASE_DIR / "persistencia" / f"conocimiento_backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.db"
        shutil.copy2(CENTRAL_DB, backup)
        logger.info(f"Backup creado: {backup}")
    
    conn = sqlite3.connect(str(CENTRAL_DB))
    cursor = conn.cursor()
    
    # Tabla de documentos fuente
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS documentos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            tipo TEXT,
            fuente TEXT,
            origen TEXT,  -- 'procesados/FM_6-40', 'html_didacta', etc.
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
            path_original TEXT,
            path_mejorado TEXT,
            tipo_contenido TEXT,
            width INTEGER,
            height INTEGER
        )
    """)
    
    # Tabla de categorías para la red neural
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS categorias (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT UNIQUE NOT NULL,
            descripcion TEXT,
            count INTEGER DEFAULT 0,
            fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    
    # Tabla de metadatos de fusión
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS fusion_log (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            db_origen TEXT,
            tabla_origen TEXT,
            registros_importados INTEGER,
            fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    
    # Índices para búsqueda rápida (skip si es virtual table)
    try:
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_conocimiento_categoria ON conocimiento(categoria)")
    except sqlite3.OperationalError:
        pass  # Virtual table, no indexing needed
    try:
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_conocimiento_tags ON conocimiento(tags)")
    except sqlite3.OperationalError:
        pass
    try:
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_documentos_tipo ON documentos(tipo)")
    except sqlite3.OperationalError:
        pass
    
    conn.commit()
    conn.close()
    
    logger.info(f"Base de datos central creada/actualizada: {CENTRAL_DB}")
    return CENTRAL_DB


def obtener_registros_db(db_path: Path) -> dict:
    """Obtiene todos los registros de una base de datos."""
    if not db_path.exists():
        return {'documentos': [], 'conocimiento': [], 'imagenes': []}
    
    try:
        conn = sqlite3.connect(str(db_path))
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        # Obtener documentos
        cursor.execute("SELECT * FROM documentos")
        documentos = [dict(row) for row in cursor.fetchall()]
        
        # Obtener conocimiento
        cursor.execute("SELECT * FROM conocimiento")
        conocimiento = [dict(row) for row in cursor.fetchall()]
        
        # Obtener imágenes
        cursor.execute("SELECT * FROM imagenes")
        imagenes = [dict(row) for row in cursor.fetchall()]
        
        conn.close()
        
        return {
            'documentos': documentos,
            'conocimiento': conocimiento,
            'imagenes': imagenes
        }
    except Exception as e:
        logger.error(f"Error leyendo {db_path}: {e}")
        return {'documentos': [], 'conocimiento': [], 'imagenes': []}


def fusionar_registros(registros: dict, origen: str) -> dict:
    """Fusiona registros de una DB origen a la central."""
    conn = sqlite3.connect(str(CENTRAL_DB))
    cursor = conn.cursor()
    
    doc_id_map = {}  # Mapa de IDs originales a nuevos
    conocimiento_id_map = {}
    
    # Insertar documentos
    documentos_insertados = 0
    for doc in registros.get('documentos', []):
        try:
            cursor.execute("""
                INSERT INTO documentos (nombre, tipo, fuente, origen, contenido_markdown, path_markdown, fecha_procesamiento)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (
                doc.get('nombre', ''),
                doc.get('tipo', ''),
                doc.get('fuente', ''),
                origen,
                doc.get('contenido_markdown', ''),
                doc.get('path_markdown', ''),
                doc.get('fecha_procesamiento', datetime.now().isoformat())
            ))
            doc_id_map[doc['id']] = cursor.lastrowid
            documentos_insertados += 1
        except Exception as e:
            logger.error(f"Error insertando documento: {e}")
    
    # Insertar conocimiento
    conocimiento_insertados = 0
    for con in registros.get('conocimiento', []):
        try:
            original_doc_id = con.get('documento_id')
            nuevo_doc_id = doc_id_map.get(original_doc_id, 1)
            
            cursor.execute("""
                INSERT INTO conocimiento (documento_id, categoria, nombre, descripcion, especificaciones, tags, nivel_confianza, fecha_creacion)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                nuevo_doc_id,
                con.get('categoria', ''),
                con.get('nombre', ''),
                con.get('descripcion', ''),
                con.get('especificaciones', ''),
                con.get('tags', ''),
                con.get('nivel_confianza', 0.5),
                con.get('fecha_creacion', datetime.now().isoformat())
            ))
            conocimiento_id_map[con['id']] = cursor.lastrowid
            conocimiento_insertados += 1
        except Exception as e:
            logger.error(f"Error insertando conocimiento: {e}")
    
    # Insertar imágenes
    imagenes_insertadas = 0
    for img in registros.get('imagenes', []):
        try:
            original_doc_id = img.get('documento_id')
            nuevo_doc_id = doc_id_map.get(original_doc_id, 1)
            
            cursor.execute("""
                INSERT INTO imagenes (documento_id, nombre, path_local, tipo_contenido)
                VALUES (?, ?, ?, ?)
            """, (
                nuevo_doc_id,
                img.get('nombre', ''),
                img.get('path_local', ''),
                img.get('tipo_contenido', '')
            ))
            imagenes_insertadas += 1
        except Exception as e:
            logger.error(f"Error insertando imagen: {e}")
    
    # Registrar fusión
    cursor.execute("""
        INSERT INTO fusion_log (db_origen, tabla_origen, registros_importados)
        VALUES (?, ?, ?)
    """, (origen, 'todos', documentos_insertados + conocimiento_insertados + imagenes_insertadas))
    
    conn.commit()
    conn.close()
    
    return {
        'documentos': documentos_insertados,
        'conocimiento': conocimiento_insertados,
        'imagenes': imagenes_insertadas
    }


def actualizar_categorias():
    """Actualiza el conteo de categorías."""
    if not CENTRAL_DB.exists():
        return
    
    try:
        conn = sqlite3.connect(str(CENTRAL_DB))
        cursor = conn.cursor()
        
        # Obtener categorías únicas
        cursor.execute("SELECT DISTINCT categoria FROM conocimiento WHERE categoria IS NOT NULL")
        categorias = [row[0] for row in cursor.fetchall()]
        
        # Actualizar conteo
        for cat in categorias:
            cursor.execute("""
                INSERT OR REPLACE INTO categorias (nombre, count)
                SELECT ?, COUNT(*) FROM conocimiento WHERE categoria = ?
            """, (cat, cat))
        
        conn.commit()
        conn.close()
        
        logger.info(f"Categorías actualizadas: {len(categorias)}")
    except Exception as e:
        logger.error(f"Error actualizando categorías: {e}")


def main():
    """Fusiona todas las bases de datos en la central."""
    logger.info("=" * 60)
    logger.info("INICIANDO FUSIÓN DE BASES DE DATOS")
    logger.info("=" * 60)
    
    # Crear base central
    crear_base_central()
    
    if not OUTPUT_DIR.exists():
        logger.error(f"No existe la carpeta: {OUTPUT_DIR}")
        return
    
    # Buscar todas las bases de datos
    dbs_encontradas = []
    
    # Buscar en procesados
    for db_file in OUTPUT_DIR.rglob("conocimiento.db"):
        dbs_encontradas.append(('procesados', db_file))
    
    # Buscar en html (si existe)
    html_dir = BASE_DIR / "manuales" / "html"
    if html_dir.exists():
        for db_file in html_dir.rglob("conocimiento.db"):
            dbs_encontradas.append(('html', db_file))
    
    logger.info(f"Encontradas {len(dbs_encontradas)} bases de datos")
    
    total_registros = {'documentos': 0, 'conocimiento': 0, 'imagenes': 0}
    
    for tipo, db_path in dbs_encontradas:
        logger.info(f"Procesando: {db_path}")
        
        # Obtener registros
        registros = obtener_registros_db(db_path)
        
        # Calcular origen
        try:
            origen = str(db_path.relative_to(BASE_DIR))
        except:
            origen = str(db_path)
        
        # Fusionar
        resultado = fusionar_registros(registros, origen)
        
        logger.info(f"  -> Documentos: {resultado['documentos']}, "
                   f"Conocimiento: {resultado['conocimiento']}, "
                   f"Imágenes: {resultado['imagenes']}")
        
        total_registros['documentos'] += resultado['documentos']
        total_registros['conocimiento'] += resultado['conocimiento']
        total_registros['imagenes'] += resultado['imagenes']
    
    # Actualizar categorías
    actualizar_categorias()
    
    # Resumen final
    logger.info("=" * 60)
    logger.info("RESUMEN DE FUSIÓN")
    logger.info("=" * 60)
    logger.info(f"Total documentos: {total_registros['documentos']}")
    logger.info(f"Total conocimiento: {total_registros['conocimiento']}")
    logger.info(f"Total imágenes: {total_registros['imagenes']}")
    logger.info(f"\nBase de datos central: {CENTRAL_DB}")


if __name__ == "__main__":
    sys.path.insert(0, str(BASE_DIR))
    main()