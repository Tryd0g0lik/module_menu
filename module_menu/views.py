"""File views.py from the django project"""

from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from module_menu.models import PageModel


class ModuleMenuViews(ModelViewSet):
    """Create your views here."""

    empty_var = ""


def get_index_page(request):
    page_list = PageModel.progect.all()
    return render(request, template_name="index.html")
