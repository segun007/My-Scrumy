from django.shortcuts import render
from django.http import HttpResponse
from .models import ScrumyUser, ScrumyGoals, GoalStatus
from django.shortcuts import get_object_or_404, render
# Create your views here.

def index(request):
	#users = ScrumyUser.objects.all()
	#output = ','.join([s.first_name for s in users])
	goals= ScrumyGoals.objects.filter(goal_type='DT')

	return HttpResponse(goals)

def detail(request, task_id):
	return HttpResponse("You re looking at user %s." % task_id)


def move_goal(request, task_id):
	goal = get_object_or_404(ScrumyGoals, pk=task_id)
	return HttpResponse(goal)

def add_user(request):
	username = ScrumyUser.objects.all()
	output = " ".join([eachuser.full_name for eachuser in username])
	return HttpResponse(output)
	
    
  #full_name = models.CharField(max_length=50),
	#    email = models.EmailField(max_length=100)
	  #  )
    	#user.save()