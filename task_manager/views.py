from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import generic

from task_manager.forms import (
    WorkerCreateForm,
    WorkerUpdateForm,
    WorkerSearchForm,
    # TaskSearchForm,
    TaskForm,
)
from task_manager.models import Worker, Task, TaskType, Position


def index(request):
    """View function for the home page of the site."""

    num_tasks = Task.objects.count()
    num_solved_task = Task.objects.filter(is_completed=True).count()
    not_solved = num_tasks - num_solved_task

    num_visits = request.session.get("num_visits", 0)

    request.session["num_visits"] = num_visits + 1

    context = {
        "not_solved": not_solved,
        "num_tasks": num_tasks,
        "num_solved_task": num_solved_task,
        "num_visits": num_visits + 1,
    }

    return render(request, "task_manager/index.html", context=context)


class TaskListView(LoginRequiredMixin, generic.ListView):
    model = Task


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TaskListView, self).get_context_data(**kwargs)

        context["not_done"] = list(Task.objects.filter(status="not_done"))
        context["in_progress"] = list(Task.objects.filter(status="in_progress"))
        context["approved"] = list(Task.objects.filter(status="approved"))

        return context


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
    paginate_by = 4


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
    paginate_by = 6

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(WorkerListView, self).get_context_data(**kwargs)
        username = self.request.GET.get("username", "")
        context["search_form"] = WorkerSearchForm(initial={"username": username})
        return context

    def get_queryset(self):
        queryset = Worker.objects.all().select_related("position")
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
    paginate_by = 6


class TaskTypeDetailView(LoginRequiredMixin, generic.DetailView):
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


def take_task_to_work(request, pk):
    task = Task.objects.get(pk=pk)
    task.status = "in_progress"
    task.save()
    return HttpResponseRedirect(reverse_lazy("task-manager:task-detail", args=[pk]))


def mark_task_as_done(request, pk):
    task = Task.objects.get(pk=pk)
    task.status = "approved"
    task.is_completed = True
    task.save()

    return HttpResponseRedirect(reverse_lazy("task-manager:task-detail", args=[pk]))


def return_task_for_revision(request, pk):
    task = Task.objects.get(pk=pk)
    task.status = "in_progress"
    task.is_completed = False
    task.save()
    return HttpResponseRedirect(reverse_lazy("task-manager:task-detail", args=[pk]))
