# Generador de lista de nombre de archivos de una carpeta  
**Desarrollador:** Nuevas Tecnologías División TI

---

## 📋 Descripción

Este script permite al usuario generar un archivo Excel con la lista de archivos de una carpeta seleccionada. Se desarrolló como apoyo a los procesos del área de CAD.  
La versión actual incluye procesamiento adicional de los nombres para facilitar la clasificación y normalización.

---

## 🚀 Requisitos

- Python 3.6 o superior  
- pandas  
- openpyxl  
- (Opcional) pyinstaller para generar ejecutable `.exe`

---

## 🔧 Instalación

Clona este repositorio:

```bash
git clone https://github.com/tu-usuario/tu-repo.git
cd tu-repo
Instala las dependencias:

bash
Copiar
Editar
pip install --upgrade pip
pip install pandas openpyxl
▶️ Uso rápido
Ejecuta el script:

bash
Copiar
Editar
python nombre_archivos.py
En la ventana que aparece:

Haz clic en "Seleccionar carpeta" y elige la carpeta deseada.

El script generará un archivo file_list_YYYYMMDD_HHMMSS.xlsx dentro de esa misma carpeta.

Al finalizar, pulsa "Abrir Excel" para visualizar el archivo generado.

📑 ¿Qué incluye el Excel generado?
El archivo contiene las siguientes columnas:

Columna	Descripción
Name	Nombre original del archivo (con extensión).
Name_without_extension	Nombre sin la extensión .pdf o .PDF.
Name_without_any_character	Nombre sin caracteres extra ni espacios. Se conserva solo el prefijo + número juntos, ej: CPFAB+33643.

🖥️ Crear un ejecutable (.exe)
Para distribuir la aplicación sin requerir Python instalado:

Instala PyInstaller:

bash
Copiar
Editar
pip install pyinstaller
Ejecuta el siguiente comando, asegurándote de que icono.ico esté en la misma carpeta del script:

bash
Copiar
Editar
pyinstaller --onefile --noconsole --icon="icono.ico" nombre_archivos.py
El archivo ejecutable nombre_archivos.exe se generará en la carpeta dist/.

🛠 Contacto
Para soporte o mejoras, contactar con el equipo de Nuevas Tecnologías División TI.
