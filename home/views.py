from django.shortcuts import render
from bugs.models import Bug
from features.models import Feature

# Create your views here.


def all_items(request):
    """A view that will display the index page"""
    bugs = Bug.objects.all()
    features = Feature.objects.all()

    return render(request, 'index.html', {'bugs': bugs,
                                          'features': features})
