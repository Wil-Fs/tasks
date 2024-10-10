from django.shortcuts import render

def home(request):
    text = 'Hi, good luck'


    return render(request, 'tasks_timing/home.html', {'text':text})