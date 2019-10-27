from django.conf.urls import url, include
from .views import all_bugs, bug_detail, BugDetailView

urlpatterns = [
    url(r'^$', all_bugs, name='bugs'),
    url(r'^(?P<pk>\d+)/$', bug_detail, name='bug_detail'),
    url((r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/'
        r'/$'),
        BugDetailView.as_view(),
        name='bug_detail')
]
