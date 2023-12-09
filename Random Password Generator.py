import random
import string
import tkinter as tk
from tkinter import messagebox


# Function to generate a random password
def generate_password():
    # Get user input for password length
    try:
        password_length = int(length_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for password length.")
        return

    # Get user preferences for character types
    use_letters = letters_var.get()
    use_numbers = numbers_var.get()
    use_symbols = symbols_var.get()

    # Check if at least one character type is selected
    if not (use_letters or use_numbers or use_symbols):
        messagebox.showerror("Error", "Please select at least one character type.")
        return

    # Define character sets based on user preferences
    characters = ""
    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    # Generate the random password
    password = "".join(random.choice(characters) for _ in range(password_length))

    # Display the generated password
    password_label.config(text=password)


# Function to increment password length
def increment_length():
    current_length = int(length_entry.get())
    if current_length < 99:
        new_length = current_length + 1
        length_entry.delete(0, tk.END)
        length_entry.insert(0, new_length)

# Function to decrement password length
def decrement_length():
    current_length = int(length_entry.get())
    if current_length > 0:
        new_length = current_length - 1
        length_entry.delete(0, tk.END)
        length_entry.insert(0, new_length)

# Function to copy the password to clipboard
def copy_to_clipboard():
    password = password_label.cget("text")
    window.clipboard_clear()
    window.clipboard_append(password)


# Create the main window
window = tk.Tk()
window.title("Random Password Generator")


# Create and pack password length entry and arrows
length_frame = tk.Frame(window)
length_frame.pack()

length_label = tk.Label(length_frame, text="Password Length:")
length_label.pack(side=tk.LEFT)

# Start password length at 0
length_entry = tk.Entry(length_frame, width=5, insertbackground="black", textvariable=tk.IntVar(value=0))
length_entry.pack(side=tk.LEFT)

up_arrow = tk.Button(length_frame, text="▲", command=increment_length)
up_arrow.pack(side=tk.LEFT)

down_arrow = tk.Button(length_frame, text="▼", command=decrement_length)
down_arrow.pack(side=tk.LEFT)

# Create and pack character type checkboxes
letters_var = tk.IntVar(value=1)
letters_checkbox = tk.Checkbutton(window, text="Letters", variable=letters_var)
letters_checkbox.pack()

numbers_var = tk.IntVar(value=1)
numbers_checkbox = tk.Checkbutton(window, text="Numbers", variable=numbers_var)
numbers_checkbox.pack()

symbols_var = tk.IntVar(value=1)
symbols_checkbox = tk.Checkbutton(window, text="Symbols", variable=symbols_var)
symbols_checkbox.pack()

# Create and pack generate and copy-to-clipboard buttons
generate_button = tk.Button(window, text="Generate Password", command=generate_password)
generate_button.pack()

password_label = tk.Label(window, text="")
password_label.pack()

copy_button = tk.Button(window, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.pack()

window.mainloop()