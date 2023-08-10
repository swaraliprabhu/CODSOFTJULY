import random
import string
import tkinter as tk

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_and_display_password():
    try:
        password_length = int(entry_length.get())
        if password_length <= 0:
            password_output.delete("1.0", tk.END)
            password_output.insert(tk.END, "Password length must be a positive integer.")
        else:
            generated_password = generate_password(password_length)
            password_output.delete("1.0", tk.END)
            password_output.insert(tk.END, generated_password)
    except ValueError:
        password_output.delete("1.0", tk.END)
        password_output.insert(tk.END, "Invalid input. Please enter a valid integer for password length.")

def accept_password():
    # You can implement the logic to store the username and generated password here
    print("Username:", entry_username.get())
    print("Generated Password:", password_output.get("1.0", tk.END))

def reset_fields():
    entry_username.delete(0, tk.END)
    entry_length.delete(0, tk.END)
    password_output.delete("1.0", tk.END)

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Create widgets
username_label = tk.Label(root, text="Username:")
username_label.pack(pady=5)

entry_username = tk.Entry(root, width=15)
entry_username.pack(pady=5)

length_label = tk.Label(root, text="Enter the desired length of the password:")
length_label.pack(pady=5)

entry_length = tk.Entry(root, width=15)
entry_length.pack(pady=5)

generate_btn = tk.Button(root, text="Generate Password", command=generate_and_display_password)
generate_btn.pack(pady=10)

password_output = tk.Text(root, width=30, height=5)
password_output.pack(pady=5)

accept_btn = tk.Button(root, text="Accept", command=accept_password)
accept_btn.pack(side=tk.LEFT, padx=5, pady=10)

reset_btn = tk.Button(root, text="Reset", command=reset_fields)
reset_btn.pack(side=tk.RIGHT, padx=5, pady=10)

# Start the main event loop
root.mainloop()
