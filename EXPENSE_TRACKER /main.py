import tkinter as tk
import sqlite3
from datetime import datetime

conn = sqlite3.connect('expense.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS expenses(
id INTEGER PRIMARY KEY AUTOINCREMENT,
ammount TEXT,
category TEXT,
discription TEXT,
date TEXT
)
""")
conn.commit()

root = tk.Tk()
root.title('expense tracker')


#make some empty string 
ammount_var = tk.StringVar()
category_var = tk.StringVar()
discription_var = tk.StringVar()

#now we will create some entry fiels 
tk.Label(root, text="ammount").grid(row =0,column = 0)
tk.Entry(root, textvariable=ammount_var).grid(row=0,column=1)

tk.Label(root, text="category").grid(row =1,column = 0)
tk.Entry(root, textvariable=category_var).grid(row=1,column=1)

tk.Label(root, text="discription").grid(row =2,column = 0)
tk.Entry(root, textvariable=discription_var).grid(row=2,column=1)

def add_expense():
    ammount = ammount_var.get()
    category = category_var.get()
    discription = discription_var.get()
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute("""
                    INSERT INTO expenses(ammount,category,discription,date)
                    VALUES (?,?,?,?)
    """,(ammount,category,discription,date))

    ammount_var.set("")
    category_var.set("")
    discription_var.set("")
    load_expense()

def load_expense():
    for widget in expense_frame.winfo_children():
        widget.destroy()
    cursor.execute('SELECT * FROM expenses')
    for row in cursor.fetchall():
        tk.Label(expense_frame,text=f"{row[1]} | {row[2]} | {row[4]} | {row[3]}").pack()

#lets make frame and button
tk.Button(root, text= "add expense",command=add_expense).grid(row= 4,column=1)
expense_frame = tk.Frame(root)
expense_frame.grid(row=5,columnspan=2)
load_expense()
root.mainloop()
conn.close()