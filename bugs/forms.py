from django import forms
from .models import Bug


class BugForm(forms.ModelForm):

    class Meta:
        model = Bug
        exclude = ['username', 'status', 'date_added', 'date_started', 'date_finished', 'upvoters', 'views']

