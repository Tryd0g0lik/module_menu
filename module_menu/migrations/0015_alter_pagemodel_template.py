# Generated by Django 4.2.14 on 2024-10-06 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("module_menu", "0014_rename_menu_id_pagemodel_menu_list"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pagemodel",
            name="template",
            field=models.CharField(
                choices=[
                    ("index.html", "index"),
                    ("about/index.html", "about"),
                    ("account/index.html", "account"),
                    ("profile/index.html", "profile"),
                    ("404/index.html", "404"),
                ],
                default="404/index.html",
                help_text="\n            HTML-шаблон для контента страницы.\n            ",
                verbose_name="Выбрать шаблон для страницы",
            ),
        ),
    ]
