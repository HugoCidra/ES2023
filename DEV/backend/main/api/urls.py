from django.urls import path, include
from .views import *

from . import REQ1 as req1

# Define the URL patterns for this application/module.
urlpatterns = [
    # Routes for REQ1
    # Route to handle user registration using the register function from the 'req1' module.
    path("register/", req1.register),
    # Route to handle user login using the login function from the 'req1' module.    
    path("login/", req1.login),

    # Below are routes for other requirements, each having its own set of URLs.
    # Instead of defining all URLs here, we are including them from their respective modules.

    # Include the URL patterns defined in the respective modules.
    path("REQ2/", include("api.REQ2.urls")),
    path("REQ3/", include("api.REQ3.urls")),
    path("REQ4/", include("api.REQ4.urls")),
    path("REQ5/", include("api.REQ5.urls")),
    path("REQ6/", include("api.REQ6.urls")),
    path("REQ7/", include("api.REQ7.urls")),
    path("REQ8/", include("api.REQ8.urls")),
]
