from django.contrib.auth.models import User
from django.test import TestCase
from .models import Feature


# Create your tests here.
class FeatureTests(TestCase):
    """
    Running a test against the Feature model
    """

    def test_str(self):
        test_username = User.objects.create_user(username="Steve", email="steve@example.com")

        test_feature = Feature(name="New animations",
                               description="I want new animations please",
                               username=test_username,
                               status="CREATED",
                               date_added="Oct. 01, 1998, 6:42 a.m",
                               donations=0,
                               views=0)
        self.assertEqual(str(test_feature.name), "New animations")
        self.assertEqual(str(test_feature.description), "I want new animations please")
        self.assertEqual(str(test_feature.username), "Steve")
        self.assertEqual(str(test_feature.status), "CREATED")
        self.assertEqual(str(test_feature.date_added), "Oct. 01, 1998, 6:42 a.m")
        self.assertEqual(test_feature.donations, 0)
        self.assertEqual(test_feature.views, 0)

