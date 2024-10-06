# Generated by Django 4.2.14 on 2024-10-06 04:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("module_menu", "0009_pagemodel_active"),
    ]

    operations = [
        migrations.AlterField(
            model_name="sublinksmode",
            name="name_id",
            field=models.ForeignKey(
                db_column="name_id",
                help_text="\n            Меню в котором будет опубликована ссылка\n            ",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="linksmenu",
                to="module_menu.menunamesmode",
                unique=True,
                verbose_name="Выбрать меню",
            ),
        ),
    ]
