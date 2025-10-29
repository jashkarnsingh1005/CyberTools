import tkinter as tk
from PIL import Image, ImageTk 
import subprocess
from tkinter.ttk import *
from tkinter import *
from PIL import Image, ImageTk 
import time 
from tkinter import messagebox
from functools import partial
import os
from tkinter import PhotoImage
from tkinter import ttk
import random


# Root window for loading screen
root = Tk()
root.geometry("600x500+100+100")
root.title("CyberTools")
icon_image = Image.open("C:\\Users\\jashk\\OneDrive\\Desktop\\PBL project\\pic\\icon.ico")
icon = ImageTk.PhotoImage(icon_image)
root.iconphoto(True, icon)

# Loading screen
bg = Image.open("C:\\Users\\jashk\\OneDrive\\Desktop\\PBL project\\pic\\app bg.jpg")
bg = bg.resize((600, 500))
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
    time.sleep(0.02)

root.destroy()

class MarqueeLabel(tk.Label):
    def __init__(self, master, text, y_position, *args, **kwargs):
        tk.Label.__init__(self, master, text=text, *args, **kwargs)
        self.text_width = self.winfo_reqwidth()
        self.current_position = 0
        self.y_position = y_position
        self.move()

    def move(self):
        self.current_position += 1
        if self.current_position > self.winfo_width():
            self.current_position = -self.text_width
        self.place(x=self.current_position, y=self.y_position)
        self.after(10, self.move)
        
class FirstPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg='white')

        frame = tk.Frame(self,bg='white', relief=tk.RIDGE)
        frame.place(x=30, y=280, width=280, height=190)  # Adjust the height as needed

        binary_text_list = [
            "01010101010101",
            "00110011001100",
            "10010010010010",
            "11101110111011",
            "11111110000000",
            "01010101010101"
        ]

        y_positions = [0, 30, 60, 90, 120, 150]  # Adjust the y positions as needed

        for binary_text, y_position in zip(binary_text_list, y_positions):
            binary_label = MarqueeLabel(frame, text=binary_text, y_position=y_position,bg='white',fg="DodgerBlue3", font=("Courier",18,"bold"))
            binary_label.place(x=0, y=0)


        image = Image.open("C:\\Users\\jashk\\OneDrive\\Desktop\\PBL project\\pic\\icon.ico")
        image = image.resize((200, 200))  # Resize the image if needed
        photo = ImageTk.PhotoImage(image)
        image_label = tk.Label(self, image=photo, bg='white')
        image_label.photo = photo  # Prevent the image from being garbage collected
        image_label.place(x=490, y=70)
        
        border = tk.LabelFrame(
            self, text='Login', fg="DodgerBlue2", bg='white', bd=10, font=("Arial", 20,"bold"))
        border.place(x=350, y=250, width=420, height=220)

        Label1 = tk.Label(border, text="Username", fg='white', font=("Arial Bold", 15), bg='DodgerBlue2')
        Label1.place(x=50, y=20)
        Txt1 = tk.Entry(border, fg='white', bg='DodgerBlue2', width=30, bd=5)
        Txt1.place(x=180, y=20)

        Label2 = tk.Label(border, text="Password", fg='white', font=("Arial Bold", 15), bg='DodgerBlue2')
        Label2.place(x=50, y=80)
        TXT2 = tk.Entry(border, fg='white', bg='DodgerBlue2', width=30, show='*', bd=5)
        TXT2.place(x=180, y=80)

        text14 = tk.Label(self, text="CYBER\n     TOOLS", fg="DodgerBlue3", font=("Arial", 47, "bold"), bg='white')
        text14.place(x=10, y=20)
        
        text1 = Label(self, text="The 'CyberTools' app is a Python-based\ngraphical interface that offers a range\nof cybersecurity tools and features", fg="black", font=("Arial", 13), bg='white')
        text1.place(x=10, y=190)



        def verify():
            try:
                with open("C:\\Users\\jashk\\OneDrive\\Desktop\\PBL project\\previous password.txt", "r") as f:
                    info = f.readlines()
                    i = 0
                    for e in info:
                        u, p = e.split(",")
                        if u.strip() == Txt1.get() and p.strip() == TXT2.get():
                            controller.show_frame(SecondPage)
                            i = 1
                            break
                    if i == 0:
                        messagebox.showinfo(
                            "Error", "Please provide the correct username and password!!")
            except:
                messagebox.showinfo(
                    "Error", "Please provide the correct username and password!!")
 
        BTN1 = tk.Button(border, text="LOG IN", fg='white', bg="DodgerBlue2", font=("Arial", 15), command=verify)
        BTN1.place(x=300, y=125)


        def register():
            
            window = tk.Tk()
            window.resizable(0, 0)
            window.configure(bg="DodgerBlue2")
            window.title("Register")
            Label1 = tk.Label(window, text="Username:", font=("Arial", 15), bg="white")
            Label1.place(x=10, y=10)
            txt1 = tk.Entry(window, width=30, bd=5)
            txt1.place(x=200, y=10)
 
            lbl2 = tk.Label(window, text="Password:", font=("Arial", 15), bg="white")
            lbl2.place(x=10, y=60)
            txt2 = tk.Entry(window, width=30, show="*", bd=5)
            txt2.place(x=200, y=60)
 
            lbl3 = tk.Label(window, text="Confirm Password:", font=("Arial", 15), bg="white")
            lbl3.place(x=10, y=110)
            txt3 = tk.Entry(window, width=30, show="*", bd=5)
            txt3.place(x=200, y=110)

 
            def check():
                if txt1.get() != "" and txt2.get() != "" and txt3.get() != "":
                    with open("C:\\Users\\jashk\\OneDrive\\Desktop\\PBL project\\previous password.txt", "a") as f:
            # Register new username and password
                        f.write(txt1.get() + "," + txt3.get() + "\n")
                    messagebox.showinfo("Welcome", "You have registered successfully!!")
                    window.destroy()
                else:
                    messagebox.showinfo("Error", "Please fill in all the fields!")


            btn1 = tk.Button(window, text="Sign in", font=("Arial", 15), bg="bisque", command=check)
            btn1.place(x=220, y=180)

            window.geometry("530x250")
            window.mainloop()

        self.lbl_register = tk.Label(self, text="Register if you don't have an ID", fg='DodgerBlue2',bg='white', cursor="hand2", font=("Arial", 14,"underline"))
        self.lbl_register.bind("<Enter>", self.on_enter)  # Bind function to cursor enter event
        self.lbl_register.bind("<Leave>", self.on_leave)  # Bind function to cursor leave event
        self.lbl_register.bind("<Button-1>", lambda event: register())  # Bind function to label click event
        self.lbl_register.place(x=380, y=420)

    def on_enter(self, event):
        self.lbl_register.config(fg='deep sky blue')  

    def on_leave(self, event):
        self.lbl_register.config(fg='DodgerBlue2')  

class SecondPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,)
        self.controller = controller

        self.configure(bg='DodgerBlue2') 
        self.check_var = tk.BooleanVar()
        self.check_var1 = tk.BooleanVar()
        # Create a Checkbutton
        check_button = Checkbutton(self, text="I read the policies", variable=self.check_var)
        check_button.place(x=310, y=440)

        check_button = Checkbutton(self, text="I agree to the terms and conditions", variable=self.check_var1)
        check_button.place(x=310, y=470)



        # Load your image
        image = Image.open("C:\\Users\\jashk\\OneDrive\\Desktop\\PBL project\\pic\\Disclaimer-Symbol-Transparent-PNG.png")
        image = image.resize((50,50)) 
        img = ImageTk.PhotoImage(image)
        
        # Create a label or canvas to display the image
        image_label = Label(self, image=img)
        image_label.image = img  
        image_label.place(x=360, y=10) 

        text_label = Label(self, text="Terms And Conditions:",fg="white", font=("Arial", 16), bg='DodgerBlue2')
        text_label.place(x=10, y=50)

        text10= Label(self, text="•By downloading, installing, or using the 'CYBERTOOLS', you agree to comply with these terms and conditions.", fg="white", font=("Arial", 12), bg='DodgerBlue2')
        text10.place(x=10, y=80)

        text11 = Label(self, text="If you do not agree with any part of these terms, do not use the App.", fg="white", font=("Arial", 12), bg='DodgerBlue2')
        text11.place(x=10, y=100)

        text_label1 = Label(self, text="•The App is designed for authorized cybersecurity purposes, including, but not limited to, keylogger,cryptography,manager, and security.",fg="white", font=("Arial", 12), bg='DodgerBlue2')
        text_label1.place(x=10, y=120)

        

        text1 = Label(self, text="•Unauthorized use of the App for malicious,illegal or unethical activities is strictly prohibited.", fg="white", font=("Arial", 12), bg='DodgerBlue2')
        text1.place(x=10, y=140)

        text3 = Label(self, text="•Some features of the App may require user registration. You are responsible for maintaining the confidentiality of", fg="white", font=("Arial", 12), bg='DodgerBlue2')
        text3.place(x=10, y=160)

        text5 = Label(self, text="your account information,including your username and password.", fg="white", font=("Arial", 12), bg='DodgerBlue2')
        text5.place(x=10, y=180)

        text6 = Label(self, text="•Users of the App are expected to comply with all applicable local,state,national laws and regulations.", fg="white", font=("Arial", 12), bg='DodgerBlue2')
        text6.place(x=10, y=200)

        text7 = Label(self, text="•We reserve the right to suspend user access to the App at our discretion if the user violates these conditions.", fg="white", font=("Arial", 12), bg='DodgerBlue2')
        text7.place(x=10, y=220)

        text8 = Label(self, text="•While we employ security measures to protect your data, we cannot guarantee the security of any information you ", fg="white", font=("Arial", 12), bg='DodgerBlue2')
        text8.place(x=10, y=240)

        text9 = Label(self, text="transmit or store in the App. Users are encouraged to implement additional security measures as necessary.", fg="white", font=("Arial", 12), bg='DodgerBlue2')
        text9.place(x=10, y=260)

        text14 = Label(self, text="App Usage", fg="white", font=("Arial", 14), bg='DodgerBlue2')
        text14.place(x=10, y=280)

        text15 = Label(self, text="a.Password Manager:It feature of the App is designed to help you securely store and manage your passwords.", fg="white", font=("Arial", 12), bg='DodgerBlue2')
        text15.place(x=10, y=310)

        text16 = Label(self, text="b.Password Generator: It feature provides the ability to create strong, random passwords.", fg="white", font=("Arial", 12), bg='DodgerBlue2')
        text16.place(x=10, y=330)

        text17 = Label(self, text="c.Keylogger: Tool that can record every keystroke that you type into a computer or mobile keyboard. ", fg="white", font=("Arial", 12), bg='DodgerBlue2')
        text17.place(x=10, y=350)

        text18 = Label(self, text="d.Cryptography: It encode and decode information so that it becomes confidential.", fg="white", font=("Arial", 12), bg='DodgerBlue2')
        text18.place(x=10, y=370)
        text19 = Label(self, text="e.Port scanner:A port scanner tool can also be used to scan network ports. ", fg="white", font=("Arial", 12), bg='DodgerBlue2')
        text19.place(x=10, y=390)
        text20 = Label(self, text="f.Image steganography: Technique of hiding secret information within an image.", fg="white", font=("Arial", 12), bg='DodgerBlue2')
        text20.place(x=10, y=410)
        
        text21 = Label(self, text="Click➡️", fg="white", font=("Arial", 25), bg='DodgerBlue2')
        text21.place(x=630, y=10)
        house_button = Button(self, text="🏠", font=("Arial", 18), command=self.open_third_page)
        house_button.place(x=740, y=10)
    
    def open_third_page(self):
        if self.check_var.get() and self.check_var1.get():
            self.controller.show_frame(ThirdPage)
        else:
            messagebox.showerror("Error", "Please agreed Terms and Conditions")


class ThirdPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.configure(bg='DodgerBlue2')
        style = ttk.Style()
        style.configure('TButton', font=("Arial", 24),padding=10,relief='RAISED',width=5,
                        height=5,
                        background='blue', foreground='BLACK')
        style.map('TButton', background=[('active', '#65e7ff')])



    
    

        Button1 = ttk.Button(self, text="🔐", command=self.open_new_window)
        Button1.place(x=60, y=30)
        text14 = Label(self, text="PASSWORD\nMANAGER", fg="BLACK", font=("Arial", 14), bg='DodgerBlue2')
        text14.place(x=60, y=100)


        Button2 = ttk.Button(self, text="📇", command=self.open_new_window1)
        Button2.place(x=240, y=30)
        text15 = Label(self, text="PASSWORD\nGENERATOR", fg="BLACK", font=("Arial", 14), bg='DodgerBlue2')
        text15.place(x=240, y=100)

        Button3 = ttk.Button(self, text="🔠-🔣", command=self.open_new_window2)
        Button3.place(x=60, y=220)
        text16 = Label(self, text="CRYPTOGRAPHY", fg="BLACK", font=("Arial", 14), bg='DodgerBlue2')
        text16.place(x=40, y=290)


        Button4 = ttk.Button(self, text="⌨", command=self.open_new_window3)
        Button4.place(x=240, y=220)
        text17 = Label(self, text="KEYLOGGER", fg="BLACK", font=("Arial", 14), bg='DodgerBlue2')
        text17.place(x=240, y=290)

        Button5 = ttk.Button(self, text="🔌", command=self.open_new_window4)
        Button5.place(x=60, y=380)
        text18= Label(self, text="PORT SCANNER", fg="BLACK", font=("Arial", 14), bg='DodgerBlue2')
        text18.place(x=50, y=450)

        Button6 = ttk.Button(self, text="   🖼️", command=self.open_new_window5)
        Button6.place(x=240, y=380)
        text19= Label(self, text="IMAGE STEGANO-\nGRAPHY", fg="BLACK", font=("Arial", 14), bg='DodgerBlue2')
        text19.place(x=220, y=450)

        BTN1 = tk.Button(
        self,
        text="🎁",
    fg='black',width='5',height='2',
    bg="SeaGreen3",  # Use a modern color, you can replace this with your preferred color",  # Use a modern color, you can replace this with your preferred color
    activebackground="azure2",  # Change color when the button is pressed
    font=("Helvetica", 24, "bold"),  # Use a bold font for better visibility
    bd=0,  # Remove border
    relief=tk.FLAT,  # Make the button flat
    command=self.open_new_window6
)
        BTN1.place(x=540, y=290)
        headingFrame1 = Frame(self, bg="gray91", bd=5)
        headingFrame1.place(relx=0.75, rely=0.1, relwidth=0.4, relheight=0.16, anchor='n')

        headingLabel = Label(headingFrame1, text="PLAY THE QUIZ!!!", fg='grey19', font=('Courier', 20, 'bold'))
        headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

        text20= Label(self, text="TO START THE QUIZ", fg="BLACK", font=("Arial", 15), bg='DodgerBlue2')
        text20.place(x=490, y=180)

        text21= Label(self, text="CLICK IT⬇️", fg="BLACK", font=("Arial", 18), bg='DodgerBlue2')
        text21.place(x=530, y=240)


    def open_new_window(self):
        try:
            subprocess.run(['python',"C:\\Users\\jashk\\OneDrive\\Desktop\\PBL project\\passmn.py"])
        except Exception as e:
            messagebox.showerror("ERROR",f"an error occurred: {str(e)}")

    def open_new_window1(self):
        try:
            subprocess.run(['python','C:\\Users\\jashk\\OneDrive\\Desktop\\PBL project\\password generator.py'])
        except Exception as e:
            messagebox.showerror("ERROR",f"an error occurred: {str(e)}")

        
    def open_new_window2(self):
        try:
            subprocess.run(['python','C:\\Users\\jashk\\OneDrive\\Desktop\\PBL project\\e and d.py'])
        except Exception as e:
            messagebox.showerror("ERROR",f"an error occurred: {str(e)}")

    def open_new_window3(self):
        try:
            subprocess.run(['python','C:\\Users\\jashk\\OneDrive\\Desktop\\PBL project\\Edukeylogger.py'])
        except Exception as e:
            messagebox.showerror("ERROR",f"an error occurred: {str(e)}")

    def open_new_window4(self):
        try:
            subprocess.run(['python',"C:\\Users\\jashk\\OneDrive\\Desktop\\PBL project\\portscanner.py"])
        except Exception as e:
            messagebox.showerror("ERROR",f"an error occurred: {str(e)}")

    def open_new_window5(self):
        try:
            subprocess.run(['python','C:\\Users\\jashk\\OneDrive\\Desktop\\PBL project\\steganography.py'])
        except Exception as e:
            messagebox.showerror("ERROR",f"an error occurred: {str(e)}")

    def open_new_window6(self):
        try:
            subprocess.run(['python',"C:\\Users\\jashk\\OneDrive\\Desktop\\PBL project\\quiz.py"])
        except Exception as e:
            messagebox.showerror("ERROR",f"an error occurred: {str(e)}")
    

        


class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # creating a window
        window = tk.Frame(self)
        window.pack()

        window.grid_rowconfigure(0, minsize=500)
        window.grid_columnconfigure(0, minsize=800)

        self.frames = {}
        for F in (FirstPage, SecondPage, ThirdPage):
            frame = F(window, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(FirstPage)

    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()
        self.title("CyberTools")


app = Application()

app.maxsize(800,500)
app.mainloop()