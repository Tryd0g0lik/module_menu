from django.contrib import admin

from module_menu.models import LinksMode, MenuNamesMode, SubLinksMode

# Register your models here.


#
# class LinksInLine(admin.TabularInline):
#     model = LinksMode
#     extra = 0

#
# class MenuNamesInLine(admin.TabularInline):
#     model = MenuNamesMode
#     extra = 0
#
#
# @admin.register(SubLinksMode)
# class SubLinksAdmin(admin.ModelAdmin):
#     fields = [
#         ("links_id"),
#         ("links", "active"),
#     ]
#     list_filter = []
#     list_display = [
#         "links_id",
#         "active",
#     ]
#
#
#     list_display_links = []
#     inlines = [MenuNamesInLine, LinksInLine]


class SubLinksInLine(admin.TabularInline):
    model = SubLinksMode
    extra = 0
# @admin.register(SubLinksMode)
# class SubLinksImLine(admin.ModelAdmin):
#     fields = [
#         ("links", "texts", "active"),
#         "name_id",
#         "links_id"
#     ]

# @admin.register(MenuNamesMode)
# class MenuNamesInLine(admin.ModelAdmin):
#     fields = [("names", "levels")]
#     list_display = ["names", "levels"]


@admin.register(LinksMode)
class LinksInLine(admin.ModelAdmin):
    fields = [("links", "texts", "active")]
    list_display = [
        "links", "texts", "active"
    ]
    list_filter = []

    inlines = [SubLinksInLine]
