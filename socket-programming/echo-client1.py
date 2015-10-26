import socket

clisock = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
clisock.connect( ('', 8000) )
clisock.send("Hi I am the client\n")
print clisock.recv(100)
clisock.close()
