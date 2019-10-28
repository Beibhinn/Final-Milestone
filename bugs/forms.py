from django import forms
from .models import Bug


class BugForm(forms.ModelForm):

    class Meta:
        model = Bug
        exclude = ('username', 'status', 'date_added', 'date_started', 'date_finished', 'upvotes', 'views')

    def __init__(self, request, username, files=None, instance=None):
        self.username = username
        super().__init__(request, files=files, instance=instance)

    def save(self, commit=True):
        bug = super().save(False)
        bug.username = self.username
        bug.save(commit)
        return bug

