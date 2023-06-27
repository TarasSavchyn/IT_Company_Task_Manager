from django.contrib.auth import get_user_model
from django.test import TestCase, Client

from task_manager.models import Position


class TestsForAdminPanel(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.position = Position.objects.create(name="Developer", duties="")
        self.user_admin = get_user_model().objects.create_superuser(
            username="test",
            password="admin-123",
            position=self.position,
            photo="mages/2023/06/26/shutterstock_142028593.jpg",
        )
        self.client.force_login(self.user_admin)

    def test_admin_panel_position_and_photo(self):
        url = "http://localhost/workers/"
        res = self.client.get(url)
        self.assertContains(res, self.user_admin.position)
        self.assertIsNotNone(self.user_admin.photo)
