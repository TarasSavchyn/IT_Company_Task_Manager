from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from task_manager.forms import (
    WorkerCreateForm,
    WorkerUpdateForm,
    WorkerSearchForm,
    TaskSearchForm,
    TaskForm,
)
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

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TaskListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        context["search_form"] = TaskSearchForm(initial={"name": name})
        return context

    def get_queryset(self):
        queryset = Task.objects.all()
        form = TaskSearchForm(self.request.GET)
        return (
            queryset.filter(name__icontains=form.cleaned_data["name"])
            if form.is_valid()
            else queryset.all()
        )


class TaskDetailView(LoginRequiredMixin, generic.DetailView):
    model = Task


class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    model = Task
    success_url = reverse_lazy("task_manager:task-list")
    form_class = TaskForm


class TaskUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Task

    success_url = reverse_lazy("task_manager:task-list")
    form_class = TaskForm


class TaskDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Task
    success_url = reverse_lazy("task_manager:task-list")


class PositionListView(LoginRequiredMixin, generic.ListView):
    model = Position
    paginate_by = 5


class PositionListDetailView(LoginRequiredMixin, generic.DetailView):
    model = Position


class PositionCreateView(LoginRequiredMixin, generic.CreateView):
    model = Position
    fields = "__all__"
    success_url = reverse_lazy("task_manager:position-list")


class PositionUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Position
    fields = "__all__"
    success_url = reverse_lazy("task_manager:position-list")


class PositionDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Position
    success_url = reverse_lazy("task_manager:position-list")


class WorkerListView(LoginRequiredMixin, generic.ListView):
    model = Worker
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(WorkerListView, self).get_context_data(**kwargs)
        username = self.request.GET.get("username", "")
        context["search_form"] = WorkerSearchForm(initial={"username": username})
        return context

    def get_queryset(self):
        queryset = Worker.objects.all()
        form = WorkerSearchForm(self.request.GET)
        return (
            queryset.filter(username__icontains=form.cleaned_data["username"])
            if form.is_valid()
            else queryset.all()
        )


class WorkerDetailView(LoginRequiredMixin, generic.DetailView):
    model = Worker


class WorkerCreateView(generic.CreateView):
    model = Worker
    form_class = WorkerCreateForm


class WorkerUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Worker
    form_class = WorkerUpdateForm
    success_url = reverse_lazy("task-manager:worker-list")


class WorkerDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Worker
    success_url = reverse_lazy("task-manager:worker-list")


class TaskTypeListView(LoginRequiredMixin, generic.ListView):
    model = TaskType
    paginate_by = 10


class TaskTypeListDetailView(LoginRequiredMixin, generic.DetailView):
    model = TaskType


class TaskTypeCreateView(LoginRequiredMixin, generic.CreateView):
    model = TaskType
    fields = "__all__"
    success_url = reverse_lazy("task_manager:task-type-list")


class TaskTypeUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = TaskType
    fields = "__all__"
    success_url = reverse_lazy("task_manager:task-type-list")


class TaskTypeDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = TaskType
    success_url = reverse_lazy("task_manager:task-type-list")


@login_required
def toggle_assign_to_task(request, pk):
    worker = Worker.objects.get(id=request.user.id)
    if Task.objects.get(id=pk) in worker.task_set.all():
        worker.task_set.remove(pk)
    else:
        worker.task_set.add(pk)
    return HttpResponseRedirect(reverse_lazy("task-manager:task-detail", args=[pk]))
