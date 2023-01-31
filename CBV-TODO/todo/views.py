from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from django.urls import reverse_lazy

from .models import Todo
from .forms import CreateTaskForm, EditTaskForm

class HomePageView(TemplateView):
    template_name = 'home.html'


# Lists the tasks 
class TaskListView(LoginRequiredMixin ,ListView):
    model = Todo
    template_name = 'task_list.html'
    context_object_name = 'todo_list'

    def get_queryset(self, *args, **kwargs):
        return super().get_queryset().filter(author=self.request.user)
 

# List the Task in detail
class TaskDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Todo
    template_name = 'task_detail.html'
    context_object_name = 'todo'

    def get_queryset(self, *args, **kwargs):
        return super().get_queryset().filter(author=self.request.user)
    
#Creates tasks
class CreateTaskView(LoginRequiredMixin,CreateView):
    model = Todo
    form_class = CreateTaskForm
    # fields = ['task', 'complete_by']
    template_name = 'task_create.html'
    

#Edits task
class EditTaskView(LoginRequiredMixin,UpdateView):
    model = Todo
    fields = 'task',
    template_name = 'task_edit.html'

    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(author=self.request.user)

#Deletes task
class DeleteTaskView(LoginRequiredMixin,DeleteView):
    model = Todo
    success_url = reverse_lazy("task_list")
    template_name = "task_delete.html"

    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(author=self.request.user)