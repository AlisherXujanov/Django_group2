from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    # We have to import the signals here so that they are registered 
    def ready(self):
        import users.signals
