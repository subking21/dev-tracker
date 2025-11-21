from django.shortcuts import render # Import render to render templates

# Create your views here.

def home(request): # Home page view 
    return render(request, 'index.html') # Render the 'index.html' template

def dashboard(request): # Dashboard page view 
    return render(request, 'dashboard.html')

def login(request): # Login page view 
    return render(request, 'login.html')

def milestones(request): # Milestones page view 
    return render(request, 'milestones.html')

def track(request): # Track page view 
    return render(request, 'track.html')