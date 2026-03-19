from django.shortcuts import render # Import render to render templates
from .models import Problem, Milestone  # Import models if needed in views
from django.contrib.auth.decorators import login_required # Import login_required decorator
from django.contrib.auth.forms import UserCreationForm # Import UserCreationForm for signup functionality
from django.shortcuts import redirect # Import redirect to redirect users after login
from django.contrib.auth.decorators import login_required # Import login_required decorator to restrict access to certain views
from .forms import MilestoneForm, ProblemForm # Import forms for handling problem and milestone submissions

# Create your views here.

def home(request): # Home page view 
    return render(request, 'index.html') # Render the 'index.html' template

# query the database for all problems solved by the user and pass that to the dashboard template
# djangos ORM lets you chain .filer() and .count() to get the count of problems by difficulty
@login_required
def dashboard(request):
    all_problems = Problem.objects.filter(user=request.user)
    easy_count = all_problems.filter(difficulty='easy').count()
    medium_count = all_problems.filter(difficulty='medium').count()
    hard_count = all_problems.filter(difficulty='hard').count()
    total = all_problems.count()
    return render(request, 'account/dashboard.html', {
        'problems': all_problems,
        'easy_count': easy_count,
        'medium_count': medium_count,
        'hard_count': hard_count,
        'total': total,
    })

def login(request): # Login page view 
    return render(request, 'login.html')

@login_required
def milestones(request): # Milestones page view 
    if request.method == 'POST':
        form = MilestoneForm(request.POST)
        if form.is_valid():
            milestone = form.save(commit=False)
            milestone.user = request.user
            milestone.save()
            return redirect('website:milestones')
    else:
        form = MilestoneForm()
    user_milestones = Milestone.objects.filter(user=request.user).order_by('-date_achieved')
    return render(request, 'milestones.html', {'form': form, 'milestones': user_milestones})

@login_required
def track(request):
    if request.method == 'POST':
        form = ProblemForm(request.POST)
        if form.is_valid():
            problem = form.save(commit=False)
            problem.user = request.user
            problem.save()
            return redirect('website:dashboard')
    else:
        form = ProblemForm()
    return render(request, 'track.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('website:login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})