from todoApi.settings.base import * 
# SECURITY WARNING: don't run with  ebug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME':'todo_app',
        'USER':'app',
        'PASSWORD':'admin123',
        'HOST':'db',
        'PORT':5432
    }
}


