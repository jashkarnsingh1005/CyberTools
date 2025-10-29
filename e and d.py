from tkinter import *
import base64
from tkinter import messagebox
import tkinter.font as font
import pyperclip
from tkinter.ttk import *
from tkinter import *
from PIL import Image,ImageTk
import time 
from tkinter import messagebox
from functools import partial
import os

root=Tk()
root.geometry("500x500+100+100")
root.title("CRYPTOGRAPHY")
icon_image = Image.open("C:\\Users\\jashk\\OneDrive\\Desktop\\PBL project\\pic\\icon.ico")
icon = ImageTk.PhotoImage(icon_image)
root.iconphoto(True, icon)
bg=Image.open("C:\\Users\\jashk\\OneDrive\\Desktop\\PBL project\\pic\\e and d.png")
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

def encode(key, message):
    enc = []
    for i in range(len(message)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(message[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

# Define the decryption function
def decode(key, message):
    dec = []
    message = base64.urlsafe_b64decode(message).decode()
    for i in range(len(message)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(message[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)

def copy_result():
  result=Output.get()
  if result:
    pyperclip.copy(result)
    messagebox.showinfo("Copied","Result copied to clipboard")
  else:
    messagebox.showinfo("no result","there is no result copied")

wn = Tk()
wn.geometry("500x500")
wn.configure(bg='azure2')
wn.title("CRYPTOGRAPHY")

Message = StringVar()
key = StringVar()
mode = IntVar()
Output = StringVar()
headingFrame1 = Frame(wn,bg="gray91",bd=5)
headingFrame1.place(relx=0,rely=0.1,relwidth=1,relheight=0.16)
headingLabel = Label(headingFrame1, text=" CRYPTOGRAPHY", fg='grey19', font=('Courier',15,'bold'))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
label1 = Label(wn, text='Enter the Message', font=('Courier',10))
label1.place(x=10,y=150)
msg = Entry(wn,textvariable=Message, width=35, font=('calibre',10,'normal'))
msg.place(x=200,y=150)
label2 = Label(wn, text='Enter the key', font=('Courier',10))
label2.place(x=10,y=200)
InpKey = Entry(wn, textvariable=key, width=35,font=('calibre',10,'normal'))
InpKey.place(x=200,y=200)
label3 = Label(wn, text='Check one of encrypt or decrypt', font=('Courier',10))
label3.place(x=10,y=250)
Radiobutton(wn, text='Encrypt', variable=mode, value=1).place(x=100,y=300)
Radiobutton(wn, text='Decrypt', variable=mode, value=2).place(x=200,y=300)
label3 = Label(wn, text='Result', font=('Courier',10))
label3.place(x=10,y=350)
res = Entry(wn,textvariable=Output, width=35, font=('calibre',10,'normal'))
res.place(x=200,y=350)

def Result():
  msg = Message.get()
  k= key.get()
  i = mode.get()
  if not k:
     messagebox.showinfo('CRYPTOGRAPHY',"please enter a key")
  elif (i==1):
    Output.set(encode(k, msg))
  elif(i==2):
    Output.set(decode(k, msg))
  else:
    messagebox.showinfo('CRYPTOGRAPHY', 'Please Choose one of Encryption or Decryption. Try again.')

def Reset():
  Message.set("")
  key.set("")
  mode.set(0)
  Output.set("")
ShowBtn = Button(wn,text="Show Message",bg='lavender blush2', fg='black',width=15,height=1,command=Result)
ShowBtn['font'] = font.Font( size=12)
ShowBtn.place(x=180,y=400)
ResetBtn = Button(wn, text='Reset', bg='honeydew2', fg='black', width=15,height=1,command=Reset)
ResetBtn['font'] = font.Font( size=12)
ResetBtn.place(x=15,y=400)
QuitBtn = Button(wn, text='Exit', bg='old lace', fg='black',width=15,height=1, command=wn.destroy)
QuitBtn['font'] = font.Font( size=12)
CopyBtn=Button(wn,text="copy",bg="light cyan",fg="black",width="15",height=1,command=copy_result)
CopyBtn['font'] = font.Font( size=12)
CopyBtn.place(x=15,y=450)
QuitBtn.place(x=345,y=400)
wn.mainloop()