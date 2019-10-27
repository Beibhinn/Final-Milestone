from django.conf.urls import url, include
from .views import all_bugs, bug_detail

urlpatterns = [
    url(r'^$', all_bugs, name='bugs'),
    url(r'^(?P<pk>\d+)/$', bug_detail, name='bug_detail'),
]
