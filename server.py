import socket
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(('0.0.0.0',9999))
server.listen(1)
print("waiting for the client")
conn,addr = server.accept()
print("connected with:",addr)
while(True):
    msg = conn.recv(1024).decode()
    print("client:",msg)
    reply = input("enter ur msg:")
    conn.send(reply.encode())