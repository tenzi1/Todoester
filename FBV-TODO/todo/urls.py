from django.urls import path

from . import views

urlpatterns = [
    path("", views.homepage, name="home"),
    path("task/<int:pk>/", views.detailTaskView, name="task_detail" ),
    path("task/edit/<int:pk>/", views.editTaskView, name="task_edit" ),
    path("task/delete/<int:pk>/", views.deleteTask, name="task_delete" ),
    path("task/create/", views.CreateTaskView, name="task_create"),
    path("tasks/", views.todoListView, name="task_list"),
    path("signup/", views.signUpView, name="signup")
]