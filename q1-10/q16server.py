import socket
import thread

def on_new_client(clientsocket,addr):
    while True:
        print addr, ' >> '
        while True:
            msg = clientsocket.recv(1024)
            print msg
            if msg[-3:] == 'bye':
                break
            msg = raw_input('SERVER >> ')
            clientsocket.send(msg)
    clientsocket.close()

s = socket.socket()
host = socket.gethostname()
port = 50002

print 'Server started!'
print 'Waiting for clients...'

s.bind((host, port))
s.listen(5)

while True:
   c, addr = s.accept()
   print 'Got connection from', addr
   thread.start_new_thread(on_new_client,(c,addr))
s.close()
