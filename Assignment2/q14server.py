import socket               
s = socket.socket()         
port = 12345                
s.bind(('127.0.0.1', port))        
while True:
   c, addr = s.accept()     
   print 'Got connection from', addr

   
