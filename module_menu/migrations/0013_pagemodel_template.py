# Generated by Django 4.2.14 on 2024-10-06 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("module_menu", "0012_alter_pagemodel_menu_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="pagemodel",
            name="template",
            field=models.CharField(
                choices=[
                    ("MAIN", "index"),
                    ("ABOUT", "about"),
                    ("ACCOUNT", "account"),
                    ("PROFILE", "profile"),
                    ("NOTPAGE", "404"),
                ],
                default="NOTPAGE",
                help_text="\n            HTML-шаблон для контента страницы.\n            ",
                verbose_name="Выбрать шаблон для страницы",
            ),
        ),
    ]
