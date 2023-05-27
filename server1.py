import socket
import threading
import socket
import threading
HOST="127.0.0.1"
PORT=8020


   
with socket.socket(socket.AF_INET,socket.SOCK_STREAM ) as c:
    c.bind(HOST,PORT)
    c.listen()
    print("connected on port ", PORT)

while(1):
    connectionSocket , addr=c.accept()
    sentence=connectionSocket.recv(1024).decode()
    capitilizedSentence=sentence.upper()
    connectionSocket.send(capitilizedSentence.encode())
    connectionSocket.close() 
