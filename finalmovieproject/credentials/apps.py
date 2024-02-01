from django.apps import AppConfig


class CredentialsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'credentials'

    def ready(self):
        import credentials.signals