# Generated by Django 4.2.14 on 2024-10-05 03:52

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="LinksMode",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "links",
                    models.CharField(
                        blank=True,
                        help_text="/ваш/маршрут/на/внутреннюю/страницу/сайта/",
                        max_length=100,
                        null=True,
                        validators=[
                            django.core.validators.MaxLengthValidator(
                                limit_value=100,
                                message="Максимальная длина 100 символов",
                            ),
                            django.core.validators.RegexValidator(
                                message="Неверный формат ссылки.",
                                regex="^(?!.*  )[a-z][\\w\\-_\\d]{1,98}\\/$[^\\S\\W \\\\]?",
                            ),
                        ],
                        verbose_name="Маршрут",
                    ),
                ),
                (
                    "texts",
                    models.CharField(
                        max_length=50,
                        unique=True,
                        validators=[
                            django.core.validators.MaxLengthValidator(
                                limit_value=50,
                                message="Максимальная длина\n                               50 символов",
                            ),
                            django.core.validators.RegexValidator(
                                message="Текст может содержать только английские и\n                    русские буквы, цифры и пробелы.",
                                regex="^[\\w\\sа-яА-ЯёЁ]+$",
                            ),
                        ],
                    ),
                ),
            ],
            options={
                "verbose_name": "Ссылка в меню",
                "verbose_name_plural": "Ссылки в меню",
            },
        ),
        migrations.CreateModel(
            name="MenuNamesMode",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "names",
                    models.CharField(
                        help_text="Имя (максимальная длина 30символов) для вашего меню,\n        чтоб ориентироваться в панели для администратора",
                        max_length=30,
                        unique=True,
                        validators=[
                            django.core.validators.MaxLengthValidator(
                                limit_value=30, message="Максимальная длина 30 символов"
                            ),
                            django.core.validators.RegexValidator(
                                message="\n                Название не должно иметь двух пробелов подряд,\n                символов не принадлежащих к алфавиту и(или) цифрам.\n                Начинается из любой буквы. Заканчивается из любой буквы и\n                цифры.\n                Допускается дефис и(или) нижнее подчёркивание\n                ",
                                regex="^(?!.*  )[a-zA-Z][\\w \\-_\\d]{1,28}[a-zA-Z0-9]$[^\\S\\W \\\\]?",
                            ),
                        ],
                        verbose_name="Название меню",
                    ),
                ),
                (
                    "levels",
                    models.CharField(
                        choices=[("TOP", "Главное"), ("SIDE", "Боковое")],
                        default="TOP",
                        help_text="Уровень может быть\n        главным ('top'), боковым ('side')",
                        verbose_name="Уровень меню",
                    ),
                ),
            ],
            options={
                "verbose_name": "Заголовок меню",
                "verbose_name_plural": "Заголовки в меню",
            },
        ),
        migrations.CreateModel(
            name="SubLinksMode",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "links",
                    models.CharField(
                        blank=True,
                        help_text="/ваш/маршрут/на/внутреннюю/страницу/сайта/",
                        max_length=100,
                        null=True,
                        validators=[
                            django.core.validators.MaxLengthValidator(
                                limit_value=100,
                                message="Максимальная длина 100 символов",
                            ),
                            django.core.validators.RegexValidator(
                                message="Неверный формат ссылки.",
                                regex="^(?!.*  )[a-z][\\w\\-_\\d]{1,98}\\/$[^\\S\\W \\\\]?",
                            ),
                        ],
                        verbose_name="Маршрут",
                    ),
                ),
                (
                    "texts",
                    models.CharField(
                        blank=True,
                        help_text="Заголовок пункта меню (ссылки)",
                        max_length=50,
                        null=True,
                        validators=[
                            django.core.validators.MaxLengthValidator(
                                limit_value=50, message="Максимальная длина 30 символов"
                            ),
                            django.core.validators.RegexValidator(
                                message="\n                    Название не должно иметь двух пробелов подряд,\n                    символов не принадлежащих к алфавиту и(или) цифрам.\n                    Начинается из любой буквы. Заканчивается из любой буквы и\n                    цифры.\n                    Допускается дефис и(или) нижнее подчёркивание\n                    ",
                                regex="^(?!.*  )[a-zA-Z][\\w \\-_\\d]{1,28}[a-zA-Z0-9]$[^\\S\\W \\\\]?",
                            ),
                        ],
                        verbose_name="Заголовок ссылки",
                    ),
                ),
                (
                    "active",
                    models.BooleanField(
                        help_text="\n        Активное или не активное меню на странице сайта\n        ",
                        verbose_name="Активное или не активное",
                    ),
                ),
                (
                    "links_id",
                    models.ForeignKey(
                        db_column="links_id",
                        help_text="\n                                    Пункт меню (ссылка) в который будет\n                                     опубликован в меню\n                                    ",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="linksmenu",
                        to="module_menu.linksmode",
                        verbose_name="Выбрать пункт для меню",
                    ),
                ),
            ],
            options={
                "verbose_name": "Ссылка в под-меню",
                "verbose_name_plural": "Ссылки в под-меню",
            },
        ),
    ]
