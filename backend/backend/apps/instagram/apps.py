from django.apps import AppConfig


class InstagramConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'instagram'
    
    # def ready(self):
    #     from sheduler import scheduler
    #     scheduler.start()
