from idlelib.rpc import request_queue

from django.shortcuts import render, redirect
from django.contrib import messages
from ..models import Task
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
                messages.warning(request, 'Sua tarefa foi cadastrada!')
                return redirect('tasks-list')

        return render(request, 'tasks_timing/add_task.html', {
            'form': form
        })


    else:
        return redirect('login')