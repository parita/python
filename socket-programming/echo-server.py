# TCP server example
import socket
import select

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("", 5000))
server_socket.listen(5)

print "TCPServer Waiting for client on port 5000"

data ='initialised...'
input_ = [server_socket]
output = [server_socket]

while 1:
        inputready,outputready,exceptready = select.select(input_,output,[])
        print len(inputready) , len(input_), len(outputready), len(output)

        for s in inputready:
                if s==server_socket:
                        client, address = server_socket.accept()
                        print "I got a connection from ", address
                        input_.append(client)
            
                else:
                        if data:
                            s.send(data)
                        data=s.recv(1024)
                        print "received:",data
                        if data:
                                print "out of inputready"
                                break;
                        else:
                                input_.remove(s)
        inputready,outputready,exceptready = select.select(input_,output,[])
        print len(inputready) , len(input_), len(outputready), len(output)
        for s in outputready:
                if s==server_socket:
                        client, address = server_socket.accept()
                        print "I got a connection from ", address
                        output.append()
                else:
                        if data:
                                s.send(data)
                                output.remove(s)
                        else:
                                s.close()
                inputready,outputready,exceptready = select.select(input_,output,[])
                print len(inputready) , len(input_), len(outputready), len(output)
        data=''
   
    
