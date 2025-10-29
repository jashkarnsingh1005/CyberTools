import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.ttk import *
from tkinter import *
from PIL import Image,ImageTk
import time 
from tkinter import messagebox

root=Tk()
root.geometry("500x400+100+100")
root.title("KEYLOGGER")
icon_image = Image.open("C:\\Users\\jashk\\OneDrive\\Desktop\\PBL project\\pic\\icon.ico")
icon = ImageTk.PhotoImage(icon_image)
root.iconphoto(True, icon)
bg=Image.open("C:\\Users\\jashk\\OneDrive\\Desktop\\PBL project\\pic\\quiz game.jpg")
bg=bg.resize((500,500))
bg=ImageTk.PhotoImage(bg)
canvas1=Canvas(height=600,width=600)
canvas1.create_image(0,0,anchor=NW,image=bg)
canvas1.pack()
bar=Progressbar(canvas1,orient=HORIZONTAL,length=200)
bar.place(x=150,y=300)
bar['value']=0
while bar['value']<100:
   bar['value']+=1
   root.update()
   time.sleep(0.01)
root.destroy()
shift=11
c=1


class QuizGame(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Quiz Game")
        self.geometry("600x400")
        self.configure(bg='DodgerBlue2')

        self.current_question = 0
        self.user_score = 0

        self.questions = [
            {
                "question": "What is the primary purpose of a firewall in network\nsecurity?",
                "options": ['To prevent malware infections', 'To filter and control network traffic',
                            'To encrypt all data on the network', 'To detect network vulnerabilities'],
                "correct_option": 1
            },
            {
                "question": "What is the main goal of penetration testing in\ncybersecurity?",
                "options": ["To develop new security software", "To perform system backups",
                            "To secure network traffic with encryption", "To identify and exploit vulnerabilities"],
                "correct_option": 3
            },
            {
                "question": "Which of the following is not a type of malware?",
                "options": ["Spyware", "Ransomware", "Firewire", "Firewall"],
                "correct_option": 2
            },
            {
                "question": "What does 'HTTPS' stand for in the context of web\nsecurity?",
                "options": ["HyperText Transfer Protocol Secure", "Hyperlink Text System",
                            "High-Tech Security Protocol", " Hypertext Transfer Page Service"],
                "correct_option": 0

            },
            {
                "question": "What is the purpose of a 'honeypot' in cybersecurity?",
                "options": ["A system used to attract bees", "A type of malware", "An encryption key",
                            "A fake network designed to trap attackers"],
                "correct_option": 3
            },
            {
                "question": "What is the primary purpose of a port scanner in\ncybersecurity?",
                "options": ["To encrypt data transmissions", "To identify open ports on a target system",
                            "To launch DDoS attacks", "To launch DDoS attacks"],
                "correct_option": 1
            },
            {
                "question": "Which encryption algorithm is commonly used to secure\n internet communications, such as web browsing?",
                "options": ["AES (Advanced Encryption Standard)", "DES (Data Encryption Standard)",
                            "RSA (Rivest–Shamir–Adleman)", "MD5 (Message Digest Algorithm 5)"],
                "correct_option": 0
            },
            {
                "question": "Which of the following is an example of a strong\npassword?",
                "options": ["P@ssw0rd!", "Password123", "123456", "qwerty"],
                "correct_option": 0
            },
            {
                "question": "Which type of keylogger can be detected by most\nantivirus software?",
                "options": ["Hardware Keylogger", "Remote Keylogger", "Rootkit Keylogger", " Software Keylogger"],
                "correct_option": 3
            },
            {
                "question": "Which term refers to the act of gaining unauthorized\naccess to a computer or network system?",
                "options": ["Penetration Testing", "Firewall", "Hacking", "Cryptography"],
                "correct_option": 2
            },
        ]

        self.create_widgets()

    def create_widgets(self):
        self.label_question = ttk.Label(self, text="", font=("Arial", 16), background='DodgerBlue2')
        self.label_question.pack(pady=20)

        self.buttons = []

        for i in range(4):
            option_button = ttk.Button(self, text="", command=lambda idx=i: self.select_option(idx))
            option_button.pack(pady=5)
            self.buttons.append(option_button)

        next_button = ttk.Button(self, text="Next Question", command=self.next_question)
        next_button.pack(pady=10)

        self.load_question()

    def load_question(self):
        if self.current_question < len(self.questions):
            question_data = self.questions[self.current_question]
            self.label_question.config(text=question_data["question"])

            for i in range(4):
                self.buttons[i].config(text=question_data["options"][i], state='normal')

        else:
            self.show_score()

    def select_option(self, option_index):
        self.var_selected_option = option_index
        for button in self.buttons:
            button.config(state='normal')
        self.buttons[option_index].config(state='disabled')

    def next_question(self):
        if hasattr(self, 'var_selected_option'):
            correct_option = self.questions[self.current_question]["correct_option"]
            if self.var_selected_option == correct_option:
                self.user_score += 1

        self.current_question += 1
        self.load_question()

    def show_score(self):
        messagebox.showinfo("Quiz Result", f"You scored {self.user_score} out of {len(self.questions)}!")
        self.destroy()

if __name__ == "__main__":
    app = QuizGame()
    app.mainloop()
