from django.apps import AppConfig

# Creating a custom configuration class for the 'api' app, which inherits from AppConfig
class ApiConfig(AppConfig):

    # Specifying the default auto field for model primary keys as BigAutoField
    default_auto_field = "django.db.models.BigAutoField"

    # Setting the name of the app as "api"
    name = "api"
