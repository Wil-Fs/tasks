from django.urls import path
from .views import home, tasks, add_task, start_task, time_working_list, add_desc_tm_working, update_task, delete_task, view_time_working

urlpatterns = [
    path('', home, name='home'),
    path('tasks_list', tasks, name='tasks-list'),
    path('add_task', add_task, name='add-task'),
    path('update_task?<pk>', update_task, name='update-task'),
    path('delete_task?<pk>', delete_task, name='delete-task'),
    path('start_task?<pk>', start_task, name='start-task'),
    path('time_working_list', time_working_list, name="time-working-list"),
    path('add_desc_tm_working?<pk>', add_desc_tm_working, name='add-desc-tm-working'),
    path('view_time_working?<pk>', view_time_working, name="view-time-working")
]