from django.contrib import admin

# Register your models here.

from .models import Problem, Milestone

admin.site.register(Problem) # Register the Problems model with the admin site
admin.site.register(Milestone) # Register the Milestone model with the admin site›