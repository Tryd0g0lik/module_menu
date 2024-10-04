import os
import dotenv
dotenv.load_dotenv()
DJANGO_SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", "")