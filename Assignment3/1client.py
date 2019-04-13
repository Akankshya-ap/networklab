import socket	
import getpass		 
s = socket.socket()	
host = socket.gethostname()	 
port = 5000	

msg = getpass.getpass('Password:')	

s.connect((host, port)) 
s.send(msg.encode())

print 'Access to Server: ',str(s.recv(1024).decode())
s.close()
