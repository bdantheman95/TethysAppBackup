from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from tethys_sdk.gizmos import Button

@login_required()
def home(request):
    """
    Controller for the app home page.
    """
    context = {}

    return render(request, 'arcgis/home.html', context)


def shortestroute(request):
    """
    Controller for the app home page.
    """
    context = {}

    return render(request, 'arcgis/shortestroute.html', context)


def areameasure(request):
    """
    Controller for the app home page.
    """
    context = {}

    return render(request, 'arcgis/areameasure.html', context)