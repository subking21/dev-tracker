from django.db import models
from django.contrib.auth.models import User # django's built-in user model
from django.utils import timezone

# Create your models here.
# making a database model for tracking development tasks
# Django already has a built in database model for users, so we will use that

# Tracks a problem you solved (Algomap or Leetcode etc)

class Problem(models.Model): # model to represent a coding problem solved by the user. *** It always uses a class that inherits from models.Model ***
    user = models.ForeignKey(User, on_delete=models.CASCADE) # link each problem to a user
    title = models.CharField(max_length=200) # title of the problem
    source = models.CharField(max_length=50 , choices = [
        ('leetcode', 'LeetCode'),
        ('algomap', 'AlgoMap'),
        ('custom', 'Custom'),
    ]) # source of the problem
    difficulty = models.CharField(max_length=10 , choices = [
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
    ])
    notes = models.TextField(blank=True) # additional notes
    date_solved = models.DateField(default=timezone.now) # date when the problem was solved

    class Meta:
        ordering = ['date_solved'] # order by what was solved first

    def __str__(self): # This code defines the string representation of the Problems model
        return self.title # when we print an instance of Problems, it will return the title of the problem
    
# Model to represent a milestone in the user's development journey
class Milestone(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) # link each milestone to a user
    topic = models.CharField(max_length=200) # name of the milestone
    description = models.TextField(blank=True) # description of the milestone
    date_achieved = models.DateField(default=timezone.now) # date when the milestone was achieved

    class Meta:
        ordering = ['date_achieved'] # order by what was achieved first

    def __str__(self): # This code defines the string representation of the Milestone model
        return self.topic # when we print an instance of Milestone, it will return the name of the milestone