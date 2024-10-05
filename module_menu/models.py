from django.core.cache import cache
from django.core.validators import MaxLengthValidator, RegexValidator
# validate_slug, validate_unicode_slug)
from django.db import models
from django.utils.translation import gettext_lazy as _

cache.clear()


# Create your models here.
class BaseLinkModel(models.Model):
    """
    This is a basis model. It is abstract model and do war with duplicate.
    'links' is reference of the '<a href="<your_refer>">'.
    'texts' is text of the '<a >Your text</a>'.
    """

    links = models.CharField(
        max_length=100,
        help_text=_("/ваш/маршрут/на/внутреннюю/страницу/сайта/"),
        validators=[
            MaxLengthValidator(
                limit_value=100, message=_("""Максимальная длина 100 символов""")
            ),
            RegexValidator(
                regex=r"^(?!.*  )[a-z][\w\-_\d]{1,98}\/$[^\S\W \\]?",
                message=_("Неверный формат ссылки."),
            ),
        ],
        verbose_name=_("Маршрут"),
    )

    texts = models.CharField(
        blank=True,
        null=True,
        max_length=50,
        help_text=_("""Заголовок пункта меню (ссылки)"""),
        verbose_name=_("Текст ссылки"),
        validators=[
            MaxLengthValidator(
                limit_value=50, message=_("""Максимальная длина 30 символов""")
            ),
            RegexValidator(
                regex=r"^(?!.*  )[a-zA-Z][\w \-_\d]{1,28}[a-zA-Z0-9]$[^\S\W \\]?",
                message=_(
                    """
                    Название не должно иметь двух пробелов подряд,
                    символов не принадлежащих к алфавиту и(или) цифрам.
                    Начинается из любой буквы. Заканчивается из любой буквы и
                    цифры.
                    Допускается дефис и(или) нижнее подчёркивание
                    """
                ),
            ),
        ],
    )

    class Meta:
        abstract = True


class LevelMenu(models.TextChoices):
    """
    'level' is a menu level 'top'. 'side' for a MenuNamesMode.level
    """

    TOP = "TOP", "Главное"
    SIDE = "SIDE", "Боковое"


class MenuNamesMode(models.Model):
    """
    The table 'MenuNamesMode'
    'names' is a menu's name.
    'levels' is a menu level 'top'. 'side'
    """

    names = models.CharField(
        unique=True,
        max_length=30,
        help_text=_(
            """Имя (максимальная длина 30символов) для вашего меню,
        чтоб ориентироваться в панели для администратора"""
        ),
        verbose_name=_("Название меню"),
        validators=[
            MaxLengthValidator(
                limit_value=30, message=_("""Максимальная длина 30 символов""")
            ),
            RegexValidator(
                regex=r"^(?!.*  )[a-zA-Z][\w \-_\d]{1,28}[a-zA-Z0-9]$[^\S\W \\]?",
                message=_(
                    """
                Название не должно иметь двух пробелов подряд,
                символов не принадлежащих к алфавиту и(или) цифрам.
                Начинается из любой буквы. Заканчивается из любой буквы и
                цифры.
                Допускается дефис и(или) нижнее подчёркивание
                """
                ),
            ),
        ],
    )
    levels = models.CharField(
        default=LevelMenu.TOP,
        choices=LevelMenu.choices,
        help_text=_(
            """Уровень может быть
        главным ('top'), боковым ('side')"""
        ),
        verbose_name=_("Уровень меню"),
    )

    def __str__(self):
        return _(f"""Заголовок меню: {self.names}""")

    class Meta:
        verbose_name = _("Заголовок меню")
        verbose_name_plural = _("Заголовки в меню")


class LinksMode(BaseLinkModel):
    """
    References
    """

    def __str__(self):
        return _(f"""Пункт меню: {self.texts}""")

    class Meta:
        verbose_name = "Ссылка в меню"
        verbose_name_plural = "Ссылки в меню"


class SubLinksMode(BaseLinkModel):
    """
    :param links is sub-reference of the '<a href="<your_refer>">'.
    :param status is specify a True or  not.
        It a position is the active or not active.
    """

    links = models.CharField(
        blank=True,
        max_length=100,
        help_text=_("/ваш/маршрут/на/внутреннюю/страницу/сайта/"),
        validators=[
            MaxLengthValidator(
                limit_value=100, message=_("""Максимальная длина 100 символов""")
            ),
            RegexValidator(
                regex=r"^(?!.*  )[a-z][\w\-_\d]{1,98}\/$[^\S\W \\]?",
                message=_("Неверный формат ссылки."),
            ),
        ],
        verbose_name=_("Маршрут"),
    )
    active = models.BooleanField(
        verbose_name=_("Активное или не активное"),
        help_text=_(
            """
        Активное или не активное меню на странице сайта
        """
        ),
    )
    name_id = models.ForeignKey(
        MenuNamesMode,
        on_delete=models.CASCADE,
        related_name="linksmenu",
        verbose_name=_("Выбрать меню"),
        help_text=_(
            """
            Меню в котором будет опубликована ссылка
            """
        ),
        db_column="name_id",
    )

    links_id = models.ForeignKey(
        LinksMode,
        on_delete=models.CASCADE,
        related_name="linksmenu",
        verbose_name=("Выбрать пункт для меню"),
        help_text=_(
            """
            Пункт меню (ссылка) в который будет
             опубликован в меню
            """
        ),
        db_column="links_id",
    )

    def __str__(self):
        return _(f"""Пункт меню: {self.texts}""")

    class Meta:
        verbose_name = "Ссылка в под-меню"
        verbose_name_plural = "Ссылки в под-меню"
