from sqlite3 import Error
from datetime import datetime
from connect_base import create_connection


# Функция добавления новой заявки
def add_application(id_applications,sender_name, sender_id, employee_name, employee_id, request_text, phone_number):
    conn = create_connection()
    created_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    status = "Открыта"
    sql = """
    INSERT INTO applications (id_applications, created_date, sender_name, sender_id, employee_name, employee_id, request_text, phone_number, status)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (
            id_applications, created_date, sender_name, sender_id, employee_name, employee_id, request_text, phone_number, status))
        conn.commit()
        print("Приложение успешно добавлено")
    except Error as e:
        print(f"Произошла ошибка '{e}'")


# Функция изменения статуса у заявки по её id
def change_application_status(application_id, new_status):
    conn = create_connection()
    sql = """
    UPDATE applications
    SET status = ?
    WHERE id = ?
    """
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (new_status, application_id))
        conn.commit()
        print("Статус заявки успешно обновлен")
    except Error as e:
        print(f"Произошла ошибка '{e}'")


# Функция вывода всей информации по заявке по её id
def get_application_by_id(conn, application_id):
    conn = create_connection()
    sql = """
    SELECT * FROM applications
    WHERE id = ?
    """
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (application_id,))
        application = cursor.fetchone()
        # if application:
        #     # Сделать вывод в нужном формате
        #     # print("Application Details:")
        #     # print(f"ID: {application[0]}")
        #     # print(f"Created Date: {application[1]}")
        #     # print(f"Closed Date: {application[2]}")
        #     # print(f"Sender Name: {application[3]}")
        #     # print(f"Sender ID: {application[4]}")
        #     # print(f"Employee Name: {application[5]}")
        #     # print(f"Employee ID: {application[6]}")
        #     # print(f"Request Text: {application[7]}")
        #     # print(f"Phone Number: {application[8]}")
        #     # print(f"Status: {application[9]}")
        # else:
        #     print(f"Заявка {application_id} не найдена")
    except Error as e:
        print(f"Произошла ошибка '{e}'")

