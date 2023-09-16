import os

from dotenv import load_dotenv

load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

SECRET_AUTH = os.environ.get("SECRET_AUTH", "SECRET_AUTH")

DB_HOST_TEST = os.getenv("DB_HOST_TEST")
DB_NAME_TEST = os.getenv("DB_NAME_TEST")
DB_PASS_TEST = os.getenv("DB_PASS_TEST")
DB_PORT_TEST = os.getenv("DB_PORT_TEST")
DB_USER_TEST = os.getenv("DB_USER_TEST")

REDIS_HOST = os.getenv("REDIS_HOST")
REDIS_PORT = os.getenv("REDIS_PORT")
