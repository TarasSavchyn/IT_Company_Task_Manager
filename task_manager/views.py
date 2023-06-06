from django.shortcuts import render
from django.views import generic

from task_manager.models import Worker, Task, TaskType, Position


def index(request):
    """View function for the home page of the site."""

    num_workers = Worker.objects.count()
    num_tasks = Task.objects.count()
    num_task_types = TaskType.objects.count()
    num_position = Position.objects.all().count()
    num_visits = request.session.get("num_visits", 0)

    request.session["num_visits"] = num_visits + 1

    context = {
        "num_workers": num_workers,
        "num_tasks": num_tasks,
        "num_task_types": num_task_types,
        "num_position": num_position,
        "num_visits": num_visits + 1,
    }

    return render(request, "task_manager/index.html", context=context)


class TaskListView(generic.ListView):
    model = Task
    paginate_by = 2


class TaskListDetailView(generic.DetailView):
    model = Task


class PositionListView(generic.ListView):
    model = Position


class PositionListDetailView(generic.DetailView):
    model = Position


class WorkerListView(generic.ListView):
    model = Worker
    paginate_by = 2


class WorkerListDetailView(generic.DetailView):
    model = Worker


class TaskTypeListView(generic.ListView):
    model = TaskType
    paginate_by = 10


class TaskTypeListDetailView(generic.DetailView):
    model = TaskType
