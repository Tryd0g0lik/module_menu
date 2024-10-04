"""File views.py from the django project"""

# from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet


class ModuleMenuViews(ModelViewSet):
    """Create your views here."""

    empty_var = ""


def get_index_page(request):
    pass
