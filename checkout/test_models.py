from django.test import TestCase
from django.contrib.auth.models import User

from .models import Donation, DonationLineItem, Feature


class TestOrderModel(TestCase):
    def test_donation(self):
        user = User.objects.create(username="admin",
                                   password="ThisPassword",
                                   is_superuser=True)
        user.save()
        donation = Donation.objects.create(user=user)
        admin = User.objects.get(username="admin")
        self.assertEqual(donation.user, admin)

    def test_donation_line_item(self):
        user = User.objects.create(username="admin",
                                   password="ThisPassword",
                                   is_superuser=True)
        user.save()
        print(user)
        print(type(user))
        donation = Donation.objects.create(user=user)
        feature = Feature(name="Add animations",
                          description="animations make it look nice ",
                          status="CREATED")
        donationitem = DonationLineItem(donation=donation, feature=feature, amount=8)
        self.assertEqual(donationitem.amount, 8)

