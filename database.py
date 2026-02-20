import os
import psycopg2
from dotenv import load_dotenv

# Load environment variables from .env (for local use)
load_dotenv()

def connection():
    con = psycopg2.connect(
        host=os.environ.get("DB_HOST"),
        database=os.environ.get("DB_NAME"),
        user=os.environ.get("DB_USER"),
        password=os.environ.get("DB_PASSWORD"),
        port=os.environ.get("DB_PORT")
    )
    return con

conn = connection()