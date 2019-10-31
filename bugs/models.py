from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class Bug(models.Model):
    name = models.CharField(max_length=150, blank=False)
    description = models.TextField(blank=False)
    image = models.ImageField(upload_to='images', blank=True)
    username = models.ForeignKey(User)
    STATUS_CHOICES = (
        ('CREATED', 'Created'),
        ('IN PROGRESS', 'In progress'),
        ('IN REVIEW', 'In review'),
        ('COMPLETE', 'Complete')
    )
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default='CREATED')
    date_added = models.DateTimeField(
        blank=False, default=timezone.now, null=False)
    date_started = models.DateTimeField(
        blank=True, default=None, null=True)
    date_finished = models.DateTimeField(
        blank=True, default=None, null=True)
    upvoters = models.ManyToManyField(User, related_name='upvoters')
    views = models.IntegerField(default=0)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.upvotes = self.upvoters.count()

    # @property
    # def upvotes(self):
    #     return self.upvoters.count()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse(
            'bug_detail',
            kwargs={'year': self.date_added.year,
                    'month': int(self.date_added.strftime('%m').lower()),
                    'day': self.date_added.day})
