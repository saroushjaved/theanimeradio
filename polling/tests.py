from django.test import TestCase
from django.urls import reverse


class PollingTests(TestCase):
    def test_polling_home_loads(self):
        response = self.client.get(reverse("polling"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Poll")

    def test_missing_poll_id_returns_not_found(self):
        response = self.client.get(reverse("pollingpage"))
        self.assertEqual(response.status_code, 404)
