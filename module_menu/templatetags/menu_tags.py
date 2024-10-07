from django import template
from django.utils.safestring import mark_safe

from module_menu.models import MenuNamesMode, SubLinksMode

register = template.Library()


@register.simple_tag
def draw_menu(levels):
    menu_name = "TOP"
    if levels == "Боковое":
        menu_name = "SIDE"
    elif levels == "Нижнее":
        menu_name = "FLOATER"
    # Получаем меню по имени
    menu = MenuNamesMode.objects.filter(levels=menu_name).first()

    # Если меню не найдено, возвращаем пустую строку
    if not menu:
        return ""

    # Получаем подменю для данного меню
    sub_links = SubLinksMode.objects.filter(name_id=menu)

    # Формируем HTML для меню с учетом уровня
    level_class = ""

    if menu.levels == "TOP":
        level_class = "top-menu"
    elif menu.levels == "SIDE":
        level_class = "side-menu"
    elif menu.levels == "FLOATER":
        level_class = "floater-menu"

    # Формируем HTML для меню
    menu_html = f'<ul class="col nav justify-content-end border {level_class}">'

    for link in sub_links:

        if link.texts != None:
            menu_html += f'<li class="nav-item"><a href="{link.links}" ' \
                         f'class="nav-link" >{link.texts}</a></li>'

    menu_html += "</ul>"
    # публикуем в качестве html
    return mark_safe(menu_html)
