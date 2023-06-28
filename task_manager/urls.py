from django.urls import path, include

from task_manager.views import (
    index,
    TaskListView,
    TaskDetailView,
    PositionListView,
    PositionListDetailView,
    WorkerListView,
    WorkerDetailView,
    TaskTypeListView,
    TaskTypeDetailView,
    TaskTypeCreateView,
    TaskTypeUpdateView,
    TaskTypeDeleteView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    PositionCreateView,
    PositionUpdateView,
    PositionDeleteView,
    WorkerCreateView,
    WorkerUpdateView,
    WorkerDeleteView,
    toggle_assign_to_task,
    take_task_to_work,
    mark_task_as_done,
    return_task_for_revision,
)


urlpatterns = [
    path("index/", index, name="index"),
    path("", index, name="index"),
    path("tasks/", TaskListView.as_view(), name="task-list"),
    path("tasks/<int:pk>/", TaskDetailView.as_view(), name="task-detail"),
    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),
    path("tasks/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("tasks/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
    path(
        "tasks/<int:pk>/toggle-assign/",
        toggle_assign_to_task,
        name="toggle-task-assign",
    ),
    path(
        "tasks/<int:pk>/take-task-to-work/",
        take_task_to_work,
        name="take-task-to-work",
    ),
    path(
        "tasks/<int:pk>/mark-task-as-done/",
        mark_task_as_done,
        name="mark-task-as-done",
    ),
    path(
        "tasks/<int:pk>/return-task-for-revision/",
        return_task_for_revision,
        name="return-task-for-revision",
    ),
    path("positions/", PositionListView.as_view(), name="position-list"),
    path(
        "positions/<int:pk>/", PositionListDetailView.as_view(), name="position-detail"
    ),
    path("positions/create/", PositionCreateView.as_view(), name="position-create"),
    path(
        "positions/<int:pk>/update/",
        PositionUpdateView.as_view(),
        name="position-update",
    ),
    path(
        "positions/<int:pk>/delete/",
        PositionDeleteView.as_view(),
        name="position-delete",
    ),
    path("workers/", WorkerListView.as_view(), name="worker-list"),
    path("workers/<int:pk>/", WorkerDetailView.as_view(), name="worker-detail"),
    path("workers/create/", WorkerCreateView.as_view(), name="worker-create"),
    path("workers/<int:pk>/update/", WorkerUpdateView.as_view(), name="worker-update"),
    path("workers/<int:pk>/delete/", WorkerDeleteView.as_view(), name="worker-delete"),
    path("task-types/", TaskTypeListView.as_view(), name="task-type-list"),
    path(
        "task-types/<int:pk>/",
        TaskTypeDetailView.as_view(),
        name="task-type-detail",
    ),
    path("task-types/create/", TaskTypeCreateView.as_view(), name="task-types-create"),
    path(
        "task-types/<int:pk>/update/",
        TaskTypeUpdateView.as_view(),
        name="task-types-update",
    ),
    path(
        "task-types/<int:pk>/delete/",
        TaskTypeDeleteView.as_view(),
        name="task-types-delete",
    ),
]


app_name = "task_manager"
