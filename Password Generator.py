import tkinter as tk
import random
import string

def generate_password():
    length = int(text_box2.get(1.0, tk.END))
    characters = string.ascii_lowercase + string.ascii_lowercase +string.digits + string.punctuation
    password = "".join(random.choice(characters) for _ in range(length))
    text_box3.delete(1.0, tk.END)
    text_box3.insert(1.0, password)
def accept():
    username = text_box1.get("1.0", tk.END)
    password = text_box3.get("1.0", tk.END)
    print("Accepted Password:")
    print("Username:", username)
    print("Password:", password)

def reset():
    text_box1.delete(1.0, tk.END)
    text_box2.delete(1.0, tk.END)
    text_box3.delete(1.0, tk.END)

window = tk.Tk()
window.geometry("600x430")
window.title("Password Generator")

label0 = tk.Label(window, text="Password Generator", font=("Times New Roman", 28))
label0.grid(pady=14, row=0, column=1, columnspan=2)

label1 = tk.Label(window, text="Enter username", font=("Arial", 10))
label1.grid(pady=5, row=2, column=0, sticky=tk.E)

label2 = tk.Label(window, text="Enter password length", font=("Arial", 10))
label2.grid(pady=5, row=4, column=0, sticky=tk.E)

label3 = tk.Label(window, text="Generated password", font=("Arial", 10))
label3.grid(pady=5, row=6, column=0, sticky=tk.E)

text_box1 = tk.Text(window, font=("Arial", 16), height=1, width=30)
text_box1.grid(pady=5, padx=10, row=2, column=1, columnspan=2)

text_box2 = tk.Text(window, font=("Arial", 16), height=1, width=30)
text_box2.grid(pady=5, padx=10, row=4, column=1, columnspan=2)

text_box3 = tk.Text(window, font=("Arial", 16), height=1, width=30)
text_box3.grid(pady=5, padx=10, row=6, column=1, columnspan=2)

btn_generate = tk.Button(window, text="Generate Password", font=("Arial Rounded MT Bold", 16), bg="Sky Blue", width=16,command=generate_password)
btn_generate.grid(pady=19, row=10, column=1, padx=10, columnspan=2)

btn_accept = tk.Button(window, text="Accept", font=("Arial Rounded MT Bold", 16), bg="Yellow", width=16,command = accept)
btn_accept.grid(pady=10, row=12, column=1, padx=10, columnspan=2)

btn_reset = tk.Button(window, text="Reset", font=("Arial Rounded MT Bold", 16), bg="Red", width=16,command = reset)
btn_reset.grid(pady=10, row=14, column=1, padx=10, columnspan=2)

window.mainloop()
