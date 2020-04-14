import sqlite3 
from parse import 



conn = sqlite3.connect(os.path.join("db", "database.db"))
cursor = conn.cursor()



def insert():
    pass

def delete():
    pass

def fetch_to_day():
    pass

def fetch_all_day():
    pass

def get_cursor():
    return cursor


def _init_db():
    """Инициализирует БД"""
    with open("createdb.sql", "r") as f:
        sql = f.read()
    cursor.executescript(sql)
    conn.commit()


def check_db_exists():
    """Проверяет, инициализирована ли БД, если нет — инициализирует"""
    cursor.execute("SELECT name FROM sqlite_master "
                   "WHERE type='table' AND name='dmik_info'")
    table_exists = cursor.fetchall()
    if table_exists:
        return
    _init_db()


check_db_exists()

