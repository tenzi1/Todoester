from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Todo

class DateTimeInput(forms.DateTimeInput):
    input_type = 'datetime-local'

# Task Creation Form
class CreateTaskForm(forms.Form):
    task = forms.CharField(max_length=256)
    complete_by = forms.DateTimeField(widget=DateTimeInput)

#Task Edit form
class EditTaskForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['task', 'complete_by']

        
#User Signup form
class SignUpForm(UserCreationForm):
    pass
