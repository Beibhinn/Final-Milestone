from django import forms
from .models import Feature


class FeatureForm(forms.ModelForm):

    class Meta:
        model = Feature

        exclude = ('username', 'status', 'date_added', 'date_started', 'date_finished', 'donations', 'views')

