from django.contrib import admin
from .models import Task, TimeWorking

# Register your models here.
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    date_hierarchy = 'date'
    list_display = ['description', 'owner', 'date',]

@admin.register(TimeWorking)
class TimeWorkingAdmin(admin.ModelAdmin):
    date_hierarchy = 'hours_working_in'
    list_display = ['task', 'only_hours', 'hours_working_in', 'hours_working_out',]