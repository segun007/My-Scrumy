from django.urls import path
from . import views

app_name = 'owolabiscrumy'
urlpatterns = [
	path('', views.index, name='index'),
	path('<int:task_id>/', views.move_goal, name='move_goal'),
	path('<int:task_id>/detail/', views.detail, name='detail'),
	path('add_user/', views.add_user, name='add_user'),
	

]
