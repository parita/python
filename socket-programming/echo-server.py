# TCP server example
import socket
import select

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("", 5000))
server_socket.listen(5)

print "TCPServer Waiting for client on port 5000"


data ='init'
input_ = [server_socket]
output = [server_socket]
inputready,outputready,exceptready = select.select(input_,output,[])
while 1: 

	print len(inputready) , len(input_), len(outputready), len(output)
    	for s in inputready:

		print s.getsockname()
        	if s==server_socket:
            		client, address = server_socket.accept()
            		print "I got a connection from ", address
            		input_.append(client)
        	else:
			data = s.recv(1024) 
            		if data:
                		s.send(data)
                		print 'received:',data
            		else:
                		s.close() 
                		input_.remove(s)
				print "Mistake idhar hai kya ?"
    	inputready,outputready,exceptready = select.select(input_,output,[])
