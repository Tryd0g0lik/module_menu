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
        unique=True,
        max_length=100,
        help_text=_("ваш/маршрут/на/внутреннюю/страницу/сайта/"),
        validators=[
            MaxLengthValidator(
                limit_value=100, message=_("""Максимальная длина 100 символов""")
            ),
            RegexValidator(
                regex=r"^(?!.*  )[a-z][\w\-_\d]{1,98}\/$[^\S\W \/]?",
                # regex=
                # r"^(?!.*  )[a-zA-Zа-яА-ЯёЁ][\w \-_\dа-яА-ЯёЁ]{0,98}[a-zA-Zа-яА-ЯёЁ0-9\/]$",
                message=_("Неверный формат ссылки."),
            ),
        ],
        verbose_name=_("Маршрут"),
    )

    texts = models.CharField(
        blank=True,
        null=True,
        max_length=50,
        help_text=_("Текст ссылки (Text refer)"),
        verbose_name=_("Текст ссылки"),
        validators=[
            MaxLengthValidator(
                limit_value=50, message=_("""Максимальная длина 50 символов""")
            ),
            RegexValidator(
                regex=r"^(?!.*  )[a-zA-Zа-яА-ЯёЁ][\w \-_\dа-яА-ЯёЁ]{1,48}[a-zA-Zа-яА-ЯёЁ]$[^\S\W \\]?",
                message=_(
                    """
                    Название не должно иметь двух пробелов подряд,
                    символов не принадлежащих к алфавиту и(или) цифрам.
                    Начинается из любой буквы. Заканчивается из любой буквы
                    и(или) цифры.
                    Допускается дефис и(или) нижнее подчёркивание.

                    """
                ),
            ),
        ],
    )

    class Meta:
        abstract = True


# class PageTemplatesMode(models.TextChoices):
"""
   This is a html templates list for the table "PageModel"
"""


class PageModel(BaseLinkModel):
    """
    One page
    'links' is reference of the itself page.
    'texts' is header of the itself page.
    'menu_list' is menu list for publication to the page.
    'template' The choice of the template for the page
    """

    MAIN = "index.html"
    ABOUT = "about/index.html"
    ACCOUNT = "account/index.html"
    PROFILE = "profile/index.html"
    NOTPAGE = "404/index.html"

    PAGE_TEMPLATES = [
        (MAIN, "Главная"),
        (ABOUT, "О нас"),
        (ACCOUNT, "Аккаунт"),
        (PROFILE, "Профиль"),
        (NOTPAGE, "Страница не найдена"),
    ]
    menu_list = models.ManyToManyField(
        "MenuNamesMode",
        # blank=True,
        # null=True,
        related_name="pages_menu",
        verbose_name=_("Выбрать меню"),
        help_text=_(
            """
            Список меню которые будут опубликованы на странице.
            """
        ),
    )
    active = models.BooleanField(
        default=False,
        verbose_name=_("Активное"),
        help_text=_(
            """
         Страница "True"-публикуется.
        """
        ),
    )
    template = models.CharField(
        default=NOTPAGE,
        choices=PAGE_TEMPLATES,
        verbose_name=_("Выбрать шаблон для страницы"),
        help_text=_(
            """
            HTML-шаблон для контента страницы.
            """
        ),
    )

    # def is_upperclass(self):
    #     return self.template in {
    #         self.template
    #     }
    def __str__(self):
        return "%s" % self.texts

    class Meta:
        verbose_name = "Страница"
        verbose_name_plural = "Страница"


class LevelMenu(models.TextChoices):
    """
    'TOP' is a menu main level.
    'SIDE' is a menu sub-level.
    """

    TOP = "TOP", _("Главное")
    SIDE = "SIDE", _("Боковое")
    FLOATER = "FLOATER", _("Нижнее")


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
        return "%s" % (self.names)

    class Meta:
        verbose_name = _("Заголовок меню")
        verbose_name_plural = _("Меню")


class LinksMode(BaseLinkModel):
    """
    References
    'links' страница на которую ссылается ссылка
    """

    active = models.BooleanField(
        verbose_name=_("Активное"),
        help_text=_(
            """
         вложенности Активное или не активное меню на странице сайта
        """
        ),
    )

    links = models.ForeignKey(
        PageModel,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name="pageыlink",
        verbose_name=_("Выбрать страницу"),
        help_text=_(
            """
            Страница на которой будет опубликовано меню
            """
        ),
    )

    def __str__(self):
        return self.texts

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
        return "%s" % self.name_id

    class Meta:
        verbose_name = "Меню и под-меню"
        verbose_name_plural = "Меню и под-меню"
