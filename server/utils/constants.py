from os import getenv
from dotenv import load_dotenv

load_dotenv()

DB_PATH = getenv("DB_PATH")
DATABASE_URI = getenv("DATABASE_URI")
