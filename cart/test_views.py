from django.test import TestCase, Client
from django.contrib.auth.models import User
from features.models import Feature


class TestViews(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='Steve')
        self.user.set_password('password')
        self.user.save()

        self.client.login(username='Steve', password='password')

        self.feature = Feature.objects.create(name="Fun transitions", description="Transitions and animations", username=self.user)
        self.feature.save()

    def test_view_cart(self):
        response = self.client.get("/cart/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "cart.html")

    def test_add_to_cart(self):
        feature = self.feature
        response = self.client.post("/cart/add/{0}".format(feature.id), {
            "donation_amount": 7,
            "username": self.user
        }, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")

    def test_adjust_cart(self):
        feature = self.feature
        response = self.client.post("/cart/adjust/{0}".format(feature.id), {
            "donation_amount": 5,
            "username": self.user
        }, follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "cart.html")

    def test_remove_feature_from_cart(self):
        feature = self.feature
        session = self.client.session
        cart = session.get('cart', {})
        cart[feature.id] = cart.get(feature.id, 123)
        session['cart'] = cart
        session.save()

        response = self.client.post("/cart/remove/{0}".format(feature.id), follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "cart.html")
