# DIDACTA

**Sistema de Ayuda y Documentación Técnica** para el **CDT Santa Bárbara** — Sistema de Artillería.

Aplicación de ayuda basada en **HTML Help Workshop (Microsoft HTML Help / .chm compatible)** con navegador web embebido, sistema de búsqueda, índice temático y visualizador de PDFs integrado.

---

## Características principales

| Componente | Descripción |
|------------|-------------|
| **Formato** | HTML Help Workshop / Microsoft HTML Help (.chm compatible) |
| **Motor de renderizado** | WebView2 (Edge/Chromium) embebido |
| **Navegación** | Índice temático (TOC), búsqueda full-text, índice alfabético |
| **Contenido** | 300+ temas HTML + 500+ PDFs de cartuchos/proyectiles/cargas |
| **Búsqueda** | Full-text search con índice invertido (JS nativo) |
| **Visualizador PDF** | Embebido (WebView2 + PDF.js) |
| **Tema visual** | Modo oscuro táctico (negro/naranja/ámbar) |

---

## Contenido incluido

| Categoría | Cantidad | Descripción |
|-----------|----------|-------------|
| **Temas HTML** | 300+ | Cartuchos, proyectiles, cargas, manuales |
| **Cartuchos 105mm** | 100+ | HE, HEAT, APERS, ILLUM, SMOKE, TP, etc. |
| **Proyectiles 155mm** | 80+ | HE, HEAT, HERA, ICM, ILLUM, SMOKE, etc. |
| **Cargas propulsoras** | 30+ | M1, M3A1, M4A2, M119A2, M203, M203A1, etc. |
| **Proyectiles 105mm** | 60+ | M1, M323, M324, M326, M392A1, M393A1/2, M444, M456, M483A1, M485, M549A1, M548, M67, M692, M718, M724, M724A1, M731, M741, M795, M804, M712, M760, M825, M864, M898, M913, M915, M919, M927, M982 |
| **Cargas 155mm** | 20+ | M1, M2, M3, M3A1, M3A2, M4, M4A1, M4A2, M119, M119A1, M119A2, M203, M203A1, M231, M232, M232A1 |

---

## Interfaz de Usuario

| Área | Descripción |
|------|-------------|
| **Barra superior** | Título "DIDACTA", logo CDT, botones minimizar/maximizar/cerrar |
| **Panel izquierdo (TOC)** | Índice temático jerárquico (3 niveles), búsqueda en vivo |
| **Panel central** | Contenido HTML renderizado (WebView2) |
| **Panel derecho** | Índice alfabético / búsqueda full-text |
| **Barra inferior** | Zoom, imprimir, página anterior/siguiente, favoritos |

---

## Instalación

### Instalador oficial
```bash
# Descargar desde Releases
Didacta_Setup.exe
```
- Instala en `C:\Program Files\DIDACTA\`
- Incluye 2000+ archivos HTML + assets
- Accesos directos: Menú Inicio + Escritorio
- Icono **Didacta.ico** en app, taskbar, installer, uninstaller
- Desinstalador incluido

### Desarrollo
```bash
# Clonar
git clone https://github.com/DolfoZ/DIDACTA.git
cd DIDACTA

# Ejecutar
python Didacta/app.py
```

---

## Build & Distribución

### Instalador Inno Setup
```bash
ISCC.exe Didacta.iss
```
- Output: `Didacta_Setup.exe` (~500 MB)
- Instala en `C:\Program Files\DIDACTA\`
- Icono **Didacta.ico** en setup, app, uninstaller, shortcut

---

## Estructura del proyecto

```
DIDACTA/
├── Didacta/                    # Contenido principal
│   ├── biblioteca.html         # Página principal
│   ├── *.html                  # 300+ temas (cartuchos, proyectiles, cargas)
│   ├── css/                    # Estilos (tema oscuro táctico)
│   ├── js/                     # JS (búsqueda, TOC, zoom, PDF viewer)
│   ├── images/                 # Assets gráficos
│   ├── pdf/                    # PDFs de referencia
│   └── jstopics/               # Índices de búsqueda
├── assets/                     # Assets adicionales
├── frontend/                   # Frontend build tools
├── imagenes del sistema/       # Imágenes del sistema
├── manuales/                   # Manuales PDF
├── traducciones/               # Traducciones
├── Didacta.ico                 # Icono personalizado
├── Didacta.iss                 # Script Inno Setup
└── README.md
```

---

## Comandos disponibles

```bash
# Ejecutar
python Didacta/app.py

# Con el instalador
Didacta_Setup.exe
```

---

## Problemas conocidos

| Issue | Estado |
|-------|--------|
| WebView2 requiere Edge instalado | Windows 10/11 incluido |
| pywebview icon kwarg no soportado | Workaround ctypes |
| TOC profundo (>3 niveles) | Limitación HTML Help |

---

## Licencia

Uso interno — CDT Santa Bárbara, Fuerzas Armadas de Honduras (UDH).

---

## Autores

**DolfoZ — Oacoello — Ares — Sistema de Artillería CDT Santa Bárbara**