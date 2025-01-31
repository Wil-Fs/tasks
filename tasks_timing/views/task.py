from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from ..models import Task, TimeWorking
from ..forms import TaskForm, TaskFilterForm


def tasks(request):
    if request.user.is_authenticated:
        form = TaskFilterForm(request.GET or None)
        tasks = Task.objects.all()

        if form.is_valid():
            if form.cleaned_data['manager']:
                tasks = tasks.filter(manager=form.cleaned_data['manager'])
            if form.cleaned_data['date']:
                tasks = tasks.filter(date__lte=form.cleaned_data['date'])
            if form.cleaned_data['description']:
                tasks = tasks.filter(description__icontains=form.cleaned_data['description'])

        return render(request, "tasks_timing/tasks_list.html", {'tasks': tasks, 'form': form})
    else:
        return redirect('login')


def add_task(request):
    if request.user.is_authenticated:
        form = TaskForm(request.POST or None)

        if request.method == "POST":
            if form.is_valid():
                task = form.save(commit=False)
                task.owner = request.user
                task.save()
                messages.warning(request, f'A tarefa "{task}" foi cadastrada!')
                return redirect('tasks-list')

        return render(request, 'tasks_timing/add_task.html', {
            'form': form
        })


    else:
        return redirect('login')

def start_task(request, pk):
    if request.user.is_authenticated:
        task = get_object_or_404(Task, id=pk)
        time_working = TimeWorking.objects.create(
            task=task,
            time_in=True
        )

        messages.warning(request, f'A terefa "{task}" foi iniciada!')
        return redirect('time-working-list')
    else:
        return redirect('login')

def update_task(request, pk):
    if request.user.is_authenticated:
        task = get_object_or_404(Task, id=pk)
        if request.user == task.owner or request.user == task.manager:
            form = TaskForm(request.POST or None, instance=task)
            if request.method == "POST":
                if form.is_valid():
                    task = form.save(commit=False)
                    task.user = request.user
                    task.save()
                    messages.warning(request, f'Descrição adicionada a tarefa "{task}"')
                    return redirect('tasks-list')
            else:
                return render(request, 'tasks_timing/update_task.html', {
                    'task': task,
                    'form': form,
                })
        else:
            messages.warning(request, 'Somente o owner, ou usuário reponsável podem atualizar esta tarefa!')
            return redirect(request.META.get('HTTP_REFERER'))

    else:
        return redirect('login')


def delete_task(request, pk):
    if request.user.is_authenticated:
        task = get_object_or_404(Task, id=pk)
        if request.user == task.owner:
            task.delete()
            messages.warning(request, f'A tarefa "{task}" foi deletada!')
            return redirect(request.META.get('HTTP_REFERER'))
        else:
            messages.warning(request, 'Somente o owner, pode deletar esta tarefa!')
            return redirect(request.META.get('HTTP_REFERER'))
    else:
        redirect('login')
