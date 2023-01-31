from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.http import Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import Todo
from .forms import CreateTaskForm, EditTaskForm, SignUpForm

@login_required
def todoListView(request):
    todo_list = get_list_or_404(Todo, author=request.user)
    
    context = {
        'todo_list': todo_list
    }
    
    return render(request, 'todo_list.html', context)


def homepage(request):
    return render(request, 'home.html')



#view detail of task
@login_required
def detailTaskView(request, pk):
    todo = get_todo(pk,request)
    return render(request, 'task_detail.html', {'todo':todo})


@login_required
def CreateTaskView(request):
    if request.method == 'POST':
        form = CreateTaskForm(request.POST)
        if form.is_valid():
            todo = Todo(**form.cleaned_data)
            todo.save()
            return redirect(reverse('home'))
    else:
        form = CreateTaskForm()
    context = {
        'form':form
    }
    return render(request, 'task_create.html', context)

# Edit Task
def get_todo( pk, request):
    return get_object_or_404(Todo, pk=pk, author=request.user)

@login_required
def editTaskView(request, pk):
    todo = get_todo(pk, request)
    if request.method == 'POST':
        form = EditTaskForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect(reverse('task_list'))
    else:
        form = EditTaskForm(instance=todo)
    context = {
        "form":form

    }
    return render(request, 'task_edit.html', context)


#Delete Task
@login_required
def deleteTask(request, pk):
    todo = get_todo(pk, request)
    if request.method == 'POST':
        todo.delete()
        return redirect('task_list')
    context = {
        'todo':todo,
    }

    return render(request, 'task_delete.html', context)



#signup view
def signUpView(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()
    context = {
        'form': form
    }
    return render(request, 'registration/signup.html', context)