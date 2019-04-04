import socket			 
s = socket.socket()	
host = socket.gethostname()	 
port = 50002	

f=open('16_2.txt','r')		
msg=f.read()
#print msg
s.connect((host, port)) 
s.send(msg.encode())

print('Server: ',s.recv(1024).decode())
s.close()
