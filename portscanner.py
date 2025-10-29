import socket
import threading
import time
from tkinter import simpledialog, messagebox
from tkinter.ttk import *
from tkinter import *
from PIL import Image,ImageTk
import time 



root=Tk()
root.geometry("500x500+100+100")
root.title("PORT SCANNER")
icon_image = Image.open("C:\\Users\\jashk\\OneDrive\\Desktop\\PBL project\\pic\\icon.ico")
icon = ImageTk.PhotoImage(icon_image)
root.iconphoto(True, icon)
bg=Image.open("C:\\Users\\jashk\\OneDrive\\Desktop\\PBL project\\pic\\port.jpg")
bg=bg.resize((500,500))
bg=ImageTk.PhotoImage(bg)
canvas1=Canvas(height=600,width=600)
canvas1.create_image(0,0,anchor=NW,image=bg)
canvas1.pack()
bar=Progressbar(canvas1,orient=HORIZONTAL,length=200)
bar.place(x=150,y=350)
bar['value']=0
while bar['value']<100:
    bar['value']+=1
    root.update()
    time.sleep(0.005)
root.destroy()

shift=11
c=1


# Scan Vars
ip_s = 1
ip_f = 1024
log = []
ports = []
target = ""

# Scanning Functions
def scanPort(target, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(4)
        c = s.connect_ex((target, port))
        if c == 0:
            m = f" Port {port}\t[open]"
            log.append(m)
            ports.append(port)
            listbox.insert(END, m)
            updateResult()
        s.close()
    except OSError as e:
        print(f"> Error: {e}. Port {port}")
    except Exception as e:
        print(f"> Error: {e}")

def updateResult():
    rtext = f" [ {len(ports)} / {ip_f} ] ~ {target}"
    L27.configure(text=rtext)

def startScan():
    global ports, log, target, ip_f, ip_s
    clearScan()
    log = []
    ports = []
    ip_s = int(L24.get())
    ip_f = int(L25.get())
    target = L22.get()
    log.append("> PORT SCANNER")
    log.append("=" * 14 + "\n")
    log.append(f" Target:\t{target}")

    try:
        target_ip = socket.gethostbyname(target)
        log.append(f" IP Adr.:\t{target_ip}")
        log.append(f" Ports:\t[ {ip_s} / {ip_f} ]")
        log.append("\n")
        while ip_s <= ip_f:
            try:
                scan = threading.Thread(target=scanPort, args=(target_ip, ip_s))
                scan.setDaemon(True)
                scan.start()
            except Exception as e:
                print(f"> Error starting scan: {e}")
                time.sleep(0.01)
            ip_s += 1
    except socket.gaierror:
        m = f"> Target {target} not found."
        log.append(m)
        listbox.insert(0, m)

def saveScan():
    global log, target, ports, ip_f
    log[5] = f" Result:\t[ {len(ports)} / {ip_f} ]\n"
    with open("C:\\Users\\jashk\\OneDrive\\Desktop\\PBL project\\portscanner.txt", mode="wt", encoding="utf-8") as myfile:
        myfile.write("\n".join(log))

def viewSavedResult():
    # Password prompt
    password = simpledialog.askstring("Password", "Enter the password:", show="*")
    if password == "jash":  # Replace "jash" with your actual password
        try:
            file_path ="C:\\Users\\jashk\\OneDrive\\Desktop\\PBL project\\portscanner.txt"
            with open(file_path, "r", encoding="utf-8") as myfile:
                result = myfile.read()
                text_window = Toplevel()
                text_window.title("Saved Result")
                text = Text(text_window)
                text.insert(INSERT, result)
                text.pack()
        except FileNotFoundError:
            messagebox.showinfo("File Not Found", "The result file does not exist.")
    else:
        messagebox.showinfo("Access Denied", "Incorrect password.")

def clearScan():
    listbox.delete(0, END)

# GUI
gui = Tk()
gui.title("PORT SCANNER")
gui.geometry("400x600+20+20")

# Colors
m1c = "black"
bgc = "azure2"
fgc = "black"

gui.tk_setPalette(background=bgc, foreground=m1c, activeBackground=fgc, activeForeground=bgc)

# Labels
L11 = Label(gui, text="PORT SCANNER", font=("Helvetica", 16, "underline"))
L11.place(x=16, y=10)

L21 = Label(gui, text="Target: ")
L21.place(x=16, y=90)

L22 = Entry(gui)
L22.place(x=180, y=90)

L23 = Label(gui, text="Ports: ")
L23.place(x=16, y=158)

L24 = Entry(gui)
L24.place(x=180, y=158, width=95)
L24.insert(0, "1")

L25 = Entry(gui)
L25.place(x=290, y=158, width=95)
L25.insert(0, "1024")

L26 = Label(gui, text="Results: ")
L26.place(x=16, y=220)
L27 = Label(gui, text="[ ... ]")
L27.place(x=180, y=220)

# Ports list
frame = Frame(gui)
frame.place(x=16, y=275, width=370, height=215)
listbox = Listbox(frame, width=59, height=6)
listbox.place(x=0, y=0)
listbox.bind("<<ListboxSelect>>")
scrollbar = Scrollbar(frame)
scrollbar.pack(side=RIGHT, fill=Y)
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

# Buttons / Scans
B11 = Button(gui, text="Start Scan", command=startScan)
B11.place(x=16, y=500, width=170)
B21 = Button(gui, text="Save Result", command=saveScan)
B21.place(x=210, y=500, width=170)
B22 = Button(gui, text="View Saved Result", command=viewSavedResult)
B22.place(x=16, y=540, width=170)

# Start GUI
gui.mainloop()
