from django.apps import AppConfig

class StoriesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.stories'

    def ready(self):
        from . import translation
