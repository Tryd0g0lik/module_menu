"""File views.py from the django project"""

from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from module_menu.models import PageModel, SubLinksMode


class ModuleMenuViews(ModelViewSet):
    """Create your views here."""

    empty_var = ""


def get_index_page(request):
    content = []
    page_list = PageModel.objects.filter(active=True) \
     .filter(links=request.path)
    if len(page_list) == 0:
        return render(
            request, template_name="404.html")
    
    return render(request, template_name="index.html", context=[
            page_list
        ])
