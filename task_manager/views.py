from django.contrib.auth.mixins import LoginRequiredMixin
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


class TaskListView(LoginRequiredMixin, generic.ListView):
    model = Task
    paginate_by = 2


class TaskListDetailView(LoginRequiredMixin, generic.DetailView):
    model = Task


class PositionListView(LoginRequiredMixin, generic.ListView):
    model = Position
    paginate_by = 10


class PositionListDetailView(LoginRequiredMixin, generic.DetailView):
    model = Position


class WorkerListView(LoginRequiredMixin, generic.ListView):
    model = Worker
    paginate_by = 2


class WorkerListDetailView(LoginRequiredMixin, generic.DetailView):
    model = Worker


class TaskTypeListView(LoginRequiredMixin, generic.ListView):
    model = TaskType
    paginate_by = 10


class TaskTypeListDetailView(LoginRequiredMixin, generic.DetailView):
    model = TaskType
