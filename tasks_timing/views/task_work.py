from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from ..models import Task, TimeWorking
from ..forms import TaskForm

def time_working_list(request):
    if request.user.is_authenticated:
        times_tasks = TimeWorking.objects.all()
        return render(request, "tasks_timing/time_working_list.html", {'times_tasks':times_tasks})
    else:
        return redirect('login')



def add_desc_tm_working(request, tm_work_id):
    pass
