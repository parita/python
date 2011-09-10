import socket 
import sys 

host = 'localhost' 
port = 5000 
size = 1024 
client= socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
client.connect((host,port))
 	
print '%'

while 1:
	print client.getsockname()
    	# read from keyboard
    	data = raw_input("Data:")
	print 'Sent:',data,'%'
	data = client.recv(size)
    	
	if data == '': 
        	break 
    	client.send(data) 
    	data = client.recv(size)
    	print 'Received:',data
    	print '%' 
client.close()
