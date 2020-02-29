import json

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from .models import Bug
from django.urls import reverse
from django.views.generic import DateDetailView
from django.http import HttpResponse, HttpResponseNotAllowed
from .forms import BugForm


# Create your views here.


def all_bugs(request):
    """
    Creates a view that returns a list of all
    Bugs and renders them to the 'bugs.html' template
    """
    bugs = Bug.objects.all()
    return render(request, "bugs.html", {"bugs": bugs,
                                         "bugs_upvoted": Bug.objects.filter(upvoters__id=request.user.id)})


def bug_detail(request, pk):
    """
    Creates a view that returns a single
    Bug object based on the bug ID (pk) and
    renders it to the 'bugdetail.html' template.
    Return 404 if not found
    """
    bug = get_object_or_404(Bug, pk=pk)
    bug.views += 1
    bug.save()
    return render(request, "bugdetail.html", {"bug": bug,
                                              "bugs_upvoted": Bug.objects.filter(upvoters__id=request.user.id)})


class BugDetailView(DateDetailView):
    model = Bug
    date_field = "date_added"
    month_format = "%m"

    def get_context_data(self, **kwargs):
        context = super(BugDetailView, self).get_context_data(**kwargs)
        context.update({'next': reverse('comments-xtd-sent')})
        return context


@login_required()
def add_or_edit_bug(request, pk=None):
    """
    Create a view that allows a user to add
    or edit a bug depending if the Bug ID
    is null or not. A user should only be able
    to edit a bug if they created it, or if they
    are staff
    """
    bug = get_object_or_404(Bug, pk=pk) if pk else None
    print(bug)
    if request.method == "POST":
        form = BugForm(request.POST, request.FILES, instance=bug)
        if form.is_valid():
            if bug is None:
                bug = form.save(commit=False)
                bug.username = request.user
                bug.save()
                return redirect(bug_detail, bug.pk)
            else:
                if request.user.is_staff or request.user == bug.username:
                    bug = form.save(commit=False)
                    bug.save()
                    return redirect(bug_detail, bug.pk)
                else:
                    return HttpResponse(status=403)
    else:
        if bug is None or request.user.is_staff or request.user == bug.username:
            form = BugForm(instance=bug)
        else:
            return HttpResponse(status=403)

    return render(request, 'bugform.html', {'form': form})


def update_status(request):
    """
    Create a view that allows a user to update the status of an issue
    """
    if request.method == "POST":
        data = json.loads(request.body)
        # print('ID ', data['id'])
        # print('STATUS ', data['status'])

        # Get the Bug with this id
        bug = get_object_or_404(Bug, pk=data['id'])
        # Check if the status is different
        if bug.status == data['status']:
            print('they are the same')
            return HttpResponse(status=204)

        if data['status'] == 'IN PROGRESS':
            if bug.date_started is None:
                bug.date_started = timezone.now()

        elif data['status'] == 'COMPLETE':
            bug.date_finished = timezone.now()

        elif bug.status == 'COMPLETE':
            bug.date_finished = None

        bug.status = data['status']
        # Save the bug with the new status
        bug.save()
        return HttpResponse(status=204)
    else:
        return HttpResponseNotAllowed(["POST"])


def toggle_upvote(request):
    """
        Create a view that allows a user to toggle
        whether they have upvoted a bug or not. They get
        added or removed to the list of upvoters for a bug
    """
    if request.method == "POST":
        data = json.loads(request.body)

        # Get the Bug with this id
        bug = get_object_or_404(Bug, pk=data['id'])

        if bug.upvoters.all().filter(id__exact=request.user.id).first() is None:
            bug.upvoters.add(request.user)
            print('Added ', request.user)
        else:
            bug.upvoters.remove(request.user)
            print('Removed ', request.user)

        bug.save()
        return HttpResponse(status=204)
    else:
        return HttpResponseNotAllowed(["POST"])
