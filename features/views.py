from django.shortcuts import render, get_object_or_404, redirect
from .models import Feature
from django.views.generic import DateDetailView
from .forms import FeatureForm

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
    Feature object based on the feature ID (pk) and
    renders it to the 'featuredetail.html' template.
    Return 404 if not found
    """
    feature = get_object_or_404(Feature, pk=pk)
    feature.views += 1
    feature.save()
    return render(request, "featuredetail.html", {'feature': feature})


class FeatureDetailView(DateDetailView):
    model = Feature
    date_field = "date_added"
    month_format = "%m"

    def get_context_data(self, **kwargs):
        context = super(FeatureDetailView, self).get_context_data(**kwargs)
        context.update({'next': reverse('comments-xtd-sent')})
        return context


def add_or_edit_feature(request, pk=None):
    """
    Create a view that allows to add
    or edit a feature depending if the feature ID
    is null or not
    """
    feature = get_object_or_404(Feature, pk=pk) if pk else None
    if request.method == "POST":
        form = FeatureForm(request.POST, request.user, files=request.FILES, instance=feature)
        if form.is_valid():
            feature = form.save()
            return redirect(feature_detail, feature.pk)
    else:
        form = FeatureForm(request.GET, request.user, files=None, instance=feature)
    return render(request, 'featureform.html', {'form': form})
