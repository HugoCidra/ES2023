from django.contrib import admin
from .models import all_classes

# The purpose of this block is to automatically register all model classes
# for the admin site. Once registered, these models will be accessible
# and manageable via Django's admin interface.

# Loop through each model class in all_classes.
for i in all_classes:
    # Register the model class with the admin site.
    admin.site.register(i)
