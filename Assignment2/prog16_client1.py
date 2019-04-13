import socket			 
s = socket.socket()	
host = socket.gethostname()	 
port = 50000				

s.connect((host, port)) 

msg = 'hello from client1\n' * 200 + 'bye' * 350
s.send(msg.encode())
print('Sever: ',s.recv(1024).decode())

s.close()
