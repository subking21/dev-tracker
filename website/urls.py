from django.contrib import admin # Admin site URL
from django.urls import path # Import path for defining URL patterns
from . import views # Import views from the current package

app_name = 'website' # Set the application namespace

# Define the URL patterns for the 'website' app
urlpatterns = [
    path('', views.home, name='homepage'),
    path('dashboard', views.dashboard, name='dashboard'), # the string 'dashboard' is the default URL after the BASE URL so it will be localhost:8000/dashboard to access this view
    path('login', views.login, name='login'),
    path('milestones', views.milestones, name='milestones'),
    path('track', views.track, name='track'),
]