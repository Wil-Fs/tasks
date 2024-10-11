from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from ..forms import TimeWorkingForm, TimeWorkingFilterForm
from ..models import Task, TimeWorking

from datetime import datetime

def time_working_list(request):
    if request.user.is_authenticated:
        form = TimeWorkingFilterForm(request.GET or None)
        times_tasks = TimeWorking.objects.all()

        if form.is_valid():
            if form.cleaned_data['task']:
                times_tasks = times_tasks.filter(task=form.cleaned_data['task'])
            if form.cleaned_data['manager']:
                times_tasks = times_tasks.filter(task__manager=form.cleaned_data['manager'])
            if form.cleaned_data['hours_working_in']:
                times_tasks = times_tasks.filter(hours_working_in__gte=form.cleaned_data['hours_working_in'])
            if form.cleaned_data['hours_working_out']:
                times_tasks = times_tasks.filter(hours_working_out__lte=form.cleaned_data['hours_working_out'])


        return render(request, "tasks_timing/time_working_list.html", {
            'times_tasks': times_tasks,
            'form': form
        })
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

def stop_time_work(request, pk):
    if request.user.is_authenticated:
        time_working = get_object_or_404(TimeWorking, id=pk)
        time_working.hours_working_out = datetime.now()
        time_working.time_out = True
        time_working.save()

        messages.warning(request, f'A terefa "{time_working}" foi encerrada, horas trabalhadas contabilizadas!')
        return redirect('time-working-list')
    else:
        return redirect('login')