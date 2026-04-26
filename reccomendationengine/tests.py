from django.test import TestCase
from django.urls import reverse


class RecommendationFlowTests(TestCase):
    def test_recommendation_home_loads(self):
        response = self.client.get(reverse("reccomendationhome"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Get Started")

    def test_missing_first_answer_does_not_crash(self):
        response = self.client.get(reverse("reccomendatio-question-1"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "anime")

    def test_empty_instant_recommendation_set_is_handled(self):
        response = self.client.get(reverse("reccomendatio-question-1"), {"answer1": "0"})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "anime")
