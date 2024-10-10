from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from ..forms.time_working_form import TimeWorkingForm
from ..models import Task, TimeWorking
from ..forms import TaskForm

def time_working_list(request):
    if request.user.is_authenticated:
        times_tasks = TimeWorking.objects.all()
        return render(request, "tasks_timing/time_working_list.html", {'times_tasks':times_tasks})
    else:
        return redirect('login')



def add_desc_tm_working(request, pk):
    if request.user.is_authenticated:
        time_working_task = get_object_or_404(TimeWorking, id=pk)
        if request.user == time_working_task.task.owner:
            form = TimeWorkingForm(request.POST or None, instance=time_working_task)
            if request.method == "POST":
                if form.is_valid():
                    time_working_task = form.save(commit=False)
                    time_working_task.user = request.user
                    time_working_task.save()
                    messages.warning(request, f'Descrição adicionada a tarefa "{time_working_task}"')
                    return redirect('time-working-list')
            else:
                return render(request, 'tasks_timing/add_desc_tm_working.html', {
                    'time_working_task': time_working_task,
                    'form': form,
                })
        else:
            return redirect('login')

    else:
        return redirect('login')

def view_time_working(request, pk):
    if request.user.is_authenticated:
        time_working_task = get_object_or_404(TimeWorking, id=pk)

        return render(request, 'tasks_timing/view_time_working.html', {
            'time_working_task': time_working_task,
        })
    else:
        return redirect('login')
