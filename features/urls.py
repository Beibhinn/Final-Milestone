from django.conf.urls import url, include
from .views import all_features, feature_detail, add_or_edit_feature, FeatureDetailView

urlpatterns = [
    url(r'^$', all_features, name='features'),
    url(r'^(?P<pk>\d+)/$', feature_detail, name='feature_detail'),
    url((r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/'
         r'/$'),
        FeatureDetailView.as_view(),
        name='feature_detail'),
    url(r'^new/$', add_or_edit_feature, name='new_feature'),
]
