from django.apps import AppConfig


class BaseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'base'

    #When app has been fully loaded, Starting the background email sending service.
    def ready(self):
        from jobs import mailschedulingjob
        mailschedulingjob.start()


