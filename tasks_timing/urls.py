from django.urls import path
from .views import home, tasks, add_task, start_task, time_working_list, add_desc_tm_working

urlpatterns = [
    path('', home, name='home'),
    path('tasks_list', tasks, name='tasks-list'),
    path('add_task', add_task, name='add-task'),
    path('start_task?<pk>', start_task, name='start-task'),
    path('time_working_list', time_working_list, name="time-working-list"),
    path('add_desc_tm_working?<pk>', add_desc_tm_working, name='add-desc-tm-working'),
]