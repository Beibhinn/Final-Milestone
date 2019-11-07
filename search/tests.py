from django.test import TestCase
from django.shortcuts import render
from bugs.models import Bug
from features.models import Feature
from django.db.models import Q

# Create your tests here.

class SearchTests(TestCase):
    def do_search(self):
        self.bug = Bug.objects.create(name="Broken Link Bug",
                                      description="Broken footer link",
                                      username=self.user,
                                      status="CREATED",
                                      views=0)
        self.bug.save()
        self.feature = Feature.objects.create(name="Add new links",
                                              description="Add a new link or two",
                                              username=self.user,
                                              status="CREATED",
                                              views=0)
        self.feature.save()
        search_term = "link"
        response = self.client.get("/search/")

        self.assertContains(response, "link")
        self.assertIn("Add a new link or two", str(response.content))
        self.assertIn("Broken link bug", str(response.content))

