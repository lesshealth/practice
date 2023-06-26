import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as ttk
import mysql.connector
from config import host, user, password, db_name



def login():
    username = username_entry_login.get()
    password = password_entry_login.get()

    try:
        conn = mysql.connector.connect(
            host=host,
            port=3306,
            user=user,
            password=password,
            database=db_name,
        )
        messagebox.showinfo("Успешно", "Авторизация прошла успешно.")
        login_window.withdraw()
        main_window.deiconify()
    except Exception as ex:
        messagebox.showerror("Ошибка", str(ex))


def open_login_window():
    main_window.withdraw()
    login_window.deiconify()

def open_main_window():
    login_window.withdraw()
    main_window.deiconify()

def filter_data():
    ip_address = ip_entry.get()

    try:
        conn = mysql.connector.connect(
            host=host,
            port=3306,
            user=user,
            password=password,
            database=db_name,
        )
        cursor = conn.cursor()

        query = f"SELECT * FROM access_logs WHERE ip_address = '{ip_address}'"
        values = (ip_address)
        cursor.execute(query)
        rows = cursor.fetchall()

        for row in rows:
            print(row)  # Вывод данных в консоль

        cursor.close()
        conn.close()

    except Exception as ex:
        messagebox.showerror("Error", str(ex)) 

def view_data():
    try:
        conn = mysql.connector.connect(
            host=host,
            port=3306,
            user=user,
            password=password,
            database=db_name,
        )
        cursor = conn.cursor()

        query = "SELECT * FROM access_logs"
        cursor.execute(query)
        rows = cursor.fetchall()

        for row in rows:
            print(row) 

        cursor.close()
        conn.close()

    except Exception as ex:
        messagebox.showerror("Error", str(ex))

def add_data():
    ip_address = ip_entry.get()
    timestamp = timestamp_entry.get()
    request_method = request_method_entry.get()
    requested_page = requested_page_entry.get()
    http_version = http_version_entry.get()
    status_code = status_code_entry.get()
    response_size = response_size_entry.get()
    user_agent = user_agent_entry.get()

    try:
        conn = mysql.connector.connect(
            host=host,
            port=3306,
            user=user,
            password=password,
            database=db_name,
        )
        cursor = conn.cursor()

        query = "INSERT INTO access_logs (ip_address, timestamp, request_method, requested_page, http_version, status_code, response_size, user_agent) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        values = (ip_address, timestamp, request_method, requested_page, http_version, status_code, response_size, user_agent)
        cursor.execute(query, values)
        conn.commit()

        messagebox.showinfo("Success", "Data added successfully.")

        cursor.close()
        conn.close()

    except Exception as ex:
        messagebox.showerror("Error", str(ex))


def delete_data():
    entry_id = id_delete_entry.get()

    try:
        conn = mysql.connector.connect(
            host=host,
            port=3306,
            user=user,
            password=password,
            database=db_name,
        )
        cursor = conn.cursor()

        query = "DELETE FROM access_logs WHERE id = %s"
        value = (entry_id)
        cursor.execute(query, value)
        conn.commit()

        messagebox.showinfo("Success", "Data deleted successfully.")

        cursor.close()
        conn.close()

    except Exception as ex:
        messagebox.showerror("Error", str(ex))



login_window = ttk.Window(themename="minty") #выбираем тему для окна
login_window["bg"] = "gray22"
login_window.title("Авторизация") #заголовок окна
login_window.geometry("800x600")


username_label_login = tk.Label(login_window, text="Username:")
username_label_login.pack(pady=10)

username_entry_login = tk.Entry(login_window)
username_entry_login.pack(pady=10)

password_label_login = tk.Label(login_window, text="Password:")
password_label_login.pack(pady=10)

password_entry_login = tk.Entry(login_window, show="*")
password_entry_login.pack(pady=10)

login_button_login = tk.Button(login_window, text="Login", command=login)
login_button_login.pack(pady=10)


main_window = ttk.Window(themename="minty") #выбираем тему для окна
main_window["bg"] = "gray22"
main_window.title("Main") #заголовок окна
main_window.geometry("1200x800")


ip_label = tk.Label(main_window, text="Фильтрация по IP:")
ip_label.pack()

ip_entry = tk.Entry(main_window)
ip_entry.pack()

filter_button = tk.Button(main_window, text="Отфильтровать", command=filter_data)
filter_button.pack()

view_button = tk.Button(main_window, text="Просмотреть данные", command=view_data)
view_button.pack(pady=5)

ip_label = tk.Label(main_window, text="IP Address:")
ip_label.pack(pady=5)

ip_entry = tk.Entry(main_window)
ip_entry.pack(pady=5)

timestamp_label = tk.Label(main_window, text="Timestamp (писать вот так: YYYY-MM-DD HH:MM:SS):")
timestamp_label.pack(pady=5)

timestamp_entry = tk.Entry(main_window)
timestamp_entry.pack(pady=5)

request_method_label = tk.Label(main_window, text="Request Method:")
request_method_label.pack(pady=5)

request_method_entry = tk.Entry(main_window)
request_method_entry.pack(pady=5)

requested_page_label = tk.Label(main_window, text="Requested Page:")
requested_page_label.pack(pady=5)

requested_page_entry = tk.Entry(main_window)
requested_page_entry.pack(pady=5)

http_version_label = tk.Label(main_window, text="HTTP Version:")
http_version_label.pack(pady=5)

http_version_entry = tk.Entry(main_window)
http_version_entry.pack(pady=5)

status_code_label = tk.Label(main_window, text="Status Code:")
status_code_label.pack(pady=5)

status_code_entry = tk.Entry(main_window)
status_code_entry.pack(pady=5)

response_size_label = tk.Label(main_window, text="Response Size:")
response_size_label.pack(pady=5)

response_size_entry = tk.Entry(main_window)
response_size_entry.pack(pady=5)

user_agent_label = tk.Label(main_window, text="User Agent:")
user_agent_label.pack(pady=5)

user_agent_entry = tk.Entry(main_window)
user_agent_entry.pack(pady=5)

add_button = tk.Button(main_window, text="Add Data", command=add_data)
add_button.pack(pady=5)

id_delete_label = tk.Label(main_window, text="Удалить по ID:")
id_delete_label.pack(pady=10)

id_delete_entry = tk.Entry(main_window)
id_delete_entry.pack(pady=10)

delete_button = tk.Button(main_window, text="Удалить данные", command=delete_data)
delete_button.pack()


open_login_window() 

main_window.mainloop()
