#!/usr/bin/python3

#-*- coding:UTF-8 -*-

import socket, time, subprocess

def parser(stringclient):
    if inputmessage=="adminpassword":
        ver="True"
    else:
        ver="False"
    return ver

host="127.0.0.1"
port=12555
subprocess.Popen("fuser -k "+str(port)+"/tcp", shell=True)
print("Porta di servizio libera")
time.sleep(3)
print("Server avviato")

s=socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))
s.listen(5)

while(True):
    c, addr=s.accept()
    print("Connessione stabilita con "+str(addr))
    inputmessage=c.recv(1024).decode()
    print("Messaggio dal client: "+inputmessage)
    outputmessage=parser(inputmessage)
    c.send(outputmessage.encode())
    print("Messaggio dal server: "+outputmessage)
    c.close()
    print("Connessione interrotta con "+str(addr))
