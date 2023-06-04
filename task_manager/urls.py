from django.urls import path, include

from task_manager.views import (
    index, TaskListView, TaskListDetailView,

)


urlpatterns = [
    path("index/", index, name="index"),
    path("", index, name="index"),

    path("tasks/", TaskListView.as_view(), name="tasks-list"),
    path("tasks/<int:pk>/", TaskListDetailView.as_view(), name="task-detail"),

    ]



app_name = "task_manager"
