from django.contrib import admin # Admin site URL
from django.urls import path # Import path for defining URL patterns
from . import views # Import views from the current package
from django.contrib.auth import views as auth_views # Import Django's built-in authentication views

app_name = 'website' # Set the application namespace

# Define the URL patterns for the 'website' app
urlpatterns = [
    path('', views.home, name='homepage'),
    path('/account/dashboard', views.dashboard, name='dashboard'), # the string 'dashboard' is the default URL after the BASE URL so it will be localhost:8000/dashboard to access this view
    path('milestones', views.milestones, name='milestones'),
    path('track', views.track, name='track'),

    path('registration/login/', auth_views.LoginView.as_view(template_name='website/registration/login.html'), name='login'), # Use the built in login view with a custom template
    path('registration/logout/', auth_views.LogoutView.as_view(template_name='website/registration/logout.html'), name='logout'), # Use the built in logout view with a custom template
]