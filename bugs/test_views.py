from django.contrib.auth.models import User
from django.test import TestCase
from django.utils import timezone

from .models import Bug


class TestBugsViews(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='admin',
                                        is_superuser=True)

        self.user.set_password('password')

        self.user.save()

        self.client.login(username='admin', password='password')

        self.bug = Bug.objects.create(name="Broken Link Bug",
                                      description="Broken footer link",
                                      username=self.user,
                                      status="CREATED",
                                      views=0)
        self.bug.save()

    def test_get_all_bugs(self):
        response = self.client.get("/bugs/")

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "bugs.html")

    def test_bug_detail(self):
        response = self.client.get("/bugs/{0}/".format(self.bug.id))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "bugdetail.html")
        self.assertIn("Broken Link Bug", str(response.content))

    def test_get_add_bug_page(self):
        response = self.client.get("/bugs/new/")

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "bugform.html")

    def test_post_add_bug_page(self):
        response = self.client.post("/bugs/new/",
                                    {"name": "I get an error saying 404?",
                                     "description": "Every time I try to access the page",
                                     "username": self.user,
                                     'status': "CREATED",
                                     "date_added": timezone.now,
                                     'upvoters': 0,
                                     'views': 0},
                                    follow=True)

        # check was redirected to the right page
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "bugdetail.html")

        # check bug was created successfully and details are as expected
        new_bug = Bug.objects.get(name="I get an error saying 404?")
        self.assertIn(new_bug.description, "Every time I try to access the page")
