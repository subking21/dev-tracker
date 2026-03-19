from django import forms
from .models import Milestone, Problem

class ProblemForm(forms.ModelForm):
    class Meta:
        model = Problem
        fields = ['title', 'source', 'difficulty', 'notes', 'date_solved']

class MilestoneForm(forms.ModelForm):
    class Meta:
        model = Milestone
        fields = ['topic', 'description', 'date_achieved']