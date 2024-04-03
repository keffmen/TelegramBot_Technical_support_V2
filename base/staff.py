import sqlite3
from sqlite3 import Error


# Функция создания подключения к базе данных
def create_connection():
    conn = None
    try:
        conn = sqlite3.connect(r"base.db")
        print("Connection to SQLite DB successful")
        return conn
    except Error as e:
        print(f"The error '{e}' occurred")


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
        print("Employee table created successfully")
    except Error as e:
        print(f"The error '{e}' occurred")


# Функция добавления нового сотрудника
def add_employee(conn, telegram_id, telegram_login, role):
    sql = """
    INSERT INTO employees (telegram_id, telegram_login, role)
    VALUES (?, ?, ?)
    """
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (telegram_id, telegram_login, role))
        conn.commit()
        print("Employee added successfully")
    except Error as e:
        print(f"The error '{e}' occurred")


# Функция изменения роли сотрудника по telegram_id
def change_employee_role(conn, telegram_id, new_role):
    sql = """
    UPDATE employees
    SET role = ?
    WHERE telegram_id = ?
    """
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (new_role, telegram_id))
        conn.commit()
        print("Employee role updated successfully")
    except Error as e:
        print(f"The error '{e}' occurred")


# Функция удаления сотрудника по telegram_id
def delete_employee(conn, telegram_id):
    sql = """
    DELETE FROM employees
    WHERE telegram_id = ?
    """
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (telegram_id,))
        conn.commit()
        print("Employee deleted successfully")
    except Error as e:
        print(f"The error '{e}' occurred")
