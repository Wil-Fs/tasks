from django import forms
from ..models import TimeWorking

class TimeWorkingForm(forms.ModelForm):
    job_description = forms.CharField(required=True, widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "Detalhes do trabalho realizado"
        }),
        label = "",
    )

    class Meta:
        model = TimeWorking
        exclude = ("date", "hours_working_in", "hours_working_out", "hours_worked", "time_in", "time_out")

