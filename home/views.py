from django.shortcuts import render

# Create your views here.


def index(request):
    """A view that will display the index page"""
    return render(request, 'index.html')
