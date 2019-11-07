from django.contrib.auth.models import User
from django.test import TestCase

from .models import Feature


class TestBugModels(TestCase):
    def test_bug_form(self):
        self.user = User.objects.create(username="Mike",
                                        password="MyPassword",
                                        is_superuser=True)
        self.user.save()

        feature = Feature.objects.create(name="Custom cursors",
                                         description="I want to be able to choose my own cursor",
                                         username=self.user)
        feature.save()

        self.assertEqual(str(feature.name), "Custom cursors")
        self.assertEqual(str(feature.description), "I want to be able to choose my own cursor")
        self.assertEqual(str(feature.username), "Mike")
        self.assertEqual(str(feature.status), "CREATED")
        self.assertEqual(feature.donations, 0)
        self.assertEqual(feature.views, 0)

