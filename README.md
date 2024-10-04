## .ENV
File `.env` make in project's root  
```text
DJANGO_SECRET_KEY=secret_key_of_your_django
DJANGO_SETTING_POSTGRES_DB=db_name_of_your_db
DJANGO_SETTING_POSTGRES_USER=user_name_of_your_db
DJANGO_SETTING_POSTGRES_PASSWORD=password_of_your_db
DJANGO_SETTING_POSTGRES_HOST=host_of_your_db
DJANGO_SETTING_POSTGRES_PORT=port_of_your_db
```

## project_root.settings
```python
# project_root.settings.py
# ...
LANGUAGE_CODE = "ru"
# ...
TIME_ZONE = "Asia/Novosibirsk"
# ...
DEFAULT_CHARSET = "utf-8"
```

## Descript
Модуль не стал привязывать к пользователю

### Task
> Все, что над выделенным пунктом - развернуто.

Значит первый уровень вложенности раскрывать НАД основным меню.

Но, читаем дальше 
> Первый уровень вложенности под выделенным пунктом тоже развернут.

Или первый уровень вложенности раскрывать ПОД основным меню? \
Но есть прилагательное `тоже`.
> Все, что над выделенным пунктом - развернуто. Первый уровень вложенности \
> под выделенным пунктом тоже развернут.

Так:
- в верх раскрывать?
- или в низ раскрывать?
- или при каких условиях открывать в верх, а при каких в низ?

*P.S.: Вопросы к многообразной формулировке задач не отражает опыт разработчика.* 
