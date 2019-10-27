from django.shortcuts import render, get_object_or_404
from .models import Feature

# Create your views here.


def all_features(request):
    """
    Creates a view that returns a list of all
    Features and renders them to the 'features.html' template
    """
    features = Feature.objects.all()
    return render(request, "features.html", {"features": features})


def feature_detail(request, pk):
    """
    Creates a view that returns a single
    Feature object based on the post ID (pk) and
    renders it to the 'featuredetail.html' template.
    Return 404 if not found
    """
    feature = get_object_or_404(Feature, pk=pk)
    feature.views += 1
    feature.save()
    return render(request, "featuredetail.html", {'feature': feature})
