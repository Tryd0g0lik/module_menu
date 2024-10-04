"""Here data imports from the file '.env' of django project"""

import os

import dotenv

dotenv.load_dotenv()
DJANGO_SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", "")
DJANGO_SETTING_POSTGRES_DB = os.getenv("DJANGO_SECRET_KEY", "")
DJANGO_SETTING_POSTGRES_USER = os.getenv("DJANGO_SECRET_KEY", "")
DJANGO_SETTING_PASSWORD = os.getenv("DJANGO_SECRET_KEY", "")
DJANGO_SETTING_HOST = os.getenv("DJANGO_SECRET_KEY", "")
DJANGO_SETTING_PORT = os.getenv("DJANGO_SECRET_KEY", "")
