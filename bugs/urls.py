from django.conf.urls import url, include
from .views import all_bugs, bug_detail, BugDetailView, add_or_edit_bug, update_status, toggle_upvote

urlpatterns = [
    url(r'^$', all_bugs, name='bugs'),
    url(r'^(?P<pk>\d+)/$', bug_detail, name='bug_detail'),
    url((r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/'
        r'/$'),
        BugDetailView.as_view(),
        name='bug_detail'),
    url(r'^new/$', add_or_edit_bug, name='new_bug'),
    url(r'^edit/(?P<pk>\d+)/$', add_or_edit_bug, name='edit_bug'),
    url(r'^update_status/$', update_status),
    url(r'^toggle_upvote/$', toggle_upvote)
]
