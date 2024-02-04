from tkinter import *
import tkinter.messagebox
from datetime import datetime

def addtask():
    input_text = entry_task.get(1.0, "end-1c")
    if input_text.strip() == "":
        tkinter.messagebox.showwarning(title="Warning!", message="Please enter some text.")
    else:
        listbox_task.insert(END, f"{len(listbox_task.get(0, END))}. {input_text.strip()}")
        entry_task.delete(1.0, END)

def deletetask():
    selected = listbox_task.curselection()
    if selected:
        if selected[0] != 0:  # Check if the selected item is not the date row
            listbox_task.delete(selected[0])
        else:
            tkinter.messagebox.showwarning(title="Warning!", message="Cannot delete the date row.")

def markcompleted():
    marked = listbox_task.curselection()
    if marked:
        temp = marked[0]
        temp_marked = listbox_task.get(marked)
        temp_marked = temp_marked + " ✔"
        listbox_task.delete(temp)
        listbox_task.insert(temp, temp_marked)
        listbox_task.itemconfig(temp, {'fg': 'green'})

# Initialize the window
window = Tk()
window.title("To-Do List APP")

# Create and pack the task frame
frame_task = Frame(window)
frame_task.pack()

# Create a listbox with a fixed row for the current date
today_date = datetime.today().strftime('%d-%m-%Y')  # Format the date
listbox_task = Listbox(frame_task, bg="black", fg="white", height=15, width=50, font="RobotoCondensed")
listbox_task.insert(0, f"Today's Date: {today_date}")
listbox_task.pack(side=LEFT)

# Create and pack the scrollbar for the listbox
scrollbar_task = Scrollbar(frame_task)
scrollbar_task.pack(side=RIGHT, fill=Y)
listbox_task.config(yscrollcommand=scrollbar_task.set)
scrollbar_task.config(command=listbox_task.yview)

# Create and pack the task entry frame
task_entry_frame = Frame(window)
task_entry_frame.pack()

# Create and pack the entry for adding tasks
entry_task = Text(task_entry_frame, width=40, height=4, borderwidth=10)
entry_task.pack(side=LEFT)

# Create and pack the "Add Task" button with color
add_task_button = Button(task_entry_frame, text="Add Task", width=10, command=addtask, bg="blue", fg="white")
add_task_button.pack(side=LEFT, padx=5)

# Create and pack the button frame
button_frame = Frame(window)
button_frame.pack()

# Create and pack the "Delete Task" button with color
delete_button = Button(button_frame, text="Delete Task", width=15, command=deletetask, bg="red", fg="white")
delete_button.pack(side=LEFT, padx=5)

# Create and pack the "Mark as Completed" button with color
mark_button = Button(button_frame, text="Mark as Completed", width=15, command=markcompleted, bg="green", fg="white")
mark_button.pack(side=LEFT, padx=5)

# Start the main event loop
window.mainloop()
