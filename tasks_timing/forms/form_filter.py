from django import forms
from django.contrib.auth.models import User
from ..models import Task, TimeWorking

class TimeWorkingFilterForm(forms.Form):
    task = forms.ModelChoiceField(queryset=Task.objects.all(), label='Tarefa:', required=False, widget=forms.Select(attrs={'class':'col-3 form-select inputs_form'}) )
    manager = forms.ModelChoiceField(queryset=User.objects.all(), label='Usuário Resposável:',required=False, widget=forms.Select(attrs={'class':'col-3 form-select inputs_form'}) )
    hours_working_in = forms.DateTimeField(required=False, label='Data/Hora Início:', widget=forms.DateInput(attrs={'class':'col-3 form-control inputs_form', 'type': 'date' }))
    hours_working_out = forms.DateTimeField(required=False, label='Data/Hora Fim:', widget=forms.DateInput(attrs={'class':'col-3 form-control inputs_form', 'type': 'date' }))


class TaskFilterForm(forms.Form):
    manager = forms.ModelChoiceField(queryset=User.objects.all(), required=False, widget=forms.Select(attrs={'class':'col-3 form-select inputs_form'}))
    date = forms.DateField(required=False, widget=forms.DateInput(attrs={'class':'col-3 form-control inputs_form', 'type': 'date'}))
    description = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class':'col-3 form-control inputs_form', 'type': 'text' }))
