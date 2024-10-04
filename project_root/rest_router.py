"""This is a router of module-menu"""

from rest_framework.routers import DefaultRouter

from module_menu.views import ModuleMenuViews

router = DefaultRouter()
router.register("modulemenu", ModuleMenuViews, basename="register")
