from django.contrib import admin
from module_menu.models import (SubLinksMode,
                                LinksMode,
                                MenuNamesMode)
# Register your models here.

#
# class LinksInLine(admin.TabularInline):
#     model = LinksMode
#     extra = 0
#
#
# class MenuNamesInLine(admin.TabularInline):
#     model = MenuNamesMode
#     extra = 0


# @admin.register(SubLinksMode)
# class SubLinksAdmin(admin.ModelAdmin):
#     fields = [
#         ("name_id", "links_id"),
#         ("links", "text", "active"),
#     ]
#     list_filter = []
#     list_display = [
#         "name_id",
#         "links_id",
#          "active",
#     ]
#     list_display_links = []
#     inlines = [MenuNamesInLine, LinksInLine]

# class SubLinksInLine(admin.TabularInline):
#     model = SubLinksMode
#     extra = 0

@admin.register(MenuNamesMode)
class MenuNamesInLine(admin.ModelAdmin):
    fields = [
        ("links", "text", "active"),
    ]
    list_display = [
        # "links", "text", "active"
    ]
    # inlines = [SubLinksInLine]