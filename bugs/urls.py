from django.conf.urls import url, include
from .views import all_bugs

urlpatterns = [
    url(r'^$', all_bugs, name='bugs'),
]