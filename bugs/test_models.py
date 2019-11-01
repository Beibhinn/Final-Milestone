from django.test import TestCase, Client
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.utils import timezone
from .models import Bug


class TestBugModels(TestCase):
    def test_bug_form(self):
        self.user = User.objects.create(username='admin',
                                        password='ThisPassword',
                                        is_superuser=True)
        self.user.save()

        bug = Bug.objects.create(name="I get an error saying 404?",
                                 description="Every time I try to access the page",
                                 username=self.user,)
        bug.save()

        self.assertEqual(str(bug.name), "I get an error saying 404?")
        self.assertEqual(str(bug.description), "Every time I try to access the page")
        self.assertEqual(str(bug.username), "admin")
        self.assertEqual(str(bug.status), "CREATED")
        self.assertEqual(bug.views, 0)

