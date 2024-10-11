from django import forms
from django.contrib.auth.models import User
from ..models import Task, TimeWorking

class TimeWorkingFilterForm(forms.Form):
    task = forms.ModelChoiceField(queryset=Task.objects.all(), label='Tarefa:', required=False, widget=forms.Select(attrs={'class':'col-3 form-select'}) )
    manager = forms.ModelChoiceField(queryset=User.objects.all(), label='Usuário Resposável:',required=False, widget=forms.Select(attrs={'class':'col-3 form-select'}) )
    hours_working_in = forms.DateTimeField(required=False, label='Data/Hora Início:', widget=forms.DateInput(attrs={'class':'col-3 form-control', 'type': 'date' }))
    hours_working_out = forms.DateTimeField(required=False, label='Data/Hora Fim:', widget=forms.DateInput(attrs={'class':'col-3 form-control', 'type': 'date' }))
