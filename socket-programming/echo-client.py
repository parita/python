import socket 
import sys 

host = 'localhost' 
port = 5000 
size = 1024 
client= socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
client.connect((host,port))
print client.getsockname()	
print '%'
data=''
while 1:
	# read from keyboard
    	if data:
                print 'Received:',data.'%'   
        else:
                data = raw_input("Data:")
                if data:
                        client.send(data)
                        print 'Sent:',data,'%'
                        data=''
                else:
                        data=client.recv(size)
                 
    	
client.close()
