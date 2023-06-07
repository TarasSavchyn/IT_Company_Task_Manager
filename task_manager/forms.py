from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from task_manager.models import Worker


class WorkerSearchForm(forms.Form):
    username = forms.CharField(
        max_length=255,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by username"}),
    )


class TaskSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by name"}),
    )


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

