from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from task_manager.models import Worker


class WorkerCreateForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Worker

        fields = UserCreationForm.Meta.fields + (
            "position",
            "first_name",
            "last_name"
        )


class WorkerUpdateForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = Worker

