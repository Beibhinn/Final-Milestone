from django.contrib.auth.models import User
from django.test import TestCase
from django.utils import timezone

from .models import Feature


class TestFeaturesViews(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='Mary',
                                        email="Mary@example.com")
        self.user.set_password('thisPassword?')
        self.user.save()

        self.client.login(username='Mary', password='thisPassword?')

        self.feature = Feature.objects.create(name="Change profile pic feature",
                                              description="I want to pic my own profile pic",
                                              username=self.user,
                                              status="CREATED",
                                              donations=0,
                                              views=0)
        self.feature.save()

    def test_get_all_features(self):
        response = self.client.get("/features/")

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "features.html")

    def test_feature_detail(self):
        response = self.client.get("/features/{0}/".format(self.feature.id))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "featuredetail.html")
        self.assertIn("profile pic", str(response.content))

    def test_get_add_feature_page(self):
        response = self.client.get("/features/new/")

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "featureform.html")

    def test_post_add_feature_page(self):
        response = self.client.post("/features/new/",
                                    {"name": "Colored text",
                                     "description": "Colored text would be much cooler",
                                     "username": self.user,
                                     'status': "CREATED",
                                     "date_added": timezone.now,
                                     'donations': 0,
                                     'views': 0},
                                    follow=True)

        # check was redirected to the right page
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "featuredetail.html")

        # check feature was created successfully and details are as expected
        new_feature = Feature.objects.get(name="Colored text")
        self.assertIn(new_feature.description, "Colored text would be much cooler")
