from .base import *
DEBUG=False
ADMINS=(
    ('anton', 'zeratul314@gmail.com')
)
ALLOWED_HOSTS=['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
ALLOWED_HOSTS = ['eduaproject.com', 'www.eduaproject.com']