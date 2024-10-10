from django.shortcuts import render, redirect
from ..models import Task


def home(request):
    if request.user.is_authenticated:
        text = 'Good luck my besto friendo'
        return render(request, 'tasks_timing/home.html', {'text': text})
    else:
        return redirect('login')