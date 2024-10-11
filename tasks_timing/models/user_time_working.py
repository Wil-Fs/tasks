from django.db import models
from ..models import Task

class TimeWorking(models.Model):
    job_description = models.CharField(max_length=800, blank=False, null=False, default='Sem detalhes registrados!')
    hours_working_in = models.DateTimeField(null=True, blank=True, editable=False, auto_now_add=True)
    hours_working_out = models.DateTimeField(null=True, blank=True, editable=False)
    hours_worked = models.DurationField(null=True, blank=True, editable=False)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    time_in = models.BooleanField(default=False)
    time_out = models.BooleanField(default=False)

    @property
    def only_hours(self):
        if self.hours_working_in and self.hours_working_out:
            self.hours_worked = self.hours_working_out - self.hours_working_in
            hours_in_seconds = self.hours_worked.total_seconds()
            hours = int(hours_in_seconds // 3600)
            minutes = int((hours_in_seconds % 3600) // 60)
            return f"{hours}:{minutes}"


    def __str__(self):
        return f"{self.task.description}"