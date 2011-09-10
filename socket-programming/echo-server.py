# TCP server example
import socket           
import select           
 
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("", 8000))                                          
server_socket.listen(5)                                                 
 
print "TCPServer Waiting for client on port 5000"                       
 
data =''               
input_ = [server_socket]
output = []       

 
while 1:
        inputready,outputready,exceptready = select.select(input_,output,[])    
        print len(inputready) , len(input_), len(outputready), len(output) 
            
        for s in inputready:                   
                if s==server_socket:            
                        client, address = server_socket.accept()        
                        print "I got a connection from ", address       
                        input_.append(client)                           
                        output.append(client)                           
                else:                                                   
                        data=s.recv(1024)    
                        if data:                                        
                                print "received:",data
                                break;
                        else:
                                input_.remove(s)
                
        inputready,outputready,exceptready = select.select(input_,output,[])    
        print len(inputready) , len(input_), len(outputready), len(output) 
        for s in outputready:                                           
                if data:                                                
                        s.send(data)                                    
                        output.remove(s)                               
                                                  
