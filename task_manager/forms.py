from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core.exceptions import ValidationError

from task_manager.models import Worker, Task


class TaskForm(forms.ModelForm):
    assignees = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
    description = forms.CharField(max_length=255)

    class Meta:
        model = Task
        fields = "__all__"

    def clean_name(self) -> str:
        name = self.cleaned_data.get("name", "")
        if len(name.split()) > 10:
            raise ValidationError("Not more than 10 words!")
        return name


class WorkerSearchForm(forms.Form):
    username = forms.CharField(
        max_length=255,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Search worker....",
                "class": "form-control mr-sm-2",
                "type": "search",
                "aria-label": "Search"
            }
        ),
    )


class TaskSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Search task....",
                "class": "form-control mr-sm-2",
                "type": "search",
                "aria-label": "Search"
            }
        ),
    )


class WorkerCreateForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Worker
        fields = UserCreationForm.Meta.fields + ("position", "first_name", "last_name", "photo")


class WorkerUpdateForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = Worker
