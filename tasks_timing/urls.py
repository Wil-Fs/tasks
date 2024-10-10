from django.urls import path
from .views import home, tasks, add_task

urlpatterns = [
    path('', home, name='home'),
    path('tasks_list', tasks, name='tasks-list'),
    path('add_task', add_task, name='add-task'),

]