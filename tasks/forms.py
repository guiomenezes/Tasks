from django.forms import ModelForm
from .models import Tasks


class TasksForm(ModelForm):
    class Meta:
        model = Tasks
        fields = ['task', 'description', 'completed'] # Exclui o campo user do formulário
    
    def __init__(self, *args, **kwargs):
        super(TasksForm, self).__init__(*args, **kwargs)

        # Adiciona classes CSS para melhorar a aparência
        self.fields['task'].widget.attrs.update({
            'class': 'form-control'
        })

        self.fields['description'].widget.attrs.update({
            'class': 'form-control',
            'rows': 5
        })

        self.fields['completed'].widget.attrs.update({
            'class': 'form-check-input'
        })