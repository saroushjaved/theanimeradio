from django.test import TestCase
from django.urls import reverse


class PublicPageTests(TestCase):
    def test_home_page_loads(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "the anime radio")
        self.assertContains(response, 'name="description"')
        self.assertContains(response, 'rel="canonical"')

    def test_sitemap_loads_as_xml(self):
        response = self.client.get(reverse("sitemap"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response["Content-Type"], "application/xml")
        self.assertContains(response, "<urlset")

    def test_robots_txt_points_to_sitemap(self):
        response = self.client.get(reverse("robots_txt"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response["Content-Type"], "text/plain")
        self.assertContains(response, "Sitemap:")
