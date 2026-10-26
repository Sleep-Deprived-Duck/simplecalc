#simple calculator
import tkinter as tk

root = tk.Tk()
root.title("Simple Calculator")
root.geometry('200x300')
root.resizable(False, False)
root.configure(bg="#505050")

input = tk.Entry(root, width=30, bd=2)
input.grid(row=1, column=0, columnspan=4)

history = []
history_list = tk.Listbox(root)

def display_list():
    history_list.place(
        x=0,
        y=40,
        width=50,
        height=100
    )
    history_list.lift()
    history_list.delete(0, tk.END)
    for item in history:
        history_list.insert(tk.END, item)

history_list_open = False

def list_toggle():
        global history_list_open
        history_list_open = not history_list_open
        if history_list_open == False:
            history_list.place_forget()

def list_func():
    display_list()
    list_toggle()

def clearlist():
    history_list.delete(0, tk.END)

def button_input(value):
    current = input.get()
    input.delete(0, tk.END)
    input.insert(tk.END, current + str(value))

def clear_input():
    input.delete(0, tk.END)

def backspace():
    current = input.get() 
    input.delete(0, tk.END)
    input.insert(tk.END, current[:-1])

def evaluate():
    try:
        expression = input.get()
        result = eval(expression)
        input.delete(0, tk.END)
        input.insert(tk.END, str(result))
    except Exception as e:
        input.delete(0, tk.END)
        input.insert(tk.END, "Error")
    history.append(result)

hist_button = tk.Button(
    root, text="History",
    command=list_func,
    bg="#505050",
    fg="#a0a0a0"
).grid(row=0, column=0, sticky='nsew')

clearhist_button = tk.Button(
    root, text="Clear",
    command=clearlist,
    bg="#505050",
    fg="#a0a0a0"
).grid(row=0, column=1, sticky='nsew')

buttons = [
    '1','2','3','/',
    '4','5','6','*',
    '7','8','9','+',
    '.','0','=','-',
]

row_count=2
col_count=0

for button in buttons:
    tk.Button(
        root, text=button, padx=100, font=('Arial', 12),
        command=lambda b=button: button_input(b) if b!= '=' else evaluate(),
        bg="#505050",
        fg="#a0a0a0"
    ).grid(row=row_count, column=col_count, sticky='nsew')
    col_count += 1
    if col_count > 3:
        col_count = 0
        row_count += 1

tk.Button(
    root, text="C",
    command=clear_input,
    bg="#505050",
    fg="#a0a0a0"
).grid(row=row_count, column=col_count, columnspan=2, sticky='nsew')

col_count += 2

tk.Button(
    root, text="DEL",
    command=backspace,
    bg="#505050",
    fg="#a0a0a0"
).grid(row=row_count, column=col_count, columnspan=2, sticky='nsew')

for i in range(0, 6):
    root.rowconfigure(i, weight=1)
    root.columnconfigure(i, weight=1)

root.mainloop() 