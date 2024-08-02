import pymysql
from tkinter import messagebox


def connect_database():
    try:
        conn = pymysql.connect(host="localhost", user="root", password="Salik@123")
        mycourser = conn.cursor()

    except:
        messagebox.showerror("Error","Something went wrong,Please ope mysql app before running again" )






def insert(id,name,phone,role,gender,salary):
    print("insert")