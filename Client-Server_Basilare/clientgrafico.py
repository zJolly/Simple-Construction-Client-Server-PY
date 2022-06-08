#!/usr/bin/python3

#-*- coding:UTF-8 -*-

from tkinter import *
from tkinter import messagebox
import socket

def loginfunction():
    data=""+user.get()+passw.get()
    print(data)
    s.send(data.encode())
    reply=s.recv(1024).decode()
    if reply=="True":
        logged()
    else:
        notlogged()

def logged():
    messagebox.showinfo("Logged")

def notlogged():
    messagebox.showinfo("Error")
    command=window.destroy

def destruction():
    command=window.destroy
    s.close()

window=Tk()
window.geometry("600x100")
window.title("Loginbox")

user=StringVar()
passw=StringVar()

s=socket.socket()
host="127.0.0.1"
port=12555

s.connect((host, port))

face=Frame(window)
face.pack()

usernamebox=Label(face, text="Username:")
usernamebox.grid(row=0, column=0)
usernameinputbox=Entry(face, width="20", bg="cyan", textvariable=user)
usernameinputbox.grid(row=0, column=1)

passwordbox=Label(face, text="Password:")
passwordbox.grid(row=1, column=0)
passwordinputbox=Entry(face, width="20", bg="cyan", textvariable=passw)
passwordinputbox.grid(row=1, column=1)

login=Button(face, text="Login", command=loginfunction)
login.grid(row=3, column=0)
cancel=Button(face, text="Cancel", command=destruction)
cancel.grid(row=3, column=2)

window.mainloop()
