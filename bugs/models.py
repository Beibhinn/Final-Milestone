from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class Bug(models.Model):
    name = models.CharField(max_length=150, blank=False)
    description = models.TextField(blank=False)
    image = models.ImageField(upload_to='images')
    username = models.ForeignKey(User, default=None)
    STATUS_CHOICES = (
        ('CREATED', 'Created'),
        ('IN PROGRESS', 'In progress'),
        ('IN REVIEW', 'In review'),
        ('COMPLETE', 'Complete')
    )
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default='CREATED')
    date_added = models.DateTimeField(
        blank=True, default=timezone.now, null=True)
    date_started = models.DateTimeField(
        blank=True, default=None, null=True)
    date_finished = models.DateTimeField(
        blank=True, default=None, null=True)
    upvotes = models.IntegerField(default=0)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.name
