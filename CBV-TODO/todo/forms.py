from django import forms

from .models import Todo

class DateTimeInput(forms.DateTimeInput):
    input_type = 'datetime-local'


#form for creating Task
class CreateTaskForm(forms.ModelForm):
   
    complete_by = forms.DateTimeField(widget=DateTimeInput())
    class Meta:
        model = Todo
        fields = ('task','complete_by')

       

#form for editing Task
class EditTaskForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ('task',)