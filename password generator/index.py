import tkinter as tk
from tkinter import ttk
import random
import string

def generate_password(length, use_uppercase, use_lowercase, use_digits, use_special_chars):
    characters = ""
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation

    if not characters:
        return "Please select at least one character set."

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_password_button_click():
    try:
        length = int(length_entry.get())
        if length <= 0:
            result_label.config(text="Please enter a valid length greater than 0.", foreground="red")
            return

        use_uppercase = uppercase_var.get()
        use_lowercase = lowercase_var.get()
        use_digits = digits_var.get()
        use_special_chars = special_chars_var.get()

        password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_special_chars)
        result_label.config(text=f"Generated Password: {password}", foreground="black")

    except ValueError:
        result_label.config(text="Please enter a valid numerical value for the password length.", foreground="red")


# Create the main window
window = tk.Tk()
window.title("Password Generator")

# Create and pack the widgets
length_label = ttk.Label(window, text="Enter Password Length:")
length_label.pack(pady=10)

length_entry = ttk.Entry(window)
length_entry.pack(pady=10)

options_frame = ttk.Frame(window)
options_frame.pack(pady=10)

uppercase_var = tk.BooleanVar()
uppercase_checkbox = ttk.Checkbutton(options_frame, text="Uppercase", variable=uppercase_var)
uppercase_checkbox.grid(row=0, column=0, padx=5)

lowercase_var = tk.BooleanVar()
lowercase_checkbox = ttk.Checkbutton(options_frame, text="Lowercase", variable=lowercase_var)
lowercase_checkbox.grid(row=0, column=1, padx=5)

digits_var = tk.BooleanVar()
digits_checkbox = ttk.Checkbutton(options_frame, text="Digits", variable=digits_var)
digits_checkbox.grid(row=0, column=2, padx=5)

special_chars_var = tk.BooleanVar()
special_chars_checkbox = ttk.Checkbutton(options_frame, text="Special Characters", variable=special_chars_var)
special_chars_checkbox.grid(row=0, column=3, padx=5)

generate_button = ttk.Button(window, text="Generate Password", command=generate_password_button_click)
generate_button.pack(pady=10)

result_label = ttk.Label(window, text="")
result_label.pack(pady=10)

# Start the main event loop
window.mainloop()
