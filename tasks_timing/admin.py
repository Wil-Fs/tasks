from django.contrib import admin
from .models import Task, Time_Working

# Register your models here.
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    date_hierarchy = 'date'
    list_display = ['description', 'owner', 'date',]

@admin.register(Time_Working)
class TimeWorkingAdmin(admin.ModelAdmin):
    date_hierarchy = 'date'
    list_display = ['task', 'only_hours', 'date',]