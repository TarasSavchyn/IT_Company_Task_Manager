from django.contrib.auth import get_user_model
from django.test import TestCase, Client

from task_manager.forms import WorkerCreateForm


class TestDriverCreationForm(TestCase):
    def test_worker_form_intro(self):
        form_data = {
            "username": "test",
            "password1": "admin-123",
            "password2": "admin-123",
        }

        form = WorkerCreateForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEquals(form_data, form.cleaned_data)


class TestWorkerSearchForm(TestCase):
    def setUp(self) -> None:
        self.user_1 = get_user_model().objects.create_user(
            username="test1",
            password="admin-123",
        )
        self.user_2 = get_user_model().objects.create_user(
            username="test2",
            password="admin-123",
        )
        self.client.force_login(self.user_1)

    def test_worker_search_form(self):
        url = "http://localhost/workers/?username=1"
        response = self.client.get(url)
        self.assertContains(response, self.user_1.username)
        self.assertNotContains(response, self.user_2.username)
