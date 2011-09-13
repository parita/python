# TCP server example
import socket           
import select           
 
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("", 8000))                                          
server_socket.listen(5)                                                 
 
print "TCPServer Waiting for client on port 8000"                       
 
data ='init'           
input_ = [server_socket]
output = []
name={}

inputready,outputready,exceptready = select.select(input_,output,[])    
print len(inputready),len(outputready),len(input_),len(output)
while 1:            
        for s in inputready:                   
                if s==server_socket:            
                        client, address = server_socket.accept()        
                        print "I got a connection from ", address
                        name[client]=client.recv(1024)
                        print 'name:',name[client]
                        input_.append(client)                           
                        output.append(client)                           
                else:
                        k=s.recv(1024)
                        if k:
                                data=data+'\n'+name[s]+':'+k
                                print data
                    
        inputready,outputready,exceptready = select.select(input_,output,[])

        for s in outputready:
                s.send(data)
        data=''

