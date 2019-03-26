from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from tethys_sdk.gizmos import Button

@login_required()
def home(request):
    """
    Controller for the app home page.
    """
    context = {}

    return render(request, 'brandon_design/home.html', context)


def example(request):
    """
    Controller for the app home page.
    """
    context = {}

    return render(request, 'brandon_design/example.html', context)


def mockup(request):
    """
    Controller for the app home page.
    """
    context = {}

    return render(request, 'brandon_design/mockup.html', context)


def proposal(request):
    """
    Controller for the app home page.
    """
    context = {}

    return render(request, 'brandon_design/proposal.html', context)
