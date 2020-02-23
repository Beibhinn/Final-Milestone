from django.contrib.auth.models import User
from django.contrib import auth
from django.test import TestCase
from django.utils import timezone

from .models import Bug


class TestBugsViews(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='admin',
                                        is_staff=True,
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

    def test_user_cannot_edit_other_user_bug(self):
        user = User.objects.create(username="Joe",
                                   is_superuser=False)

        user.set_password("ThisPassword")

        user.save()

        author = User.objects.create(username="Ben",
                                     is_superuser=False)
        author.save()

        bug = Bug.objects.create(name="Broken link",
                                 description="Link not working",
                                 username=author)
        bug.save()

        self.client.logout()
        self.client.login(username="Joe", password="ThisPassword")
        response = self.client.get("/bugs/edit/{0}/".format(bug.id))
        self.assertEqual(response.status_code, 403)

    def test_user_can_edit_own_bug(self):
        author = User.objects.create(username="Joe",
                                     is_superuser=False)

        author.set_password("ThisPassword")

        author.save()

        bug = Bug.objects.create(name="Joe's Bug",
                                 description="Just wanted to be part of something",
                                 username=author)
        bug.save()

        self.client.logout()
        self.client.login(username="Joe", password="ThisPassword")
        response = self.client.get("/bugs/edit/{0}/".format(bug.id))
        self.assertEqual(bug.username, author)
        self.assertEqual(response.status_code, 200)

        edit = self.client.post("/bugs/edit/{0}/".format(bug.id),
                                {"name": "The bug of Joe",
                                 "description": "Please accept my bug",
                                 "username": "Joe"},
                                follow=True)

        # check was redirected to the right page
        self.assertEqual(edit.status_code, 200)
        self.assertTemplateUsed(edit, "bugdetail.html")

        # check bug was edited successfully and details are as expected
        edited_bug = Bug.objects.get(name="The bug of Joe")
        self.assertEqual(edited_bug.description, "Please accept my bug")

    def test_admin_can_edit_other_user_bug(self):
        author = User.objects.create(username="Joe",
                                     is_superuser=False)
        author.save()

        bug = Bug.objects.create(name="Joe's Bug",
                                 description="Just wanted to be part of something",
                                 username=author)
        bug.save()

        loggedin = auth.get_user(self.client)
        print(loggedin)
        response = self.client.get("/bugs/edit/{0}/".format(bug.id))
        self.assertEqual(response.status_code, 200)

        edit = self.client.post("/bugs/edit/{0}/".format(bug.id),
                                {"name": "Technically Joe's bug",
                                 "description": "This bug is now a collaboration between Joe and admin",
                                 "username": "Joe"},
                                follow=True)

        # check was redirected to the right page
        self.assertEqual(edit.status_code, 200)
        self.assertTemplateUsed(edit, "bugdetail.html")

        # check no bug exists with the original name
        try:
            original_bug = Bug.objects.get(name="The bug of Joe")
        except Bug.DoesNotExist:
            original_bug = None
        self.assertIsNone(original_bug)

        # check bug exists with new name and details are as expected
        edited_bug = Bug.objects.get(name="Technically Joe's bug")
        self.assertEqual(edited_bug.description, "This bug is now a collaboration between Joe and admin")
