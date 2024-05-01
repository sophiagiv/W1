from tkinter import *
from tkinter import messagebox
import requests

def login():
    StudentID = entry_StudentID.get()
    Password = entry_Password.get()
    response = requests.post('http://127.0.0.1:5050/login', data={'StudentID': StudentID, 'Password': Password})
    if response.status_code == 200:
        messagebox.showinfo("Login Success", response.json()['message'])
        show_gpa(StudentID)
    else:
        messagebox.showerror("Login Failed", response.json()['message'])

def signup():
    StudentID = entry_StudentID.get()
    Password = entry_Password.get()
    response = requests.post('http://127.0.0.1:5050/signup', data={
        'StudentID': StudentID,  'Password': Password, 
    })
    if response.status_code == 201:
        messagebox.showinfo("Signup Success", response.json()['message'])
    else:
        messagebox.showerror("Signup Failed", response.json()['message'])

def show_gpa(StudentID):
    response = requests.get(f'http://127.0.0.1:5050/gpa', params={'StudentID': StudentID})
    if response.status_code == 200:
        topwindow = Toplevel(root)
        topwindow.title("GPA Data")
        Label(topwindow, text=f"Your GPA: {response.json()['GPA']}", font=('Helvetica', 18)).pack(pady=20)
    else:
        messagebox.showerror("Error", response.json()['message'])

root = Tk()
root.title("Login System")
root.geometry("1000x600")

frame = Frame(root)
frame.pack(pady=20)

Label(frame, text="Student ID", font=('Helvetica', 16)).grid(row=0, column=0, padx=10, pady=10)
entry_StudentID = Entry(frame, font=('Helvetica', 16))
entry_StudentID.grid(row=0, column=1, padx=10, pady=10)

Label(frame, text="Password", font=('Helvetica', 16)).grid(row=2, column=0, padx=10, pady=10)
entry_Password = Entry(frame, show='*', font=('Helvetica', 16))
entry_Password.grid(row=2, column=1, padx=10, pady=10)

login_btn = Button(frame, text="Login", command=login, font=('Helvetica', 16))
login_btn.grid(row=4, column=0, padx=10, pady=10)

signup_btn = Button(frame, text="Signup", command=signup, font=('Helvetica', 16))
signup_btn.grid(row=4, column=1, padx=10, pady=10)

root.mainloop()
