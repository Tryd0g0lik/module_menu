"""File router_menu.py from the django project"""

from django.urls import path


def empty():
    pass


urlpatterns = [
    path("about/<str:sign>", empty),
]
