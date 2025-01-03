import sqlite3
from tkinter import *
from tkinter import messagebox
import sqlite3
conn = sqlite3.connect('users.db')
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password TEXT
)
""")
conn.commit()
conn.close()


#funtion to enter username              
def register_user():
    username = username_entry.get()
    password = password_entry.get()
    if not username or not password:
        messagebox.showwarning('please put both username end ')
        return
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    try:
        cursor.execute('INSERT INTO users (username,password) VALUES (?, ?)',(username,password))
        conn.commit()
        messagebox.showinfo("success","registration is successful")
    except sqlite3.IntegrityError:
        messagebox.showerror('username already exists')
    finally:
        conn.close()
    username_entry.delete(0, END)
    password_entry.delete(0, END)

#function to enter passwoard
def login_user():
    username = username_entry.get()
    password = password_entry.get()

    if not username or not password:
        messagebox.showwarning('please fill both')
        return
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?",(username, password))
        result = cursor.fetchone()
        if result:
            messagebox.showinfo('success',"log in was successfull")
        else:
            messagebox.showerror('failed',"log in was unsuccessfull")
    except sqlite3.Error as e:
        messagebox.showerror('database error,f"error{e}"')
    finally:
        conn.close()
    #clear entries
    username_entry.delete(0, END)
    password_entry.delete(0, END)


root = Tk()
root.title('log in system')
root.geometry('300x200')

#username entry and label
username_label = Label(root, text="USERNAME")
username_label.grid(row=0,column=0,padx=0,pady=10)
username_entry = Entry(root)
username_entry.grid(row=0,column=1,padx=0,pady=10)


password_label = Label(root, text="PASSWORD")
password_label.grid(row=1,column=0,padx=0,pady=10)
password_entry = Entry(root, show="*")
password_entry.grid(row=1,column=1,padx=10,pady=10)

register_button = Button(root, text="register", command=register_user)
register_button.grid(row=2,column=0,padx=10,pady=10)

login_button = Button(root, text="log in", command=login_user)
login_button.grid(row=3,column=0,padx=10,pady=10)
root.mainloop()