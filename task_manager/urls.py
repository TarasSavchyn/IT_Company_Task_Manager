from django.urls import path, include

from task_manager.views import (
    index, TaskListView, TaskListDetailView, PositionListView, PositionListDetailView, WorkerListView,
    WorkerListDetailView, TaskTypeListView, TaskTypeListDetailView, TaskTypeCreateView, TaskTypeUpdateView,
    TaskTypeDeleteView, TaskCreateView, TaskUpdateView, TaskDeleteView, PositionCreateView, PositionUpdateView,
    PositionDeleteView,

)


urlpatterns = [
    path("index/", index, name="index"),
    path("", index, name="index"),

    path("tasks/", TaskListView.as_view(), name="task-list"),
    path("tasks/<int:pk>/", TaskListDetailView.as_view(), name="task-detail"),
    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),
    path("tasks/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("tasks/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),


    path("positions/", PositionListView.as_view(), name="position-list"),
    path("positions/<int:pk>/", PositionListDetailView.as_view(), name="position-detail"),
    path("positions/create/", PositionCreateView.as_view(), name="position-create"),
    path("positions/<int:pk>/update/", PositionUpdateView.as_view(), name="position-update"),
    path("positions/<int:pk>/delete/", PositionDeleteView.as_view(), name="position-delete"),

    path("workers/", WorkerListView.as_view(), name="worker-list"),
    path("workers/<int:pk>/", WorkerListDetailView.as_view(), name="worker-detail"),

    path("task-types/", TaskTypeListView.as_view(), name="task-type-list"),
    path("task-types/<int:pk>/", TaskTypeListDetailView.as_view(), name="task-type-detail"),
    path("task-types/create/", TaskTypeCreateView.as_view(), name="task-types-create"),
    path("task-types/<int:pk>/update/", TaskTypeUpdateView.as_view(), name="task-types-update"),
    path("task-types/<int:pk>/delete/", TaskTypeDeleteView.as_view(), name="task-types-delete"),
    ]



app_name = "task_manager"
