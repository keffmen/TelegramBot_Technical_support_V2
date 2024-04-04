import sqlite3
from sqlite3 import Error


# Функция создания подключения к базе данных
def create_connection():
    conn = None
    try:
        conn = sqlite3.connect(r"base.db")
        print("Подключение к базе данных SQLite выполнено успешно")
        return conn
    except Error as e:
        print(f"Произошла ошибка '{e}'")


# Функция создания таблицы сотрудников, если её нет
def create_employee_table(conn):
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY,
        telegram_id INTEGER UNIQUE,
        telegram_login TEXT,
        role TEXT
    );
    """
    try:
        cursor = conn.cursor()
        cursor.execute(create_table_sql)
        conn.commit()
        print("Таблица сотрудников успешно создана")
    except Error as e:
        print(f"Произошла ошибка '{e}'")


# Функция создания таблицы заявок
def create_applications_table(conn):
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS applications (
        id_applications INTEGER PRIMARY,
        created_date TEXT,
        closed_date TEXT,
        sender_name TEXT,
        sender_id INTEGER,
        employee_name TEXT,
        employee_id INTEGER,
        request_text TEXT,
        phone_number TEXT,
        status TEXT
    );
    """
    try:
        cursor = conn.cursor()
        cursor.execute(create_table_sql)
        conn.commit()
        print("Таблица приложений успешно создана")
    except Error as e:
        print(f"The error '{e}' occurred")


if __name__ == '__main__':
    # Создание подключения к базе данных
    conn = create_connection()
    if conn is not None:
        # Создание таблицы сотрудников
        create_employee_table(conn)
        create_applications_table(conn)
