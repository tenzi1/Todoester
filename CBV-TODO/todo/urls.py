from django.urls import path

from . import views

urlpatterns = [
    path("", views.HomePageView.as_view(), name="home"),
    path("tasks/", views.TaskListView.as_view(), name="task_list"),
    path("task/<int:pk>/", views.TaskDetailView.as_view(), name="task_detail"),
    path("task/<int:pk>/edit/", views.EditTaskView.as_view(), name="task_edit"),
    path("task/create/", views.CreateTaskView.as_view(), name="task_create"),
    path("task/<int:pk>/delete/", views.DeleteTaskView.as_view(), name="task_delete"),
]