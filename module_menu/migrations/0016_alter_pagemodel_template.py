# Generated by Django 4.2.14 on 2024-10-06 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("module_menu", "0015_alter_pagemodel_template"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pagemodel",
            name="template",
            field=models.CharField(
                choices=[
                    ("index", "Главная"),
                    ("about", "О нас"),
                    ("account", "Аккаунт"),
                    ("profile", "Профиль"),
                    ("NOTPAGE", "Страница не найдена"),
                ],
                default="NOTPAGE",
                help_text="\n            HTML-шаблон для контента страницы.\n            ",
                verbose_name="Выбрать шаблон для страницы",
            ),
        ),
    ]
