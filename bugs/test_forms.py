from django.contrib.auth.models import User
from django.test import TestCase, Client

from .forms import BugForm


# Create your tests here.
class TestBugFormForm(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='admin',
                                        password='ThisPassword',
                                        is_superuser=True)

        self.client.login(username='admin', password='This Password')

    def test_can_add_bug(self):
        form = BugForm({'name': 'Unique Bug Name', 'description': 'I keep getting this bug'})
        self.assertTrue(form.is_valid())

    def test_cant_add_if_name_blank(self):
        form = BugForm({'name': '', 'description': 'This is my bug'})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['name'], [u'This field is required.'])

    def test_cant_add_if_description_blank(self):
        form = BugForm({'name': 'Another bug', 'description': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['description'], [u'This field is required.'])
