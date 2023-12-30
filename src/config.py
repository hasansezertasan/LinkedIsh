import datetime
import os

import dotenv

from database.config import SQLALCHEMY_DATABASE_URL

dotenv.load_dotenv(".env")

basedir = os.path.abspath(os.path.dirname(__name__))
SECRET_KEY = os.getenv("SECRET_KEY", "super-secret")
SESSION_LIFETIME_DAYS = os.getenv("SESSION_LIFETIME_DAYS", 7)
SESSION_LIFETIME_DAYS = int(SESSION_LIFETIME_DAYS)

config = {
    "SECRET_KEY": SECRET_KEY,
    "PERMANENT_SESSION_LIFETIME": datetime.timedelta(days=SESSION_LIFETIME_DAYS),
    "SQLALCHEMY_DATABASE_URI": SQLALCHEMY_DATABASE_URL,
}
