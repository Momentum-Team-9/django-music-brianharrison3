from django.apps import AppConfig
from .models import Album

class AlbumsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'albums'
