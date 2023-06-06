from django.urls import path, include

from task_manager.views import (
    index, TaskListView, TaskListDetailView, PositionListView, PositionListDetailView, WorkerListView,
    WorkerListDetailView, TaskTypeListView, TaskTypeListDetailView,

)


urlpatterns = [
    path("index/", index, name="index"),
    path("", index, name="index"),

    path("tasks/", TaskListView.as_view(), name="tasks-list"),
    path("tasks/<int:pk>/", TaskListDetailView.as_view(), name="task-detail"),

    path("positions/", PositionListView.as_view(), name="position-list"),
    path("positions/<int:pk>/", PositionListDetailView.as_view(), name="position-detail"),

    path("workers/", WorkerListView.as_view(), name="worker-list"),
    path("workers/<int:pk>/", WorkerListDetailView.as_view(), name="worker-detail"),

    path("task-types/", TaskTypeListView.as_view(), name="task-type-list"),
    path("task-types/<int:pk>/", TaskTypeListDetailView.as_view(), name="task-type-detail"),


    ]



app_name = "task_manager"
