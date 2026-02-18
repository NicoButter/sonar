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

1. **Cloná el repositorio:**

```bash
git clone https://github.com/nicobutter/sonar.git
cd sonar
```

2. **Activá tu entorno virtual (recomendado):**

```bash
python3 -m venv venv
source venv/bin/activate  # En Linux/Mac
# o
venv\Scripts\activate     # En Windows
```

3. **Instalá las dependencias:**

```bash
pip install -r requirements.txt
```

4. **Configurá las variables de entorno:**

Copia el archivo de ejemplo y configúralo:

```bash
cp .env.example .env
```

Edita `.env` con tus configuraciones locales. Para desarrollo, puedes usar los valores por defecto.

**Variables importantes:**
- `SECRET_KEY`: Cambia esto en producción
- `DEBUG`: `True` para desarrollo, `False` para producción
- `DATABASE_*`: Configuración de base de datos (SQLite por defecto)

5. **Ejecutá las migraciones:**

```bash
python manage.py makemigrations
python manage.py migrate
```

6. **Creá un superusuario (opcional):**

```bash
python manage.py createsuperuser
```

7. **¡Y a sonar!**

```bash
python manage.py runserver
```

Visita `http://127.0.0.1:8000` en tu navegador.

## 🔧 Configuración de producción

Para producción, asegúrate de:

- Cambiar `DEBUG=False`
- Configurar `SECRET_KEY` segura
- Usar PostgreSQL en lugar de SQLite
- Configurar email real
- Establecer `ALLOWED_HOSTS` apropiadamente

🤘 Contribuciones
¡Toda colaboración es bienvenida! Ya sea codificando, diseñando o compartiendo la app con bandas amigas. Mandá tu PR o escribime por cualquier idea que tengas.

📬 Contacto
Si querés sumarte, tenés ideas locas o teorías conspirativas sobre por qué los demos tienen que ser 4 y no 5, escribime a:

📧 nicobutter@gmail.com

Sonar es un proyecto hecho con pasión por la música, el software libre y el sur del mundo.

