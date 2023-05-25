from django.contrib.auth.models import AbstractUser
from django.db import models


class Position(models.Model):
    name = models.CharField(max_length=63, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class TaskType(models.Model):
    name = models.CharField(max_length=63, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Worker(AbstractUser):

    position = models.ForeignKey(Position, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        ordering = ["position"]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Task(models.Model):
    PRIORITIES = (
        ("High", "One week"),
        ("Medium", "One month"),
        ("Low", "Three month"),
        ("Absent", "Free time"),
    )

    name = models.CharField(max_length=63)
    description = models.TextField(blank=True, null=True)
    deadline = models.DateField()
    is_completed = models.BooleanField(default=False)
    priority = models.CharField(max_length=63, choices=PRIORITIES)
    task_type = models.ForeignKey(TaskType, on_delete=models.DO_NOTHING)
    assignees = models.ManyToManyField(Worker)

    class Meta:
        ordering = ["priority"]
