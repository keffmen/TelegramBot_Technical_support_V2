from sqlite3 import Error
from connect_base import create_connection


# Функция добавления нового сотрудника
def add_employee(telegram_id, telegram_login, role):
    conn = create_connection()
    sql = """
    INSERT INTO employees (telegram_id, telegram_login, role)
    VALUES (?, ?, ?)
    """
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (telegram_id, telegram_login, role))
        conn.commit()
        print("Сотрудник успешно добавлен")
    except Error as e:
        print(f"Произошла ошибка '{e}'")


# Функция изменения роли сотрудника по telegram_id
def change_employee_role(telegram_id, new_role):
    conn = create_connection()
    sql = """
    UPDATE employees
    SET role = ?
    WHERE telegram_id = ?
    """
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (new_role, telegram_id))
        conn.commit()
        print("Роль сотрудника успешно обновлена")
    except Error as e:
        print(f"Произошла ошибка '{e}'")


# Функция удаления сотрудника по telegram_id
def delete_employee(telegram_id):
    conn = create_connection()
    sql = """
    DELETE FROM employees
    WHERE telegram_id = ?
    """
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (telegram_id,))
        conn.commit()
        print("Сотрудник успешно удален")
    except Error as e:
        print(f"Произошла ошибка '{e}'")
