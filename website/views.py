from django.shortcuts import render # Import render to render templates
from .models import Problem, Milestone  # Import models if needed in views
from django.contrib.auth.decorators import login_required # Import login_required decorator

# Create your views here.

def home(request): # Home page view 
    return render(request, 'index.html') # Render the 'index.html' template

@login_required # Require login to access the dashboard
def dashboard(request): # Dashboard page view 
    all_problems = Problem.objects.all()  # this is just an SQL query to get all Problem objects from the database
    return render(request, 'account/dashboard.html', {'Problems Solved': all_problems}) # Pass the problems to the template context

def login(request): # Login page view 
    return render(request, 'login.html')

def milestones(request): # Milestones page view 
    return render(request, 'milestones.html')

def track(request): # Track page view 
    return render(request, 'track.html')