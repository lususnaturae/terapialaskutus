from django.apps import AppConfig

class UsersConfig(AppConfig):
    name = 'therapyinvoicing.users'
    verbose_name = 'Users Application'

    def ready(self):
        import therapyinvoicing.users.signals
