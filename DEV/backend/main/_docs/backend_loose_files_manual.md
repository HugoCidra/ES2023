# Loose File Manual

## Ficheiros soltos \DEV\backend\main\main

---

###     \_\_init\_\_.py
####     **EMPTY FILE**

---

###     asgi.py
It exposes the ASGI callable as a module-level variable named ``application``.

---

###     settings.py
The code is the settings for the project:

- Essential configurations like the SECRET_KEY, debug mode, and allowed hosts are defined.

- Installed apps, including Django's built-ins and extras like rest_framework, are listed.

- Middleware, including security and CORS settings, is configured.

- SQLite is set as the default database with its location defined.

- Settings for templates, internationalization, static files, and password validation are provided.



---

###     urls.py
- A list of URL patterns, urlpatterns, is defined for routing.

- The Django admin interface is accessible via the "admin/" route.

- All "api/" prefixed routes are delegated to the api.urls module.

---

###     wsgi.py
It exposes the WSGI callable as a module-level variable named ``application``.

---


## Ficheiros soltos \DEV\backend\main\api

---

###     \_\_init\_\_.py
####    Estado: **VAZIO**

---

###     admin.py
The purpose of this block is to automatically register all model classes for the admin site. Once registered, these models will be accessible and manageable via Django's admin interface.

---

###     apps.py
- Creating a custom configuration class for the 'api' app, which inherits from AppConfig

- Specifying the default auto field for model primary keys as BigAutoField

- Setting the name of the app as "api"
---

###     models.py
- The code defines database table structures using Django's Object-Relational Mapping (ORM) system.

- The User model represents a user with attributes like name, password, email, and role.

- Question, Option, Test, SolvedTest, Vote, and Tag models define various aspects of a question-answer system, with relationships like ForeignKeys and ManyToManyFields.

- The inner Meta class in some models enforces unique constraints for combinations of fields.

- all_classes is a list containing all the model classes, potentially for batch operations or registry.

---

###     tests.py
####    Estado: **VAZIO**

---

###     urls.py
- Essential Django URL utilities and all view functions from the current module are imported.

- The module REQ1 is imported under the alias 'req1'.

- URL patterns, urlpatterns, are defined for the app/module.

- Two specific routes for registration and login are set using functions from 'req1'.

- Subsequent routes delegate to other modules, including their respective URL patterns.

---

###     views.py
####    Estado: **VAZIO**
