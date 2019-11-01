from django.contrib.auth.models import User
from django.test import TestCase
from .models import Bug

# Create your tests here.


class BugTests(TestCase):
    """
    Running a test against the Bug model
    """

    def test_str(self):
        test_username = User.objects.create_user(username="Mike")
        test_bug = Bug(name="Broken Link Bug",
                       description="Broken footer link",
                       username=test_username,
                       status="CREATED",
                       date_added="Oct. 28, 2017, 7:09 p.m",
                       views=0)
        self.assertEqual(str(test_bug.name), "Broken Link Bug")
        self.assertEqual(str(test_bug.description), "Broken footer link")
        self.assertEqual(str(test_bug.username), "Mike")
        self.assertEqual(str(test_bug.status), "CREATED")
        self.assertEqual(str(test_bug.date_added), "Oct. 28, 2017, 7:09 p.m")
        self.assertEqual(test_bug.views, 0)


