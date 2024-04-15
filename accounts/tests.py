from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

# Benjamin Heerlyn
# CIS218
# 4/15/2024

class SignUpPageTest(TestCase):
    """Sign Up Page Test"""

    def test_url_exists_at_correct_location_signupview(self):
        """Test Url exists at correct location"""
        response = self.client.get("/accounts/signup/")
        self.assertEqual(response.status_code, 200)

    def test_signup_view_name(self):
        """Test Signup view name"""
        response = self.client.get(reverse("signup"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/signup.html")

    def test_signup_form(self):
        """Test SignUp form"""
        response = self.client.post(
            reverse("signup"),
            {
                "username": "Benjamin",
                "email": "bheerlyn3953@mail.kvcc.edu",
                "password1": "Benh2003",
                "password2": "Benh2003",
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, "Benjamin")
        self.assertEqual(get_user_model().objects.all()[0].email, "bheerlyn3953@mail.kvcc.edu")