"""
Configuración de Django para el proyecto ElectroTech.
Plataforma de gestión de inventario para almacén de componentes de hardware.

Para más información:
https://docs.djangoproject.com/en/6.0/topics/settings/
"""

from pathlib import Path
import os

# ============================================================
# RUTAS BASE
# ============================================================
BASE_DIR = Path(__file__).resolve().parent.parent


# ============================================================
# SEGURIDAD
# ============================================================
SECRET_KEY = 'django-insecure-u+loc)n7(2w5u$fhz6y008r(&g$xxc2t0zl8xd10f#=i1b@un-'
DEBUG = True
ALLOWED_HOSTS = ['*']


# ============================================================
# APLICACIONES INSTALADAS
# ============================================================
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Apps propias de ElectroTech
    'accounts.apps.AccountsConfig',      # Gestión de usuarios, autenticación y roles
    'inventory.apps.InventoryConfig',    # Categorías y componentes del inventario
    'movements.apps.MovementsConfig',    # Ingresos, egresos, planillas y movimientos
    'metrics.apps.MetricsConfig',        # Dashboard, métricas, gráficas e historial
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'electrotech.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Templates globales
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # Context processor personalizado para datos globales del menú
                'electrotech.context_processors.datos_globales',
            ],
        },
    },
]

WSGI_APPLICATION = 'electrotech.wsgi.application'


# ============================================================
# BASE DE DATOS (SQLite para entorno universitario)
# ============================================================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# ============================================================
# MODELO DE USUARIO PERSONALIZADO
# ============================================================
AUTH_USER_MODEL = 'accounts.Usuario'


# ============================================================
# VALIDACIÓN DE CONTRASEÑAS
# ============================================================
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# ============================================================
# INTERNACIONALIZACIÓN (Español latinoamericano)
# ============================================================
LANGUAGE_CODE = 'es'
TIME_ZONE = 'America/Caracas'
USE_I18N = True
USE_TZ = True


# ============================================================
# ARCHIVOS ESTÁTICOS (CSS, JavaScript, Imágenes)
# ============================================================
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]
STATIC_ROOT = BASE_DIR / 'staticfiles'


# ============================================================
# ARCHIVOS MULTIMEDIA (Imágenes de componentes)
# ============================================================
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


# ============================================================
# AUTENTICACIÓN
# ============================================================
LOGIN_URL = '/cuentas/login/'           # Redirige aquí si no está autenticado
LOGIN_REDIRECT_URL = '/dashboard/'       # Redirige aquí después de iniciar sesión
LOGOUT_REDIRECT_URL = '/cuentas/login/'  # Redirige aquí después de cerrar sesión


# ============================================================
# CONFIGURACIÓN POR DEFECTO PARA CAMPOS AUTOMÁTICOS
# ============================================================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# ============================================================
# CONFIGURACIÓN DE MENSAJES (usando Bootstrap/Tailwind classes)
# ============================================================
from django.contrib.messages import constants as messages
MESSAGE_TAGS = {
    messages.DEBUG: 'bg-gray-100 text-gray-800 border-gray-300',
    messages.INFO: 'bg-blue-100 text-blue-800 border-blue-300',
    messages.SUCCESS: 'bg-green-100 text-green-800 border-green-300',
    messages.WARNING: 'bg-yellow-100 text-yellow-800 border-yellow-300',
    messages.ERROR: 'bg-red-100 text-red-800 border-red-300',
}
