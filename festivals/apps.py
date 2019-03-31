from django.apps import AppConfig


class FestivalsConfig(AppConfig):
    name = 'festivals'

    def ready(self):
        import festivals.services.signals