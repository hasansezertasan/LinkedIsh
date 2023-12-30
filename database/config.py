import os

import dotenv

dotenv.load_dotenv(".env")

basedir = os.path.abspath(os.path.dirname(__name__))
SQLITE_PATH = os.path.join(basedir, "db.sqlite3")
SQLALCHEMY_DATABASE_URL = os.getenv("SQLALCHEMY_DATABASE_URL", f"sqlite:///{SQLITE_PATH}")
ASQLALCHEMY_DATABASE_URL = os.getenv("ASQLALCHEMY_DATABASE_URL", f"sqlite+aiosqlite:///{SQLITE_PATH}")

connect_args = {}
if "sqlite" in SQLALCHEMY_DATABASE_URL or "sqlite" in ASQLALCHEMY_DATABASE_URL:
    connect_args = {"check_same_thread": False}
