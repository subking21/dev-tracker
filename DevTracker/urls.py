"""
URL configuration for DevTracker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin # Admin site URL§
from django.urls import path, include # Import include to reference other URLconfs

# Define the URL patterns for the project
# Dont forget to go to the seetings.py and register the app

urlpatterns = [
    path('admin/', admin.site.urls), # Admin site URL
    path('', include('website.urls', namespace='website')), # here i removed 'website/' to make the BASE URL lead to the 'website' app like home page
    path('accounts/', include('django.contrib.auth.urls')), # Include Django's built-in authentication URLs
]
