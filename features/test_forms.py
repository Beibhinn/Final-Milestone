from django.contrib.auth.models import User
from django.test import TestCase

from .forms import FeatureForm


# Create your tests here.
class TestFeatureFormForm(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='Mary',
                                        password='ThisPassword',
                                        is_superuser=True)
        self.user.save()

        self.client.login(username='Mary', password='This Password')

    def test_can_add_feature(self):
        form = FeatureForm({'name': 'Unique Feature Name', 'description': 'This is my feature idea'})
        self.assertTrue(form.is_valid())

    def test_cant_add_if_name_blank(self):
        form = FeatureForm({'name': '', 'description': 'This is my feature idea'})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['name'], [u'This field is required.'])

    def test_cant_add_if_description_blank(self):
        form = FeatureForm({'name': 'A feature', 'description': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['description'], [u'This field is required.'])
