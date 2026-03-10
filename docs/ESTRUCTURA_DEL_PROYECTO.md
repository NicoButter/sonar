# Estructura de Proyecto Sonar - Estándar Django

Este documento describe la nueva estructura del proyecto Sonar después de la refactorización para seguir el estándar recomendado de Django.

## Estructura General

```
sonar/
├── apps/                    # Directorio para todas las aplicaciones Django
│   ├── accounts/           # App de autenticación y gestión de usuarios
│   ├── bandas/             # App de gestión de bandas
│   ├── dashboards/         # App de paneles de control (dashboards)
│   └── __init__.py
│
├── config/                 # Configuración del proyecto
│   ├── settings.py         # Configuración de Django
│   ├── urls.py             # URLs principales del proyecto
│   ├── asgi.py             # Configuración ASGI (producción)
│   ├── wsgi.py             # Configuración WSGI (producción)
│   └── __init__.py
│
├── docs/                   # Documentación del proyecto
│
├── static/                 # Archivos estáticos (CSS, JS, imágenes)
│   ├── css/
│   ├── js/
│   └── images/
│
├── templates/              # Templates globales del proyecto
│   └── base.html
│
├── media/                  # Archivos subidos por usuarios
│   ├── bandas/
│   └── gusto-amplificado/
│
├── manage.py              # Script de gestión de Django
├── requirements.txt       # Dependencias del proyecto
├── README.md             # Documentación principal
├── LICENSE               # Licencia del proyecto
└── db.sqlite3            # Base de datos (desarrollo)
```

## Cambios Principales

### 1. **Directorio `config/` (antes `sonar/`)**
   - Contiene toda la configuración centralizada del proyecto
   - `settings.py`: Configuración de Django con INSTALLED_APPS actualizado
   - `urls.py`: Rutas principales que incluyen apps desde `apps.*`
   - `asgi.py`, `wsgi.py`: Configuración para servidores de producción

### 2. **Directorio `apps/`**
   - Agrupa todas las aplicaciones del proyecto
   - Cada app está en su propio subdirectorio
   - Las apps se referencian como `apps.accounts`, `apps.bandas`, `apps.dashboards`

### 3. **Directorio `docs/`**
   - Destinado para documentación del proyecto
   - Puede incluir archivos README específicos, arquitectura, etc.

## Cambios en Configuración

### INSTALLED_APPS (config/settings.py)
```python
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "apps.accounts",      # Actualizado
    "apps.bandas",         # Actualizado  
    "apps.dashboards"      # Actualizado
]
```

### ROOT_URLCONF (config/settings.py)
```python
ROOT_URLCONF = "config.urls"  # Antes: "sonar.urls"
```

### DJANGO_SETTINGS_MODULE (manage.py, asgi.py, wsgi.py)
```python
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")  # Antes: "sonar.settings"
```

### URLs (config/urls.py)
```python
urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('apps.accounts.urls')),
    path('dashboard/', include('apps.dashboards.urls')),
    path('bandas/', include('apps.bandas.urls')),
]
```

## Cambios en Imports

Todos los imports dentro de las aplicaciones fueron actualizados:

**Antes:**
```python
from accounts.models import Usuario
from bandas.models import Banda
```

**Después:**
```python
from apps.accounts.models import Usuario
from apps.bandas.models import Banda
```

## Migraciones

Las migraciones fueron actualizadas para reflejar la nueva estructura:
- Referencias en archivos de migración: `bandas.models` → `apps.bandas.models`
- Referencias en campos ForeignKey: `to="bandas.banda"` → `to="apps.bandas.banda"`

## Ventajas de Esta Estructura

✅ **Escalabilidad**: Fácil agregar nuevas aplicaciones  
✅ **Claridad**: Separación clara entre configuración, lógica y activos  
✅ **Mantenimiento**: Estructura estándar de Django que cualquier desarrollador reconoce  
✅ **Organización**: Cada aplicación está auto-contenida en su directorio  
✅ **Colaboración**: Sigue las mejores prácticas de Django  

## Comandos Útiles

```bash
# Verificar que todo está bien configurado
python manage.py check

# Ver el plan de migraciones
python manage.py migrate --plan

# Ejecutar migraciones
python manage.py migrate

# Crear superusuario
python manage.py createsuperuser

# Ejecutar servidor de desarrollo
python manage.py runserver
```

## Notas Importantes

- El archivo `db.sqlite3` se mantiene en la raíz del proyecto
- Los archivos media se sirven desde `/media/`
- Los archivos estáticos se sirven desde `/static/`
- Las templates globales están en `/templates/`
- Cada app tiene sus propias templates en `apps/{app_name}/templates/{app_name}/`
