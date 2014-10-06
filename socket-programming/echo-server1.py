import socket
	srvsock = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
	srvsock.bind( ('', 8000) )
	srvsock.listen( 5 )

while 1:
	clisock, (remhost, remport) = srvsock.accept()
	str = clisock.recv(100)
	clisock.send( str )
	clisock.close()
