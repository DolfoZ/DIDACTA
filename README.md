# DIDACTA

**Sistema de Ayuda y Documentación Técnica** para el **CDT Santa Bárbara** — Sistema de Artillería.

Aplicación de ayuda basada en **HTML Help Workshop (Microsoft HTML Help / .chm compatible)** con navegador web embebido, sistema de búsqueda, índice temático y visualizador de PDFs integrado.

---

## 🎯 Características principales

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

## 📦 Contenido incluido

| Categoría | Cantidad | Descripción |
|-----------|----------|-------------|
| **Temas HTML** | 300+ | Cartuchos, proyectiles, cargas, manuales |
| **Cartuchos 105mm** | 100+ | HE, HEAT, APERS, ILLUM, SMOKE, TP, etc. |
| **Proyectiles 155mm** | 80+ | HE, HEAT, HERA, ICM, ILLUM, SMOKE, etc. |
| **Cargas propulsoras** | 30+ | M1, M3A1, M4A2, M119A2, M203, M203A1, etc. |
| **Proyectiles 105mm** | 60+ | M1, M323, M324, M326, M392A1, M393A1/2, M444, M456, M483A1, M485, M549A1, M548, M67, M692, M718, M724, M724A1, M731, M741, M795, M804, M712, M718, M741, M718, M760, M795, M804, M825, M864, M898, M913, M915, M919, M927, M982 |
| **Proyectiles 155mm** | 80+ | M101, M102, M107, M110, M112, M116, M121, M121A1, M121A2, M121A3, M121A4, M121A5, M121A6, M121A7, M121A8, M121A9, M121A10, M121A11, M121A12, M121A13, M121A14, M121A15, M121A16, M121A17, M121A18, M121A19, M121A20, M121A21, M121A21, M121A22, M121A23, M121A24, M121A25, M121A26, M121A27, M121A28, M121A29, M121A30, M121A31, M121A32, M121A33, M121A34, M121A35, M121A36, M121A37, M121A38, M121A39, M121A40 |
| **Cargas 155mm** | 20+ | M1, M2, M3, M3A1, M3A2, M4, M4A1, M4A2, M119, M119A1, M119A2, M203, M203A1, M231, M232, M232A1 |

---

## 🔐 Autenticación (sb-acceso)

**Integración obligatoria con Token Passing** — la app solo funciona si se lanza desde `sb-acceso`:

```bash
# Desde sb-acceso
Didacta.exe --sessionToken=<token> --deviceId=<id> --applicationCode=didacta

# Testing sin servidor (demo mode)
Didacta.exe --demo
```

**Flujo de autenticación:**
```
sb-acceso → Didacta.exe --sessionToken=X --deviceId=Y --applicationCode=didacta
    → auth_guard.validate() → POST http://localhost:3001/auth/validate
      → OK: app maximizada "DIDACTA" + user bar + TOC + búsqueda
      → FAIL: blocked screen maximizada "DIDACTA" + icono
      → --demo: bypass para testing
```

---

## 🖥️ Interfaz de Usuario

| Área | Descripción |
|------|-------------|
| **Barra superior** | Título "DIDACTA", logo CDT, botones minimizar/maximizar/cerrar |
| **Panel izquierdo (TOC)** | Índice temático jerárquico (3 niveles), búsqueda en vivo |
| **Panel central** | Contenido HTML renderizado (WebView2) |
| **Panel derecho** | Índice alfabético / búsqueda full-text |
| **Barra inferior** | Zoom, imprimir, página anterior/siguiente, favoritos |

---

## 🔧 Instalación

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

# Ejecutar (modo demo)
Didacta.exe --demo

# Con auth (desde sb-acceso)
Didacta.exe --sessionToken=X --deviceId=Y --applicationCode=didacta
```

---

## 🏗️ Build & Distribución

### Instalador Inno Setup
```bash
ISCC.exe Didacta.iss
```
- Output: `Didacta_Setup.exe` (~500 MB)
- Instala en `C:\Program Files\DIDACTA\`
- Icono **Didacta.ico** en setup, app, uninstaller, shortcut

**Archivos de build:**
| Archivo | Descripción |
|---------|-------------|
| `Didacta.iss` | Script Inno Setup (icono Didacta.ico en todo) |
| `Didacta.ico` | Icono personalizado (app, taskbar, installer, uninstaller) |

---

## 📁 Estructura del proyecto

```
DIDACTA/
├── Didacta.iss              # Script Inno Setup
├── Didacta.ico              # Icono personalizado
├── auth_guard.py            # Auth guard (token passing + demo mode)
├── DidactaSetup.exe         # Instalador compilado
├── html/                    # Contenido principal (HTML/JS/CSS)
│   ├── *.html               # 300+ temas HTML
│   ├── css/                 # Estilos (tema oscuro táctico)
│   ├── js/                  # JS (búsqueda, TOC, zoom, PDF viewer)
│   ├── images/              # Assets gráficos
│   ├── css/                 # Estilos
│   └── *.htm/*.html         # Temas HTML (cartuchos, proyectiles, cargas)
├── images/                  # Assets gráficos
├── images/                  # Assets gráficos
├── pdf/                     # PDFs de referencia
├── manuales/                # Manuales PDF
├── pdf/                     # PDFs de cartuchos/proyectiles
├── images/                  # Assets gráficos
├── favicon.ico              # Favicon
├── settings.js              # Configuración runtime
├── zoom_*.js                # Control de zoom
├── zoom_*.htm               # Páginas de zoom
└── *.html                   # Temas raíz (biblioteca.html, carousel.html, etc.)
```

---

## 🚀 Comandos disponibles

```bash
# App (default)
Didacta.exe                          # Con auth check

# Demo mode (testing sin servidor)
Didacta.exe --demo

# Con auth (desde sb-acceso)
Didacta.exe --sessionToken=X --deviceId=Y --applicationCode=didacta
```

---

## 📦 Instalador oficial

**Descargar desde Releases:**
```
Didacta_Setup.exe
```
- Instala en `C:\Program Files\DIDACTA\`
- Incluye 2000+ archivos HTML/JS/CSS/PDF
- Accesos directos: Menú Inicio + Escritorio
- Icono **Didacta.ico** en app, taskbar, installer, uninstaller
- Desinstalador incluido

**Instalador disponible en:**
```
C:\Users\DolfoZR\Downloads\CDT\INSTALADORES\Didacta_Installer\
Didacta_Setup.exe + Didacta_Setup-1.bin a Didacta_Setup-5.bin
```

---

## 🔐 Autenticación — Detalles técnicos

### auth_guard.py
```python
# Validación contra servidor central
payload = {
    "sessionToken": token,
    "deviceId": device,
    "application": "didacta",
    "requiredPermissions": ["canUseDidacta", "canUseSearch", "canUsePDFViewer"]
}
# POST http://localhost:3001/auth/validate
# Response: { valid: true, profile: { nombre, rango, foto }, sessionId }
```

### Demo mode
```bash
Didacta.exe --demo
# Bypass auth, usuario "MODO DEMO / TEST"
```

---

## 📦 Instalador oficial

**Ubicación del instalador:**
```
C:\Users\DolfoZR\Downloads\CDT\INSTALADORES\Didacta_Installer\
Didacta_Setup.exe + Didacta_Setup-1.bin a Didacta_Setup-5.bin
```

---

## 📋 Problemas conocidos

| Issue | Estado |
|-------|--------|
| WebView2 requiere Edge instalado | ✅ Windows 10/11 incluido |
| pywebview icon kwarg no soportado | ✅ Workaround ctypes |
| TOC profundo (>3 niveles) | ⚠️ Limitación HTML Help |

---

## 📄 Licencia

Uso interno — CDT Santa Bárbara, Fuerzas Armadas de Honduras (UDH).

---

## 👤 Autores

**👤 Autores**  
**DolfoZ — Oacoello — Ares — Sistema de Artillería CDT Santa Bárbara**