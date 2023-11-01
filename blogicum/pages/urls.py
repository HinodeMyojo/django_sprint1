"""Calls the function corresponding to the query.

For example, if we have a request for the path <domain>/pages/rules
The urlpatterns variable will start the 'rules' function,
which is located in the 'views' file, assign name=rules to it.
"""

from django.urls import path

from . import views

app_name = 'pages'

urlpatterns = [
    path('about/', views.about, name='about'),
    path('rules/', views.rules, name='rules')
]
