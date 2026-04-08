from django.apps import AppConfig

# class CarsConfig herda da clss AppConfig(class criada por algum programador)
class CarsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cars'
