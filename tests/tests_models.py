from django.test import TestCase

from task_manager.models import Worker, Position, Task, TaskType


class TestForModels(TestCase):
    def setUp(self) -> None:
        self.position = Position.objects.create(name="test")
        self.task_type = TaskType.objects.create(name="test")

    def test_task_type_str(self):
        example = TaskType.objects.create(name="test2")
        self.assertEquals(str(example), "test2")

    def test_position_str(self):
        example = Position.objects.create(name="test1")
        self.assertEquals(str(example), "test1")

    def test_task_str(self):
        example = Task.objects.create(
            name="test", deadline="2023-01-01", task_type=self.task_type
        )
        self.assertEquals(str(example), "test")

    def test_worker_str(self):
        example = Worker.objects.create_user(
            username="test", first_name="test", last_name="test", password="admin-123"
        )
        self.assertEquals(str(example), "test test")

    def test_position(self):
        example = Worker.objects.create_user(
            username="ts",
            first_name="test",
            last_name="test",
            password="admin-123",
            position=self.position,
        )
        self.assertEquals(example.username, "ts")
        self.assertTrue(example.check_password("admin-123"))
        self.assertEquals(example.position, self.position)
