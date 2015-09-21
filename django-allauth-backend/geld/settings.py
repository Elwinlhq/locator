# Django settings for geld project.
DEBUG = True
TEMPLATE_DEBUG = DEBUG
ADMINS = ('juanseph@gmail.com')
MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE'   : 'django.db.backends.mysql', 
        'NAME'     : 'geld',                      
        'USER'     : 'root',
        'PASSWORD' : '',
        'HOST'     : '',                      
        'PORT'     : '',                      
    }
}

ALLOWED_HOSTS = []
TIME_ZONE = 'America/Chicago'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = True
USE_L10N = True
USE_TZ = True
MEDIA_ROOT = ''
MEDIA_URL = ''
STATIC_ROOT = ''
STATIC_URL = '/static/'
STATICFILES_DIRS = ()

# List of finder classes that know how to find static files in various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'w$ghg@e$mh64yil=u_-7n0)dchoi+ha5pg6k-xo303$biq9!ul'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.core.context_processors.request",
    "allauth.account.context_processors.account",
    "allauth.socialaccount.context_processors.socialaccount",
    # Admin
    'django.contrib.auth.context_processors.auth'
)

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",

    # `allauth` specific authentication methods, such as login by e-mail
    "allauth.account.auth_backends.AuthenticationBackend",
)


MIDDLEWARE_CLASSES = (    
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',        
)

ROOT_URLCONF = 'geld.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'geld.wsgi.application'

TEMPLATE_DIRS = (
    '/media/psf/Home/git/geld/templates'
)

EMAIL_HOST = 'localhost'
EMAIL_PORT = 25      

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',
    
    'rest_framework',
    
    # My own app
    'geld'
)

# Rest framework config ------------------------------
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
    ),
    'PAGINATE_BY': 5
}

# Log config ------------------------------
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,

    'formatters': {
        'geld': {
            'format': '[%(asctime)s] %(levelname)s  %(module)s: %(message)s'
        },
    }, 
    
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter' : 'geld'
        },
        
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': '/var/log/django/db.log',
        },
    },
        
    'loggers': {
        'django.db.backends': {
            'handlers': ['file'],
            'level': 'DEBUG',
        },
        
        'geld': {
            'handlers': ['console'],
            'level': 'DEBUG'
        },
        
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True
        },
    }
}


# Allauth config ------------------------------
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_EMAIL_REQUIRED = True
LOGIN_REDIRECT_URLNAME = "/"

SOCIALACCOUNT_EMAIL_VERIFICATION = "none"
SOCIALACCOUNT_EMAIL_REQUIRED = False
SOCIALACCOUNT_QUERY_EMAIL = False
