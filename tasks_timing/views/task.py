from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from ..models import Task, TimeWorking
from ..forms import TaskForm


def tasks(request):
    if request.user.is_authenticated:
        tasks = Task.objects.all()
        return render(request, 'tasks_timing/tasks_list.html', {'tasks': tasks})
    else:
        return redirect('login')


def add_task(request):
    if request.user.is_authenticated:
        form = TaskForm(request.POST or None)

        if request.method == "POST":
            if form.is_valid():
                task = form.save(commit=False)
                task.save()
                messages.warning(request, f'A tarefa {task} foi cadastrada!')
                return redirect('tasks-list')

        return render(request, 'tasks_timing/add_task.html', {
            'form': form
        })


    else:
        return redirect('login')

def start_task(request, pk):
    if request.user.is_authenticated:
        task = Task.objects.get(id=pk)
        time_working = TimeWorking.objects.create(
            task=task,
            time_in=True
        )

        messages.warning(request, f'A terefa "{task}" foi iniciada!')
        return redirect('tasks-list')
    else:
        return redirect('login')