import socket 
import sys 

host = 'localhost' 
port = 8000 
size = 1024 
client= socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
client.connect((host,port))
print client.getsockname()	
print '%'
data=''
while 1:
        # read from keyboard
        data=raw_input("Data:")
        if data:
                client.send(data)
                print 'Sent:',data,'%'
                data=''
        
                data=client.recv(size)
                if data:
                        print 'Received:',data,'%'
client.close()
