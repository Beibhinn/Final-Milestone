from django.shortcuts import render
from bugs.models import Bug
from features.models import Feature
from django.db.models import Q

# Create your views here.


def search_issues(request):
    """
       A view that displays all bugs and features that match the users
       search term(s)
     """
    bugs = Bug.objects.filter(
        Q(name__icontains=request.GET['search_term']) | Q(description__icontains=request.GET['search_term']))
    features = Feature.objects.filter(
        Q(name__icontains=request.GET['search_term']) | Q(description__icontains=request.GET['search_term']))
    search_term = request.GET['search_term']

    return render(request, "searchresults.html", {"bugs": bugs,
                                                  "features": features,
                                                  "search_term": search_term,
                                                  "bugs_upvoted": Bug.objects.filter(upvoters__id=request.user.id)})

