# Benjamin Heerlyn
# CIS218
# 4/15/2024

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from .models import Twit

class TwitTest(TestCase):
    """Twit Test"""

    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="testuser", email="onvsoerjno@gmail.com", password="Benh2003"
        )

        cls.twit = Twit.objects.create(
            body="Updated body",
            author= cls.user,
        )

    def test_twit_model(self):
        """Test twit Model"""
        self.client.force_login(self.user)
        self.assertEqual(self.twit.body, "Updated body")
        self.assertEqual(self.twit.author.username, "testuser")
        self.assertEqual(self.twit.get_absolute_url(), "/twits/1/")

    def test_url_exists_at_correct_location_listview(self):
        """Test to see if url exists at correct location listview"""
        self.client.force_login(self.user)
        response = self.client.get("/twits/")
        self.assertEqual(response.status_code, 200)
    
    def test_url_exists_at_correct_location_detailview(self):
        """Test to see if url exists at correct location detailview"""
        self.client.force_login(self.user)
        response = self.client.get("/twits/1/")
        self.assertEqual(response.status_code, 200)

    def test_twit_listview(self):
        """Test twit listview"""
        self.client.force_login(self.user)
        response = self.client.get(reverse("twit_list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "twit_list.html")
        self.assertContains(response, "<hr>")
    
    def test_twit_detailview(self):
        """Test Twit Detailview"""
        self.client.force_login(self.user)
        response = self.client.get(reverse("twit_detail", kwargs={"pk": self.twit.pk}))
        no_response = self.client.get("/twits/1000000/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertTemplateUsed(response, "twit_detail.html")
        self.assertContains(response, '<hr>')

    def test_twit_updateview(self):
        """Test twit UpdateView"""
        self.client.force_login(self.user)
        response = self.client.post(
            reverse("twit_edit", args="1"),
            {
                "body": "Updated body",
            }
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Twit.objects.last().body, "Updated body")
    
    def test_twit_deleteview(self):
        """Test Twit Delete View"""
        response = self.client.post(reverse("twit_delete", args="1"))
        self.assertEqual(response.status_code, 302)