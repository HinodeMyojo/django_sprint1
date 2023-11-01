"""Page content display functions file."""

from django.shortcuts import render


def about(request):
    """Returns the contents of 'about.html' file."""
    templates = 'pages/about.html'
    return render(request, templates)


def rules(request):
    """Returns the contents of 'rules.html' file."""
    templates = 'pages/rules.html'
    return render(request, templates)

