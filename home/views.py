from django.db.models import Count
from django.shortcuts import render
from bugs.models import Bug
from features.models import Feature
import json

# Create your views here.


def filter_by_status(issues, status):
    return [issue for issue in issues if issue.status == status]


def all_items(request):
    """A view that will display the index page including all bugs and features"""
    bugs = Bug.objects.all()
    features = Feature.objects.all()

    return render(request, 'index.html', {'bugs_created': filter_by_status(bugs, "CREATED"),
                                          'bugs_in_progress': filter_by_status(bugs, "IN PROGRESS"),
                                          'bugs_in_review': filter_by_status(bugs, "IN REVIEW"),
                                          'bugs_complete': filter_by_status(bugs, "COMPLETE"),
                                          'bugs_upvoted': Bug.objects.filter(upvoters__id=request.user.id),
                                          'features_created': filter_by_status(features, "CREATED"),
                                          'features_in_progress': filter_by_status(features, "IN PROGRESS"),
                                          'features_in_review': filter_by_status(features, "IN REVIEW"),
                                          'features_complete': filter_by_status(features, "COMPLETE")})


def about_us(request):
    """A view that will display the 'about us' page"""
    return render(request, 'about.html')


def charts(request):
    all_bugs = Bug.objects.all()
    created_bugs = len(filter_by_status(all_bugs, "CREATED"))
    in_progress_bugs = len(filter_by_status(all_bugs, "IN PROGRESS"))
    in_review_bugs = len(filter_by_status(all_bugs, "IN REVIEW"))
    completed_bugs = len(filter_by_status(all_bugs, "COMPLETE"))
    all_features = Feature.objects.all()
    created_features = len(filter_by_status(all_features, "CREATED"))
    in_progress_features = len(filter_by_status(all_features, "IN PROGRESS"))
    in_review_features = len(filter_by_status(all_features, "IN REVIEW"))
    completed_features = len(filter_by_status(all_features, "COMPLETE"))

    return render(request, 'charts.html', {'created_bugs': created_bugs,
                                           'in_progress_bugs': in_progress_bugs,
                                           'in_review_bugs': in_review_bugs,
                                           'completed_bugs': completed_bugs,
                                           'created_features': created_features,
                                           'in_progress_features': in_progress_features,
                                           'in_review_features': in_review_features,
                                           'completed_features': completed_features})



