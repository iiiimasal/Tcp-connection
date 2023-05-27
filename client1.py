import socket

HOST="127.0.0.1"
PORT=8020

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as c:
 c.connect((HOST,PORT))
 print("connected to server")
 while(1):
  sentence=input()
  if sentence=="exit":
    break
  c.sendall(sentence.encode())
  modifiedsentence=c.recv(1024)
  print("recieved:",modifiedsentence.decode())

c.close()
print("connection has been closed")
