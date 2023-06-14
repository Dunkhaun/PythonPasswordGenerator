import random
import string
import tkinter as tk
import tkinter.messagebox as messagebox
import tkinter.ttk as ttk

def generate_password(length, uppercase, lowercase, numbers, special_chars):
    # Define the character sets based on user criteria
    character_set = ""
    if uppercase:
        character_set += string.ascii_uppercase
    if lowercase:
        character_set += string.ascii_lowercase
    if numbers:
        character_set += string.digits
    if special_chars:
        character_set += string.punctuation

    # Generate the password
    password = ''.join(random.choice(character_set) for _ in range(length))
    return password

def generate():
    # Get user criteria for password generation
    length = int(length_entry.get())
    uppercase = uppercase_var.get()
    lowercase = lowercase_var.get()
    numbers = numbers_var.get()
    special_chars = special_chars_var.get()

    # Generate the password
    password = generate_password(length, uppercase, lowercase, numbers, special_chars)
    password_text.set(password)

def copy_password():
    password = password_text.get()
    if password:
        window.clipboard_clear()
        window.clipboard_append(password)
        messagebox.showinfo("Password Copied", "Password copied to clipboard.")
    else:
        messagebox.showwarning("No Password", "Generate a password first.")

# Create the main window
window = tk.Tk()
window.title("Password Generator")

# Length label and entry
length_label = tk.Label(window, text="Password Length:")
length_label.pack()
length_entry = tk.Entry(window)
length_entry.pack()

# Checkbox options
uppercase_var = tk.BooleanVar()
uppercase_check = tk.Checkbutton(window, text="Include Uppercase Letters", variable=uppercase_var)
uppercase_check.pack()

lowercase_var = tk.BooleanVar()
lowercase_check = tk.Checkbutton(window, text="Include Lowercase Letters", variable=lowercase_var)
lowercase_check.pack()

numbers_var = tk.BooleanVar()
numbers_check = tk.Checkbutton(window, text="Include Numbers", variable=numbers_var)
numbers_check.pack()

special_chars_var = tk.BooleanVar()
special_chars_check = tk.Checkbutton(window, text="Include Special Characters", variable=special_chars_var)
special_chars_check.pack()

# Generate button
generate_button = tk.Button(window, text="Generate Password", command=generate)
generate_button.pack()

# Copy button
copy_button = tk.Button(window, text="Copy Password", command=copy_password)
copy_button.pack()

# Generated password label
password_text = tk.StringVar()
password_label = tk.Label(window, textvariable=password_text)
password_label.pack()

# Start the GUI event loop
window.mainloop()
