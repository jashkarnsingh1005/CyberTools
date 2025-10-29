from tkinter.ttk import *
from tkinter import *
from PIL import Image,ImageTk
import time 
from tkinter import messagebox
from functools import partial
import os

root=Tk()
root.geometry("500x500+100+100")
root.title("PASSWORD MANAGER")
icon_image = Image.open("C:\\Users\\jashk\\OneDrive\\Desktop\\PBL project\\pic\\icon.ico")
icon = ImageTk.PhotoImage(icon_image)
root.iconphoto(True, icon)
bg=Image.open("C:\\Users\\jashk\\OneDrive\\Desktop\\PBL project\\pic\\pass mn.jpg")
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


def decrypt(data):
   global shift
   decrypted=""
   for i in range(len(data)):
      char=data[i]
      if char.isupper():
         decrypted += chr((ord(char) - shift - 65) % 26 + 65)
      elif char.islower():
         decrypted += chr((ord(char) - shift - 97) %26 +97 )
      elif char.isdigit():
         num=(int(char) - shift) %10
         decrypted += str(num)
   return decrypted
   

def encrypt(data):
   global shift
   encrypted=""
   for i in range(len(data)):
      char=data[i]
      if char.isupper():
         encrypted += chr((ord(char)+ shift - 65) % 26 + 65)
      elif char.islower():
         encrypted += chr((ord(char)+shift - 97) %26 +97 )
      elif char.isdigit():
         num=(int(char) + shift) %10
         encrypted += str(num)
   return encrypted


def clear(menu):
   fw=open("C:\\Users\\jashk\\OneDrive\\Desktop\\PBL project\\pass.txt",'w').close()
   messagebox.showinfo("Success","Entries deleted successfully")
   menu.destroy()
   main()


def save(website,username,password):
   fw=open("C:\\Users\\jashk\\OneDrive\\Desktop\\PBL project\\pass.txt",'a')
   website=encrypt(website)
   username=encrypt(username)
   password=encrypt(password)
   fw.write(website+"|"+username+"|"+password+'\n')
   fw.close()


def add_pass(web,user,pasw,add_main):
   x=True
   website=web.get()
   username=user.get()
   password=pasw.get()
   if website=="" or username=="" or password=="":
      x=False
      messagebox.showwarning("Alert","Empty Fields not allowed")
   if x is True:
      save(website,username,password)
      messagebox.showinfo("Success","Password Added Successfully")
      add_main.destroy()
      main()


def back(add_main):
   add_main.destroy()
   main()


def add(root):
   root.destroy()
   add_main=Tk()
   add_main.geometry("600x400+100+100")
   add_main.title("Add Password")
   add_main.configure(bg="azure2")
   canvas1=Canvas(height=600,width=600, bg="azure2")
   canvas1.create_image(0,0,anchor=NW)
   canvas1.pack()
   ent_web=Entry(width=30, bg="old lace")
   ent_user=Entry(width=30, bg="old lace")
   ent_pass=Entry(width=30, bg="old lace")
   canvas1.create_text(160,120,text="Website",fill="black",font=("Helvetica",16,"italic bold"))
   canvas1.create_text(160,180,text="Username",fill="black",font=("Helvetica",16,"italic bold"))
   canvas1.create_text(160,240,text="Password",fill="black",font=("Helvetica",16,"italic bold"))
   canvas1.create_window(340,120,window=ent_web)
   canvas1.create_window(340,180,window=ent_user)
   canvas1.create_window(340,240,window=ent_pass)
   add_btn=Button(text="Add",font=("Calibri",14,"bold"),bg="#104E8B",fg="#E2DFD2",width=5,command=partial(add_pass,ent_web,ent_user,ent_pass,add_main))
   canvas1.create_window(250,320,window=add_btn)
   cancel_btn=Button(text="Cancel",font=("Calibri",14,"bold"),bg="#104E8B",fg="#E2DFD2",width=7,command=partial(back,add_main))
   canvas1.create_window(330,320,window=cancel_btn)
   add_main.mainloop()


def view_pass():
   filesize = os.path.getsize("C:\\Users\\jashk\\OneDrive\\Desktop\\PBL project\\pass.txt")
   menu=Tk()
   menu.title("PASSWORD MANAGER")
   menu.configure(bg="azure2")
   menu.geometry("600x400+100+100")
   canvas1=Canvas(height=400,width=600,bg='azure2')
   canvas1.create_image(0,0,anchor=NW)
   canvas1.pack()
   canvas1.create_text(300,30,text="Your Saved Passwords",font=("Calibri",25,"italic bold"),fill="black")
   if os.path.getsize("C:\\Users\\jashk\\OneDrive\\Desktop\\PBL project\\pass.txt")==0:
      canvas1.create_text(300,200,text="No password saved yet",font=("Helvetica",20,"italic bold"),fill="black")
      add_btn=Button(text="Add password",font=("Helvetica",12),bg="#c80815",fg="white",width=13,command=partial(back,menu))
      canvas1.create_window(290,350,window=add_btn)
   else:
      canvas1.create_text(120,100,text="Website",font=("Calibri",13," italic bold underline"),fill="grey19")
      canvas1.create_text(280,100,text="Username",font=("Calibri",13,"italic bold underline"),fill="grey19")
      canvas1.create_text(450,100,text="Password",font=("Calibri",13,"italic bold underline"),fill="grey19")
      fw=open("C:\\Users\\jashk\\OneDrive\\Desktop\\PBL project\\pass.txt")
      x=110
      for line in fw:
         x=x+25
         line=line.rstrip()
         sentence=line.split("|")
         website=decrypt(sentence[0])
         username=decrypt(sentence[1])
         password=decrypt(sentence[2])
         canvas1.create_text(120,x,text=website,font=("Helvetica",10,"italic bold"),fill="black")
         canvas1.create_text(280,x,text=username,font=("Helvetica",10,"italic bold"),fill="black")
         canvas1.create_text(450,x,text=password,font=("Helvetica",10,"italic bold"),fill="black")
      clr_btn=Button(text="Clear All",font=("Helvetica",12),bg="#c80815",fg="white",width=8,command=partial(clear,menu))
      back_btn=Button(text="Go Back",font=("Helvetica",12),bg="#c80815",fg="white",width=8,command=partial(back,menu))
      canvas1.create_window(240,350,window=clr_btn)
      canvas1.create_window(350,350,window=back_btn)
   menu.mainloop()


def check(ent_pass,pas):
   global c
   ans=ent_pass.get()
   if ans == "jash":
      messagebox.showinfo("Success","Welcome!")
      pas.destroy()
      view_pass()
   else:
      if c<3:
         ent_pass.delete(0,'end')
         x=3-c
         messagebox.showwarning("Incorrect",f"Password Incorrect\n{x} try left")
         c=c+1
      else:
         messagebox.showerror("Login Failed","No more try left")
         pas.destroy()
         main()


def view(root):
   root.destroy()
   pas=Tk()
   pas.title("PASSWORD MANAGER")
   pas.configure(bg="azure2")
   pas.geometry("300x200+500+300")
   lab=Label(pas,text="Enter Password",bg="old lace",font=("Arial",20,UNDERLINE))
   lab.pack(pady=10)
   ent_pass=Entry(pas,show="*")
   ent_pass.pack(pady=5)
   submit=Button(pas,text="Login",bg='old lace',command=partial(check,ent_pass,pas))
   submit.pack(pady=20)
   pas.mainloop()


def exit(root):
   root.destroy()  


def main():
   root=Tk()
   root.title("PASSWORD MANAGER")
   root.geometry("600x400+100+100")
   root.configure(bg="azure2")
   canvas1=Canvas(root,height=400,width=600,bg="azure2")
   canvas1.create_image(0,0,anchor=NW)
   canvas1.pack()
   add_img=Image.open("C:\\Users\\jashk\\Downloads\\pass2.jpg")  
   add_img=add_img.resize((80,80))
   add_img=ImageTk.PhotoImage(add_img)
   view_img=Image.open("C:\\Users\\jashk\\Downloads\\vpass.png")
   view_img=view_img.resize((75,75))
   view_img=ImageTk.PhotoImage(view_img)
   btn=Button(text="Add new password",bg="#40B5AD",fg="#162252",width=18,command=partial(add,root),font=("Helvetica 13 italic bold"),relief="raised")
   btn2=Button(text="View saved passwords",bg="#104E8B",fg="#E2DFD2",width=20,command=partial(view,root),font=("Helvetica 13 italic bold"),relief="raised")
   exit_btn=Button(text="Exit",command=partial(exit,root),font=("Helvetica",12,"bold italic"),bg="#c80815",fg="white",width=5,relief="raised")
   canvas1.create_image(140,100,anchor=NW,image=add_img)
   canvas1.create_window(335,140,window=btn)
   canvas1.create_image(142,230,anchor=NW,image=view_img)
   canvas1.create_window(345,265,window=btn2)
   canvas1.create_window(530,370,window=exit_btn)
   root.mainloop()

main()
root.mainloop()