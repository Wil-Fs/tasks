from django import forms
from ..models import Task

class TaskForm(forms.ModelForm):
    description = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            "class": "form-control",
            "placeholder": "Descrição",
            "rows":"40",
            "cols":"100",
        }),
        label = "",
    )

    class Meta:
        model = Task
        fields = ('manager', 'description',)
        exclude = ('date',)

        labels = {
            'owner': 'Usuário Reposável:'
        }

        widgets = {
            'manager': forms.Select(
            attrs={
                "class": "form-select",
            }),
        }