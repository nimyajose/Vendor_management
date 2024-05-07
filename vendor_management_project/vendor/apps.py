from django.apps import AppConfig

class VendorsConfig(AppConfig):
    name = 'vendor'

    def ready(self):
        import vendor.signals
