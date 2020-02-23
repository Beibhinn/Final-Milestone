from django.contrib.auth.models import User
from django.contrib import auth
from django.test import TestCase
from django.utils import timezone

from .models import Feature


class TestFeaturesViews(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='Mary',
                                        email="Mary@example.com")
        self.user.set_password('thisPassword?')
        self.user.save()

        self.user = User.objects.create(username='admin',
                                        is_staff=True,
                                        is_superuser=True)

        self.user.set_password('password')
        self.user.save()

        self.client.login(username='Mary', password='thisPassword?')

        self.feature = Feature.objects.create(name="Change profile pic feature",
                                              description="I want to pick my own profile pic",
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

    def test_user_cannot_edit_other_user_feature(self):
        user = User.objects.create(username="Joe",
                                   is_superuser=False)
        user.set_password("Password")
        user.save()

        feature = Feature.objects.create(name="Add GPS",
                                         description="GPS and maps and stuff",
                                         username=User.objects.get(username="Mary"))
        feature.save()

        self.client.logout()
        self.client.login(username="Joe", password="Password")
        response = self.client.get("/features/edit/{0}/".format(feature.id))
        self.assertEqual(response.status_code, 403)

    def test_user_can_edit_own_feature(self):
        feature = Feature.objects.create(name="Mary's Feature idea",
                                         description="My contribution",
                                         username=User.objects.get(username="Mary"))
        feature.save()

        self.client.logout()
        self.client.login(username="Mary", password="thisPassword?")
        response = self.client.get("/features/edit/{0}/".format(feature.id))
        self.assertEqual(feature.username, auth.get_user(self.client))
        self.assertEqual(response.status_code, 200)

        edit = self.client.post("/features/edit/{0}/".format(feature.id),
                                {"name": "Mary's edited feature",
                                 "description": "A better contribution",
                                 "username": "Mary"},
                                follow=True)

        # check was redirected to the right page
        self.assertEqual(edit.status_code, 200)
        self.assertTemplateUsed(edit, "featuredetail.html")

        # check feature was edited successfully and details are as expected
        edited_feature = Feature.objects.get(name="Mary's edited feature")
        self.assertEqual(edited_feature.description, "A better contribution")

    def test_admin_can_edit_other_user_feature(self):
        self.client.login(username='admin', password="password")
        loggedin = auth.get_user(self.client)
        print(loggedin)
        response = self.client.get("/features/edit/{0}/".format(self.feature.id))
        self.assertEqual(response.status_code, 200)

        edit = self.client.post("/features/edit/{0}/".format(self.feature.id),
                                {"name": "Change profile pic feature & add filters",
                                 "description": "I want to pick my own profile pic and have filters like instagram",
                                 "username": "Maary"},
                                follow=True)

        # check was redirected to the right page
        self.assertEqual(edit.status_code, 200)
        self.assertTemplateUsed(edit, "featuredetail.html")

        # check no feature exists with the original name
        try:
            original_feature = Feature.objects.get(name="Change profile pic feature")
        except Feature.DoesNotExist:
            original_feature = None
        self.assertIsNone(original_feature)

        # check feature exists with new name and details are as expected
        edited_feature = Feature.objects.get(name="Change profile pic feature & add filters")
        self.assertEqual(edited_feature.description, "I want to pick my own profile pic and have filters like instagram")
