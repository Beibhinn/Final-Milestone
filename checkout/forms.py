from django import forms
from .models import Donation


class MakePaymentForm(forms.Form):

    MONTH_CHOICES = [(i, i) for i in range(1, 12)]
    YEAR_CHOICES = [(i, i) for i in range(2020, 2099)]

    credit_card_number = forms.CharField(label='Credit card number', required=False)
    cvv = forms.CharField(label='Security code (CVV)', required=False)
    expiry_month = forms.ChoiceField(label='Month', choices=MONTH_CHOICES, required=False)
    expiry_year = forms.ChoiceField(label='Year', choices=YEAR_CHOICES, required=False)
    stripe_id = forms.CharField(widget=forms.HiddenInput)


class DonationForm(forms.ModelForm):

    class Meta:
        model = Donation
        exclude = (
            'user', 'date'
        )

    def __init__(self, request, user, date):
        self.user = user
        self.date = date
        super().__init__(request)

    def save(self, commit=True):
        donation = super(DonationForm, self).save(False)
        donation.user = self.user
        donation.date = self.date
        donation.save(commit)
        return donation
