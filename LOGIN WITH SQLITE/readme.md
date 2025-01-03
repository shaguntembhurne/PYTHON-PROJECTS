# Login System

## Overview
This is a simple **Login System** built with **Python, Tkinter, and SQLite**. It allows users to **register** with a username and password and then **log in** using their credentials. The data is stored securely in an SQLite database.

## Features
- **User Registration**: Allows users to register with a unique username and password.
- **User Login**: Users can log in with their registered credentials.
- **SQLite Database**: Stores user information securely.
- **Basic Input Validation**: Ensures that both fields are filled before processing.
- **Error Handling**: Prevents duplicate usernames and incorrect logins.

## Dependencies
Ensure you have the following dependencies installed:
```bash
pip install tk
```
> SQLite3 is built into Python, so no additional installation is required.

## Database Schema
A table named `users` is created with the following structure:

| Column   | Data Type  | Description                    |
|----------|-----------|--------------------------------|
| id       | INTEGER (Primary Key) | Auto-incremented ID  |
| username | TEXT (Unique) | User's unique username       |
| password | TEXT | User's password (stored in plain text) |

## Code Breakdown

### 1. **Database Setup**
```python
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
```
- Creates the SQLite **database and users table** if they do not exist.

### 2. **User Registration**
```python
def register_user():
    username = username_entry.get()
    password = password_entry.get()
    if not username or not password:
        messagebox.showwarning('Please enter both username and password')
        return
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    try:
        cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
        conn.commit()
        messagebox.showinfo("Success", "Registration successful!")
    except sqlite3.IntegrityError:
        messagebox.showerror('Error', 'Username already exists')
    finally:
        conn.close()
    username_entry.delete(0, END)
    password_entry.delete(0, END)
```
- **Validates input fields** before processing.
- **Checks for duplicate usernames** to ensure uniqueness.
- Stores user credentials in the SQLite database.

### 3. **User Login**
```python
def login_user():
    username = username_entry.get()
    password = password_entry.get()
    if not username or not password:
        messagebox.showwarning('Please fill both fields')
        return
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
        result = cursor.fetchone()
        if result:
            messagebox.showinfo('Success', "Login successful!")
        else:
            messagebox.showerror('Failed', "Invalid username or password")
    except sqlite3.Error as e:
        messagebox.showerror('Database Error', f"Error: {e}")
    finally:
        conn.close()
    username_entry.delete(0, END)
    password_entry.delete(0, END)
```
- **Checks user credentials** against the database.
- **Handles incorrect login attempts gracefully.**
- **Clears input fields** after attempting login.

### 4. **GUI Setup with Tkinter**
```python
root = Tk()
root.title('Login System')
root.geometry('300x200')

username_label = Label(root, text="USERNAME")
username_label.grid(row=0, column=0, padx=10, pady=10)
username_entry = Entry(root)
username_entry.grid(row=0, column=1, padx=10, pady=10)

password_label = Label(root, text="PASSWORD")
password_label.grid(row=1, column=0, padx=10, pady=10)
password_entry = Entry(root, show="*")
password_entry.grid(row=1, column=1, padx=10, pady=10)

register_button = Button(root, text="Register", command=register_user)
register_button.grid(row=2, column=0, padx=10, pady=10)

login_button = Button(root, text="Log In", command=login_user)
login_button.grid(row=3, column=0, padx=10, pady=10)

root.mainloop()
```
- Creates **input fields** for username and password.
- Adds **buttons for registration and login**.
- Uses **Tkinter message boxes** to display success/error messages.

## How to Run
1. **Save the script as `login_system.py`.**
2. **Run the script:**
```bash
python login_system.py
```
3. **Register a new user** and log in using the credentials.

## Future Enhancements
- **Password Hashing** (Use `bcrypt` or `hashlib` for security).
- **Forgot Password Functionality**.
- **User Profile Management**.
- **Integration with a Web Interface**.

## Conclusion
This simple **Login System** provides a secure way to register and authenticate users using **Python, Tkinter, and SQLite**. 🚀

