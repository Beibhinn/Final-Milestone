from django.shortcuts import render, get_object_or_404
from .models import Bug
from django.urls import reverse
from django.views.generic import DateDetailView


# Create your views here.


def all_bugs(request):
    """
    Creates a view that returns a list of all
    Bugs and renders them to the 'bugs.html' template
    """
    bugs = Bug.objects.all()
    return render(request, "bugs.html", {"bugs": bugs})


def bug_detail(request, pk):
    """
    Creates a view that returns a single
    Bug object based on the post ID (pk) and
    renders it to the 'bugdetail.html' template.
    Return 404 if not found
    """
    bug = get_object_or_404(Bug, pk=pk)
    bug.views += 1
    bug.save()
    return render(request, "bugdetail.html", {'bug': bug})


class BugDetailView(DateDetailView):
    model = Bug
    date_field = "date_added"
    month_format = "%m"

    def get_context_data(self, **kwargs):
        context = super(BugDetailView, self).get_context_data(**kwargs)
        context.update({'next': reverse('comments-xtd-sent')})
        return context