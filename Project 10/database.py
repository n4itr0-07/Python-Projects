import pymysql
from tkinter import messagebox

def connect_database():
    global conn, mycourser
    try:
        conn = pymysql.connect(host="localhost", user="root", password="Salik@123")
        mycourser = conn.cursor()
    except Exception as e:
        messagebox.showerror("Error", "Something went wrong. Please open MySQL app before running again.")
        return None, None

    try:
        mycourser.execute("CREATE DATABASE IF NOT EXISTS employee_data")
        mycourser.execute("USE employee_data")
        mycourser.execute("""
            CREATE TABLE IF NOT EXISTS data (
                id VARCHAR(20),
                Name VARCHAR(50),
                Phone VARCHAR(15),
                Roles VARCHAR(50),
                Gender VARCHAR(30),
                Salary DECIMAL(10, 2)
            )
        """)
        conn.commit()
    except Exception as e:
        messagebox.showerror("Error", f"Failed to create table: {e}")
    finally:
        conn.close()

    return pymysql.connect(host="localhost", user="root", password="Salik@123", database="employee_data")


def insert(id, name, phone, role, gender, salary):
    conn = connect_database()
    if conn is None:
        return

    try:
        mycourser = conn.cursor()
        mycourser.execute("INSERT INTO data VALUES (%s, %s, %s, %s, %s, %s)", (id, name, phone, role, gender, salary))
        conn.commit()
    except Exception as e:
        messagebox.showerror("Error", f"Failed to insert data: {e}")
    finally:
        conn.close()

def fetch_employees():
    conn = connect_database()
    if conn is None:
        return []

    try:
        mycourser = conn.cursor()
        mycourser.execute("SELECT * FROM data")
        result = mycourser.fetchall()
        return result
    except Exception as e:
        messagebox.showerror("Error", f"Failed to fetch data: {e}")
        return []
    finally:
        conn.close()

def delete_employee(id):
    conn = connect_database()
    if conn is None:
        return

    try:
        mycourser = conn.cursor()
        mycourser.execute("DELETE FROM data WHERE id=%s", (id,))
        conn.commit()
    except Exception as e:
        messagebox.showerror("Error", f"Failed to delete data: {e}")
    finally:
        conn.close()

def delete_all_employees():
    conn = connect_database()
    if conn is None:
        return

    try:
        mycourser = conn.cursor()
        mycourser.execute("DELETE FROM data")
        conn.commit()
    except Exception as e:
        messagebox.showerror("Error", f"Failed to delete data: {e}")
    finally:
        conn.close()
