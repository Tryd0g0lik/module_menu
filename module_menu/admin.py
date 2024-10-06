from django.contrib import admin

from module_menu.models import (LinksMode, MenuNamesMode, PageModel,
                                SubLinksMode)

# Register your models here.


class SubLinksInLine(admin.TabularInline):
    model = SubLinksMode
    extra = 0


class MenuNamesInLine(admin.TabularInline):
    model = MenuNamesMode
    extra = 0


@admin.register(PageModel)
class PageAdmin(admin.ModelAdmin):
    fields = [("links", "texts","active", "template"),  "menu_list"]
    list_display = ["links", "texts"]
    # inlines = [MenuNamesInLine]


@admin.register(LinksMode)
class LinksAdmin(admin.ModelAdmin):
    fields = [("links", "texts", "active")]
    list_display = ["links", "texts", "active"]
    list_filter = []

    inlines = [SubLinksInLine]


@admin.register(MenuNamesMode)
class MenuNamesAdmin(admin.ModelAdmin):
    fields = ["names"]
    list_display = ["names"]
    list_filter = []
