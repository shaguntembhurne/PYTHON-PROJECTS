#for gui lets import tkinter
# for the evaluaitona nd solution we are gonna use the library named simpify
import tkinter as tk
from sympy import sympify
root = tk.Tk()
root.title('Advance Calculator')
root.geometry("400x400")

#to hold the string variable we can use this
string_hold = tk.StringVar()

#field to get the data

field_1 = tk.Entry(root, textvariable=string_hold,font=["Arial,9"],insertwidth=4,borderwidth=4,width=14)
field_1.grid(row=0,column=0,rowspan=1,columnspan=4)

#now lets take the entry from field1 and use get operator
def button_click(value):
    current = string_hold.get()
    string_hold.set(current+str(value))

#to evaluate the result 
def evaluate():
    try:
        result = sympify(string_hold.get())
        string_hold.set(result.evalf())
    except Exception as e:
        string_hold.set('error')
    
#to clear the field we will just empty the string 
def clear():
    string_hold.set('')

#we can create buttons manually but lets use one matrix form 
buttons_list = [
    "7","8","9","*",
    "4","5","6","/",
    "1","2","3","+",
    "C","0","=","-"
]
row =1
col=0

for buttons in buttons_list:
    if buttons == "=":
        tk.Button(root,text=buttons,command=evaluate,padx=20,pady=20).grid(row=row,column=col)
    elif buttons == "C":
        tk.Button(root, text=buttons,command=clear,padx=20,pady=20).grid(row=row,column=col)
    else:
        tk.Button(root, text=buttons,command=lambda b= buttons: button_click(b),padx=20,pady=20).grid(row=row,column=col)
    
    col += 1 

    if col > 3:
        row +=1
        col =0

root.mainloop()