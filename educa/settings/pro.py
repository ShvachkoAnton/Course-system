from .base import *
DEBUG=False
ADMINS=(
    ('anton', 'zeratul314@gmail.com')
)
ALLOWED_HOSTS=['*']

DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.postgresql',
       'NAME': 'postgres',
       'USER': 'educa',
       'PASSWORD': 'antosha16',
   }
}