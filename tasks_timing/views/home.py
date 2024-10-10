from django.shortcuts import render, redirect
from ..models import Task


def home(request):
    if request.user.is_authenticated:
        return redirect('tasks-list')
    else:
        return redirect('login')
