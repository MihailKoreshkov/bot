import sqlite3 
import os



conn = sqlite3.connect(os.path.join("db", "database.db"))
cursor = conn.cursor()


def insert(table: str, data: list):
    placeholders = ', '.join('?' * data[0])
    cursor.executemany(f"INSERT INTO {table} VALUES({placeholders})", data)
    conn.commit()
    

def delete(table):
    cursor.execute(
        f"DELETE FROM {table}"
    )
    conn.commit()


def fetch_to_day(date, table):
    pass

def fetch_all_day(table):
    cursor.execute(f"SELECT * FROM {table}")
    data = cursor.fetchall()
    return data

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

