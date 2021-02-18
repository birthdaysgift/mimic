from os import path
from os.path import abspath, dirname

AUTH_USER_MODEL = "auth_custom.User"

# absolute path to the project directory
BASE_DIR = dirname(dirname(dirname(abspath(__file__))))

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.staticfiles',

    'auth_custom.apps.AuthConfig',
    'common.apps.CommonConfig',
    'friends.apps.FriendsConfig',
    'pages.apps.PagesConfig',
    'photos.apps.PhotosConfig',
    'posts.apps.PostsConfig',
    'search.apps.SearchConfig',
    'talks.apps.TalksConfig',
    'videos.apps.VideosConfig',
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

ROOT_URLCONF = 'mimic.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'libraries': {
            }
        },
    },
]

WSGI_APPLICATION = 'mimic.wsgi.application'

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_ROOT = path.join(BASE_DIR, "static")
STATIC_URL = "/static/"

MEDIA_ROOT = path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"