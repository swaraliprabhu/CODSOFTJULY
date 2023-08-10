from tkinter import *
import tkinter.messagebox

# Create the application window
window = Tk()
window.title("DataFlair Python To-Do List APP")

# Create the application layout
frame_task = Frame(window)
frame_task.pack()

listbox_task = Listbox(frame_task, bg="white", fg="black", height=15, width=50, font="Helvetica")
listbox_task.pack(side=LEFT)

scrollbar_task = Scrollbar(frame_task)
scrollbar_task.pack(side=RIGHT, fill=Y)

listbox_task.config(yscrollcommand=scrollbar_task.set)
scrollbar_task.config(command=listbox_task.yview)

entry_task = Entry(window, width=50)
entry_task.pack()

button_add_task = Button(window, text="Add task", width=48, bg="green", fg="white", command=lambda: add_item())
button_add_task.pack()

button_delete_task = Button(window, text="Delete task", width=48, bg="red", fg="white", command=lambda: delete_item())
button_delete_task.pack()

button_edit_task = Button(window, text="Edit task", width=48, bg="blue", fg="white", command=lambda: edit_item())
button_edit_task.pack()

def add_item():
    task = entry_task.get()
    if task != "":
        listbox_task.insert(END, task)
        entry_task.delete(0, END)
    else:
        tkinter.messagebox.showwarning("Warning", "You need to enter a task.")

def delete_item():
    try:
        task_index = listbox_task.curselection()[0]
        listbox_task.delete(task_index)
    except IndexError:
        tkinter.messagebox.showwarning("Warning", "You need to select a task.")

def edit_item():
    try:
        task_index = listbox_task.curselection()[0]
        new_value = entry_task.get()
        listbox_task.delete(task_index)
        listbox_task.insert(task_index, new_value)
    except IndexError:
        tkinter.messagebox.showwarning("Warning", "You need to select a task.")

# Run the main loop
window.mainloop()
