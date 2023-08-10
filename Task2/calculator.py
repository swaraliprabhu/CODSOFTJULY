import tkinter as tk
import math

def click_button(number):
    current = entry_result.get()
    entry_result.delete(0, tk.END)
    entry_result.insert(tk.END, str(current) + str(number))

def clear():
    entry_result.delete(0, tk.END)

def calculate():
    try:
        expression = entry_result.get()
        result = eval(expression)
        entry_result.delete(0, tk.END)
        entry_result.insert(tk.END, result)
    except Exception as e:
        entry_result.delete(0, tk.END)
        entry_result.insert(tk.END, "Error")

def calculate_square():
    try:
        num = float(entry_result.get())
        result = num * num
        entry_result.delete(0, tk.END)
        entry_result.insert(tk.END, result)
    except ValueError:
        entry_result.delete(0, tk.END)
        entry_result.insert(tk.END, "Error")

def calculate_sqrt():
    try:
        num = float(entry_result.get())
        result = math.sqrt(num)
        entry_result.delete(0, tk.END)
        entry_result.insert(tk.END, result)
    except ValueError:
        entry_result.delete(0, tk.END)
        entry_result.insert(tk.END, "Error")

def calculate_percentage():
    try:
        expression = entry_result.get()
        result = eval(expression) / 100
        entry_result.delete(0, tk.END)
        entry_result.insert(tk.END, result)
    except Exception as e:
        entry_result.delete(0, tk.END)
        entry_result.insert(tk.END, "Error")

def calculate_factorial():
    try:
        num = int(entry_result.get())
        result = math.factorial(num)
        entry_result.delete(0, tk.END)
        entry_result.insert(tk.END, result)
    except ValueError:
        entry_result.delete(0, tk.END)
        entry_result.insert(tk.END, "Error")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create the result entry field
entry_result = tk.Entry(root, width=25, borderwidth=5)
entry_result.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Create number buttons
for i in range(1, 10):
    button = tk.Button(root, text=str(i), padx=20, pady=10, command=lambda num=i: click_button(num))
    button.grid(row=(i - 1) // 3 + 1, column=(i - 1) % 3, padx=5, pady=5)

button_0 = tk.Button(root, text="0", padx=20, pady=10, command=lambda: click_button(0))
button_0.grid(row=4, column=0, padx=5, pady=5)

button_dot = tk.Button(root, text=".", padx=22, pady=10, command=lambda: click_button('.'))
button_dot.grid(row=4, column=1, padx=5, pady=5)

# Create operation buttons
button_add = tk.Button(root, text="+", padx=20, pady=10, command=lambda: click_button('+'))
button_add.grid(row=1, column=3, padx=5, pady=5)

button_subtract = tk.Button(root, text="-", padx=22, pady=10, command=lambda: click_button('-'))
button_subtract.grid(row=2, column=3, padx=5, pady=5)

button_multiply = tk.Button(root, text="*", padx=22, pady=10, command=lambda: click_button('*'))
button_multiply.grid(row=3, column=3, padx=5, pady=5)

button_divide = tk.Button(root, text="/", padx=22, pady=10, command=lambda: click_button('/'))
button_divide.grid(row=4, column=3, padx=5, pady=5)

button_equals = tk.Button(root, text="=", padx=20, pady=10, command=calculate)
button_equals.grid(row=5, column=3, padx=5, pady=5)

button_clear = tk.Button(root, text="C", padx=20, pady=10, command=clear)
button_clear.grid(row=5, column=0, padx=5, pady=5)

button_sqrt = tk.Button(root, text="√", padx=20, pady=10, command=calculate_sqrt)
button_sqrt.grid(row=5, column=1, padx=5, pady=5)

button_percentage = tk.Button(root, text="%", padx=20, pady=10, command=calculate_percentage)
button_percentage.grid(row=5, column=2, padx=5, pady=5)

button_factorial = tk.Button(root, text="!", padx=20, pady=10, command=calculate_factorial)
button_factorial.grid(row=4, column=2, padx=5, pady=5)

# Start the main event loop
root.mainloop()
