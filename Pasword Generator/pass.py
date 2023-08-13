import tkinter as tk
import random
import string


def generate_password():
    password_length = int(password_length_entry.get())

    if password_length <= 0:
        password_result.set("Invalid password length.")
        return

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(password_length))

    password_result.set(password)


# Create the main Tkinter window
root = tk.Tk()
root.title("Password Generator")

# Password Length Entry
password_length_label = tk.Label(root, text="Enter password length:")
password_length_label.pack()

password_length_entry = tk.Entry(root)
password_length_entry.pack()

# Generate Button
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack()

# Password Result
password_result = tk.StringVar()
password_result_label = tk.Label(root, textvariable=password_result)
password_result_label.pack()

# Run the Tkinter event loop
root.mainloop()
