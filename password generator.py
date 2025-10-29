import random
import pyperclip
import time
from tkinter import simpledialog, ttk, messagebox
from tkinter.font import Font
from tkinter.ttk import *
from tkinter import *
from PIL import Image, ImageTk
from array import array
from ctypes import alignment
from sqlite3.dbapi2 import Cursor
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet
import re

# Root window for loading screen
root = Tk()
root.geometry("600x400+100+100")
root.title("Password Generator")
icon_image = Image.open("C:\\Users\\jashk\\OneDrive\\Desktop\\PBL project\\pic\\icon.ico")
icon = ImageTk.PhotoImage(icon_image)
root.iconphoto(True, icon)

# Loading screen
bg = Image.open("C:\\Users\\jashk\\OneDrive\\Desktop\\PBL project\\pic\\password.jpg")
bg = bg.resize((600, 400))
bg = ImageTk.PhotoImage(bg)

canvas1 = Canvas(height=600, width=600)
canvas1.create_image(0, 0, anchor=NW, image=bg)
canvas1.pack()

bar = Progressbar(canvas1, orient=HORIZONTAL, length=200)
bar.place(x=200, y=300)
bar['value'] = 0

def update_progress():
    if bar['value'] < 100:
        bar['value'] += 1
        root.after(10, update_progress)  # Schedule the function to run again in 10 milliseconds

update_progress()

while bar['value'] < 100:
    bar['value'] += 1
    root.update()
    time.sleep(0.005)

root.destroy()

# Password Generator window
window = Tk()
window.geometry('900x500')
window.configure(bg='azure2')
window.title("Password Generator")
window.resizable(0, 0)

# Styling
window.style = ttk.Style(window)
font = Font(family='Arial', size=16)

window.style.configure("TLabel", font=font)
window.style.configure("TButton", font=font)
window.style.configure("TSpinbox", font=Font(family='Helvetica', size=12))

# Heading
heading = ttk.Label(window, text='Password Generator', style="TLabel")
heading.config(font=("Arial", 27))
heading.pack(pady=20)

# Spinboxes for customizing password
spinbox_style = "TSpinbox"
spinbox_width = 10

options = [("letters", 0), ("digits", 0), ("symbols", 0)]
spinboxes = []

for label_text, default_value in options:
    label = ttk.Label(window, text=f"Select number of {label_text}", style="TLabel")
    label.pack()
    spinbox = ttk.Spinbox(window, from_=0, to=11, textvariable=IntVar(value=default_value), width=spinbox_width, style=spinbox_style)
    spinbox.pack()
    spinboxes.append(spinbox)

# Password result
password_string = StringVar()

def Copy_password():
    password = password_string.get()
    pyperclip.copy(password)
    copy_button["state"] = "disabled"
    messagebox.showinfo("Copied", f"Password '{password}' copied to clipboard.")


def generate():
    copy_button["state"] = "normal"
    password = []
    digits = '1234567890'
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    symbols = '#$%&()*+-./:<>?@[]^_{}'

    for spinbox, char_set in zip(spinboxes, [letters, digits, symbols]):
        for _ in range(int(spinbox.get())):
            password.append(random.choice(char_set))

    random.shuffle(password)
    password_string.set("".join(password))

copy_button = ttk.Button(window, text='COPY', command=Copy_password, state='enabled')
copy_button.pack(pady=10)

entry = ttk.Entry(window, textvariable=password_string)
entry.pack()

generate_button = ttk.Button(window, text="GENERATE PASSWORD", command=generate)
generate_button.pack(pady=20)

def analyze_password_strength():
    password = password_string.get()
    strength = calculate_password_strength(password)
    messagebox.showinfo("Password Strength", f"Password Strength: {strength}")

def calculate_password_strength(password):
    # Minimum length requirement
    if len(password) < 8:
        return "Weak"

    # Check for uppercase, lowercase, digits, and special characters
    has_uppercase = re.search(r'[A-Z]', password)
    has_lowercase = re.search(r'[a-z]', password)
    has_digit = re.search(r'\d', password)
    has_special = re.search(r'[!@#$%^&*()_+{}\[\]:;<>,.?~\\]', password)

    # Character diversity and complexity
    character_sets = [has_uppercase, has_lowercase, has_digit, has_special]
    diversity_count = sum(1 for char_set in character_sets if char_set)

    if diversity_count < 3:
        return "Moderate"

    return "Strong"

strength_button = ttk.Button(window, text="Analyze Password Strength", command=analyze_password_strength)
strength_button.pack(pady=20)

window.mainloop()
