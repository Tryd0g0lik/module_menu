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
    old_links_id = 9999999999999
    old_name_id = 9999999999999
    links_list = []
    # Получаем список references/links
    for ind in range(0, len(sub_links)):
        if sub_links[ind].links_id.active == False:
            continue
        # Проверяем наличие sub-links
        if sub_links[ind].texts != None:
            
            links_id = sub_links[ind].links_id.id
            name_id = sub_links[ind].name_id.id
            if old_links_id == links_id and old_name_id == name_id:
                links_list[-1]["sub"].append(
                    {"sub_texts": sub_links[ind].texts,
                     "sub_links": sub_links[ind].links}
                )
                old_links_id = links_id
                old_name_id = name_id
                continue
            else:
                links_list.append(
                    {
                        "texts": sub_links[ind].links_id.links.texts,
                        "links": sub_links[ind].links_id.links.links,
                        "sub": [
                            {"sub_texts": sub_links[ind].texts,
                             "sub_links": sub_links[ind].links}
                        ]
                    }
                )
                old_links_id = links_id
                old_name_id = name_id
        else:
            links_list.append({
                "texts": sub_links[ind].links_id.links.texts,
                "links": sub_links[ind].links_id.links.links,
                "sub": []
            })
    
    # Формируем HTML для меню с учетом уровня
    level_class = ""

    if menu.levels == "TOP":
        level_class = "top-menu"
    elif menu.levels == "SIDE":
        level_class = "side-menu"
    elif menu.levels == "FLOATER":
        level_class = "floater-menu"

    # Формируем HTML для меню
    menu_html = f'<div class="nav-item">' \
                f'<ul class="col nav justify-content-end border {level_class}">'

    for link in links_list:
        if len(link["sub"]) > 0:
            menu_html += f'<li class="dropdown nav-item">' \
                             f'<a href="{link["links"]}" ' \
                             f'class="nav-link dropdown" >' \
                             f'{link["texts"]}</a>' \
                             f'<div class="dropdown-memu">'
            for sub in link["sub"]:
                menu_html += \
                    f'<a href="{sub["sub_links"]} class="dropdown-item">' \
                    f'{sub["sub_texts"]}</a>'
            menu_html += f'</li>'
        else:
            menu_html += f'<li class="nav-item">' \
                         f'<a href="{link["links"]}" class="nav-link">' \
                         f'{link["texts"]}</a></li>'

    menu_html += "</ul></div>"
    # публикуем в качестве html
    return mark_safe(menu_html)
