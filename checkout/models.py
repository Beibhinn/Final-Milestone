from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from features.models import Feature


# Create your models here.


class Donation(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateField()

    def __str__(self):
        return "{0}-{1}-{2}".format(self.id, self.date, self.user)


class DonationLineItem(models.Model):
    donation = models.ForeignKey(Donation, null=False)
    feature = models.ForeignKey(Feature, null=False)
    amount = models.IntegerField(blank=False)

    def __str__(self):
        return "{0} {1} @ {2}".format(
            self.feature, self.feature.name, self.feature.amount)
