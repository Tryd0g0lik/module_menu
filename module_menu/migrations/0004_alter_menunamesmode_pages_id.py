# Generated by Django 4.2.14 on 2024-10-06 01:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("module_menu", "0003_alter_menunamesmode_pages_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="menunamesmode",
            name="pages_id",
            field=models.ForeignKey(
                blank=True,
                help_text="\n            Страница на которой будет опубликовано меню\n            ",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="pageыmenu",
                to="module_menu.pagemodel",
                verbose_name="Выбрать страницу",
            ),
        ),
    ]
