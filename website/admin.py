from django.contrib import admin

# Register your models here.

from .models import Problem, Milestone

admin.site.register(Problem) # Register the Problems and Milestone model with the admin site
admin.site.register(Milestone) # This allows admin users to manage these models through the Django admin interface