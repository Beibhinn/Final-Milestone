from django import forms
from .models import Feature


class FeatureForm(forms.ModelForm):

    class Meta:
        model = Feature

        exclude = ('username', 'status', 'date_added', 'date_started', 'date_finished', 'donations', 'views')

    def __init__(self, request, username, files=None, instance=None):
        self.username = username
        super().__init__(request, files=files, instance=instance)

    def save(self, commit=True):
        feature = super().save(False)
        feature.username = self.username
        feature.save(commit)
        return feature

