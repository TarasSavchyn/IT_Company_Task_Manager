from django.contrib.auth import get_user_model
from django.test import TestCase

from task_manager.models import Position, TaskType, Task


class TestViewsIsPrivate(TestCase):
    def test_task_type_list_is_private(self):
        url = "http://localhost/task-types/"
        response = self.client.get(url)
        self.assertNotEquals(response.status_code, 200)

    def test_workers_list_is_private(self):
        url = "http://localhost/workers/"
        response = self.client.get(url)
        self.assertNotEquals(response.status_code, 200)

    def test_positions_list_is_private(self):
        url = "http://localhost/positions/"
        response = self.client.get(url)
        self.assertNotEquals(response.status_code, 200)

    def test_tasks_list_is_private(self):
        url = "http://localhost/tasks/"
        response = self.client.get(url)
        self.assertNotEquals(response.status_code, 200)


class TestViewsUnlocked(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test", password="test-123"
        )
        self.task_type = TaskType.objects.create(name="test")
        self.position = Position.objects.create(name="test")
        self.client.force_login(self.user)
        self.task = Task.objects.create(
            name="test",
            task_type=self.task_type,
            deadline="2023-01-01",
        )

    #
    def test_task_type_list_is_unlocked(self):
        url = "http://localhost/task-types/"
        response = self.client.get(url)
        task_types = TaskType.objects.all()
        self.assertEquals(response.status_code, 200)
        self.assertEquals(list(task_types), list(response.context["tasktype_list"]))
        self.assertTemplateUsed(response, "task_manager/tasktype_list.html")

    def test_worker_list_is_unlocked(self):
        url = "http://localhost/workers/"
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "task_manager/worker_list.html")

    def test_position_list_is_unlocked(self):
        url = "http://localhost/positions/"
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "task_manager/position_list.html")

    def test_task_list_is_unlocked(self):
        url = "http://localhost/tasks/"
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "task_manager/task_list.html")
