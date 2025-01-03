# Expense Tracker

## Overview
This is a simple **Expense Tracker** application using **Python, Tkinter, and SQLite**. It allows users to **log expenses** with an amount, category, and description, and displays the recorded expenses in a GUI.

## Features
- **Add Expenses:** Users can enter an amount, category, and description to log an expense.
- **Store Data in SQLite:** The expenses are stored in a SQLite database (`expense.db`).
- **Display Expenses:** The GUI dynamically loads and displays recorded expenses.

## Installation
Ensure you have the following dependencies installed:
```bash
pip install tk
```
> SQLite3 is built-in with Python, so no need to install it separately.

## Database Schema
A table named `expenses` is created if it does not exist, with the following structure:

| Column      | Data Type  | Description |
|------------|-----------|-------------|
| id         | INTEGER (Primary Key) | Auto-incremented ID |
| amount     | TEXT      | Expense amount |
| category   | TEXT      | Expense category |
| description | TEXT      | Expense details |
| date       | TEXT      | Timestamp of the expense |

## Usage
### 1. **Database Connection & Table Creation**
```python
conn = sqlite3.connect('expense.db')
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS expenses(
id INTEGER PRIMARY KEY AUTOINCREMENT,
amount TEXT,
category TEXT,
description TEXT,
date TEXT
)
""")
conn.commit()
```
- Establishes a **connection** to `expense.db`.
- Creates the `expenses` table if it doesn’t already exist.

### 2. **Creating the Tkinter GUI**
```python
root = tk.Tk()
root.title('Expense Tracker')
```
- Initializes the Tkinter **window**.
- Sets the **title** of the application.

### 3. **User Input Fields**
```python
tk.Label(root, text="Amount").grid(row=0, column=0)
tk.Entry(root, textvariable=amount_var).grid(row=0, column=1)

tk.Label(root, text="Category").grid(row=1, column=0)
tk.Entry(root, textvariable=category_var).grid(row=1, column=1)

tk.Label(root, text="Description").grid(row=2, column=0)
tk.Entry(root, textvariable=description_var).grid(row=2, column=1)
```
- Creates **labels** and **entry fields** for users to input expense details.

### 4. **Adding Expenses**
```python
def add_expense():
    amount = amount_var.get()
    category = category_var.get()
    description = description_var.get()
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute("""
                    INSERT INTO expenses(amount, category, description, date)
                    VALUES (?, ?, ?, ?)
    """, (amount, category, description, date))

    amount_var.set("")
    category_var.set("")
    description_var.set("")
    load_expense()
```
- Fetches user input.
- Stores the new expense in the SQLite database.
- Clears the input fields after saving.

### 5. **Loading and Displaying Expenses**
```python
def load_expense():
    for widget in expense_frame.winfo_children():
        widget.destroy()
    cursor.execute('SELECT * FROM expenses')
    for row in cursor.fetchall():
        tk.Label(expense_frame, text=f"{row[1]} | {row[2]} | {row[4]} | {row[3]}").pack()
```
- Clears the existing labels inside the expense display frame.
- Fetches **all expenses** from the database and displays them.

### 6. **Adding the 'Add Expense' Button and Expense Frame**
```python
tk.Button(root, text="Add Expense", command=add_expense).grid(row=4, column=1)
expense_frame = tk.Frame(root)
expense_frame.grid(row=5, columnspan=2)
load_expense()
```
- Creates a button to **add an expense**.
- Creates a frame to **display expenses**.
- Calls `load_expense()` initially to show existing records.

### 7. **Running the Application**
```python
root.mainloop()
conn.close()
```
- Starts the Tkinter **event loop**.
- **Closes the database connection** when the program exits.

## How to Run
1. **Save the script as `expense_tracker.py`.**
2. **Run the script:**
```bash
python expense_tracker.py
```
3. **Enter expense details** and click 'Add Expense'.
4. **View the saved expenses** displayed in the UI.

## Future Enhancements
- **Edit & Delete Expenses**
- **Category-based Filtering**
- **Export Data as CSV**
- **Graphical Analysis using Matplotlib**

## License
This project is licensed under the MIT License.

## Conclusion
This simple **Expense Tracker** helps in recording and managing expenses efficiently using Python, Tkinter, and SQLite. 🚀

