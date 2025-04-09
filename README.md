# 🎵 Sonar

**Sonar** es una plataforma web desarrollada con Django + PostgreSQL, creada para **fomentar la escena musical en Río Gallegos** y conectar bandas emergentes con su comunidad. Pensada para ser simple, funcional y con amor al under, esta aplicación permite a las bandas registrarse, subir sus demos y compartir sus fotos.

## 🚀 Objetivos

- Dar visibilidad a bandas locales de Río Gallegos y alrededores.
- Permitir la creación de un perfil de banda con:
  - Hasta **4 demos de audio**.
  - Una **galería de imágenes**.
  - Información de contacto y descripción de estilo.
- Facilitar la conexión entre músicos, organizadores de eventos y oyentes.

## 🛠️ Tecnologías utilizadas

- 💻 **Backend**: Django (Python)
- 🐘 **Base de Datos**: PostgreSQL
- 🎨 **Frontend**: HTML5, CSS3 (con amor propio, sin Bootstrap ni nada raro)
- 🐧 **Sistema Operativo**: openSUSE (sí, ¡aguante el pingüino verde!)

## 📸 Funcionalidades principales

- Registro y login de bandas.
- Panel para editar perfil y subir demos (.mp3/.wav).
- Subida de imágenes (portadas, fotos de recitales, etc.).
- Visualización de bandas registradas.
- Búsqueda por género, nombre o ciudad.

## ⚙️ Instalación local (modo desarrollador)

1. Cloná el repositorio:

```bash
git clone https://github.com/tu_usuario/sonar.git
cd sonar
```

Activá tu entorno virtual (recomendado):

```bash
python3 -m venv venv
source venv/bin/activate
```

Instalá las dependencias:

```bash
pip install -r requirements.txt
```

Configurá PostgreSQL y las variables de entorno (.env o settings.py modificado).

Ejecutá migraciones:

```bash
python manage.py migrate
```

¡Y a sonar!

```bash
python manage.py runserver
```

🤘 Contribuciones
¡Toda colaboración es bienvenida! Ya sea codificando, diseñando o compartiendo la app con bandas amigas. Mandá tu PR o escribime por cualquier idea que tengas.

📬 Contacto
Si querés sumarte, tenés ideas locas o teorías conspirativas sobre por qué los demos tienen que ser 4 y no 5, escribime a:

📧 nicobutter@gmail.com

Sonar es un proyecto hecho con pasión por la música, el software libre y el sur del mundo.

