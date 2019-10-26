from django.conf.urls import url, include
from .views import all_features

urlpatterns = [
    url(r'^$', all_features, name='features'),
]
