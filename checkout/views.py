from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import MakePaymentForm, DonationForm
from .models import DonationLineItem
from django.conf import settings
from django.utils import timezone
from features.models import Feature
from datetime import datetime
import stripe

# Create your views here.
stripe.api_key = settings.STRIPE_SECRET


@login_required()
def checkout(request):
    """
        A view where payment information is taken and the donation
        amount is logged and added to the total donations for that
        feature
    """
    if request.method == "POST":
        donation_form = DonationForm(request.POST, request.user, datetime.now())
        payment_form = MakePaymentForm(request.POST)

        if donation_form.is_valid() and payment_form.is_valid():
            donation_details = donation_form.save(commit=False)
            donation_details.date = timezone.now()
            donation_details.save()

            cart = request.session.get('cart', {})
            total = 0
            for id, donation_amount in cart.items():
                feature = get_object_or_404(Feature, pk=id)
                total += donation_amount
                donation_line_item = DonationLineItem(
                    donation=donation_details,
                    feature=feature,
                    amount=donation_amount
                )
                donation_line_item.save()

            try:
                customer = stripe.Charge.create(
                    amount=int(total * 100),
                    currency="EUR",
                    description=request.user.email,
                    card=payment_form.cleaned_data['stripe_id']
                )
            except stripe.error.CardError:
                messages.error(request, "Sorry, looks like your card was declined.")

            if customer.paid:
                messages.success(request, "Thank you. You have successfully donated")
                for id, donation_amount in cart.items():
                    feature = get_object_or_404(Feature, pk=id)
                    feature.donations += donation_amount
                    feature.save()

                request.session['cart'] = {}
                return redirect(reverse('features'))
            else:
                messages.error(request, "We were unable to take payment. Please try again later")
        else:
            print(payment_form.errors)
            messages.error(request, "Sorry, we were unable to take a payment with that card")
    else:
        payment_form = MakePaymentForm()
        donation_form = DonationForm(request.GET, request.user, datetime.now())

    return render(request, "checkout.html",
                  {"donation_form": donation_form, "payment_form": payment_form, "publishable": settings.STRIPE_PUBLISHABLE})
