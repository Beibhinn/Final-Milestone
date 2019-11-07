from django.test import TestCase, Client
from django.contrib.auth.models import User
from features.models import Feature
from django.conf import settings
from django.contrib import messages


class TestViews(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='john10',
                                        email='admin@admin.com')
        self.user.set_password('john10')
        self.user.save()

    def test_checkout_with_login_get(self):
        self.client.login(username='john10', password='john10')
        response = self.client.get("/checkout/", follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "checkout.html")

    def test_checkout_without_login_get(self):
        response = self.client.get("/checkout/", follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "login.html")

    def test_checkout_with_login_post(self):
        self.client.login(username='john10', password='john10')

        item = Feature(name="Test feature", description="description of my test feature", donations=30.00, username=self.user)
        item.save()
        # create shopping cart
        self.client.post("/cart/add/{0}".format(item.id),
                         data={'donation_amount': '6', 'user': self.user})

        stripe_id = 'tok_gb'

        response = self.client.post("/checkout/",
                                    {'user': self.user,
                                     'credit_card_number': '4242424242424242',
                                     'cvv': '123',
                                     'expiry_month': '10',
                                     'expiry_year': '2024',
                                     'stripe_id': stripe_id},
                                    follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "features.html")
        message = list(response.context.get('messages'))[0]
        self.assertEqual(message.tags, "success")
        self.assertEqual(message.message, "Thank you. You have successfully donated")

    def test_checkout_with_login_card_declined(self):
        self.client.login(username='john10', password='john10')

        item = Feature(name="Test feature", description="description of my test feature", donations=30.00, username=self.user)
        item.save()

        self.client.post("/cart/add/{0}".format(item.id),
                         data={'donation_amount': '12', 'user': self.user})

        stripe_id = 'tok_chargeDeclined'

        response = self.client.post("/checkout/",
                                    {'user': self.user,
                                     'credit_card_number': '4000000000000002',
                                     'cvv': '123',
                                     'expiry_month': '04',
                                     'expiry_year': '2024',
                                     'stripe_id': stripe_id})

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "checkout.html")
        message = list(response.context.get('messages'))[0]
        self.assertEqual(message.tags, "error")
        self.assertEqual(message.message, "Sorry, we were unable to take a payment with that card")
