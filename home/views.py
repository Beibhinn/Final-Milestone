from django.shortcuts import render
from bugs.models import Bug
from features.models import Feature

# Create your views here.


def all_items(request):
    """A view that will display the index page"""
    bugs = Bug.objects.all()
    features = Feature.objects.all()

    def filter_by_status(issue, status):
        return [issue for issue in issue if issue.status == status]

    return render(request, 'index.html', {'bugs_created': filter_by_status(bugs, "CREATED"),
                                          'bugs_in_progress': filter_by_status(bugs, "IN PROGRESS"),
                                          'bugs_in_review': filter_by_status(bugs, "IN REVIEW"),
                                          'bugs_complete': filter_by_status(bugs, "COMPLETE"),
                                          'features_created': filter_by_status(features, "CREATED"),
                                          'features_in_progress': filter_by_status(features, "IN PROGRESS"),
                                          'features_in_review': filter_by_status(features, "IN REVIEW"),
                                          'features_complete': filter_by_status(features, "COMPLETE")})


