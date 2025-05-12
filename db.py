import sqlite3
import os
from pathlib import Path

DEFAULT_INITIAL_DB_FILE = Path("initial.db")
DEFAULT_PROD_DB_FILE = Path("prod.db")

def initialize_db():
    if not DEFAULT_PROD_DB_FILE.is_file():  # if DB is not initialized
        DEFAULT_PROD_DB_FILE.write_bytes(DEFAULT_INITIAL_DB_FILE.read_bytes())  # copy initial.db to prod.db (create it)

def get_conn():
    return sqlite3.connect(str(DEFAULT_PROD_DB_FILE))