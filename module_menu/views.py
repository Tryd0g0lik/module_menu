"""File views.py from the django project"""

from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from module_menu.models import PageModel, MenuNamesMode, SubLinksMode


class ModuleMenuViews(ModelViewSet):
    """Create your views here."""

    empty_var = ""


def get_index_page(request):
    """
    The choice of the template is autonomous, for the page
    :param request:
    :return:
    """
    content = []
    # Get one page
    page_list = []
    if len(request.path) == 1:
        page_list = PageModel.objects.filter(active=True).filter(links='index/')
    else:
        page_list = PageModel.objects.filter(active=True) \
            .filter(links=request.path[1:])
    if len(page_list) == 0:
        return render(
            request, template_name="404/index.html")
    # Get a list of menu indexes menu
    id_page_of_request = page_list[0].id
    menu_id_list_has_page = [sub_link.name_id.id for sub_link
                             in SubLinksMode.objects.all()
                             if sub_link.links_id.links.id
                             == id_page_of_request]
    # Get a unique list of indexes menu
    menu_id_list_has_page_unique = list(set(menu_id_list_has_page))
    references = \
        [
            [
                {"name_menu": obj.name_id.names, "links": obj} for obj
                in SubLinksMode.objects.all()
                if obj.name_id.id == index
            ] for index in menu_id_list_has_page_unique
        ]
    list_menu_all = SubLinksMode.objects.all()
    # The choice of the template is autonomous, for the page
    return render(request, template_name=page_list[0].template, context={"context":
        
        {"ind":page_list[0].id,
         "links":page_list[0].links, # The page's pathname
         "texts": page_list[0].texts}, # header
        "references":references
        })
