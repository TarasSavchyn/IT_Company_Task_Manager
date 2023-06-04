from django.urls import path, include

from task_manager.views import (
    index, TaskListView,

)


urlpatterns = [
    path("index/", index, name="index"),
    path("", index, name="index"),

    path("tasks/", TaskListView.as_view(), name="tasks-list"),

    ]



app_name = "task_manager"
