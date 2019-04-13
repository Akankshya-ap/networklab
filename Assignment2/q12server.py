import socket
import fcntl
import struct

def get_interface_ip(ifname):
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	return socket.inet_ntoa(fcntl.ioctl(s.fileno(), 0x8915, struct.pack('256s',ifname[:15]))[20:24])
host = socket.gethostname()
port = 7200  

s = socket.socket()  # get instance
# look closely. The bind() function takes tuple as argument
s.bind((host, port))  # bind host address and port together

# configure how many client the server can listen simultaneously
s.listen(4)
print 'Starting server on', host, port
print 'The Web server URL for this would be http://%s:%d/' % (host, port)

track = dict()
while True:
    c, (client_host, client_port) = s.accept()
    data = c.recv(4096).decode()
    print("from connected user: " + str(data))
    #track[client_host] = track.get(client_host, 0) + 1
    c.recv(1000)
    c.send('HTTP/1.0 200 OK\n')
    c.send('Content-Type: text/html\n')
    c.send('\n')
    c.send("""
    <html>
    <body>
    <h1>Hi there</h1> this is from server!"""+host+" "+ get_interface_ip('eth0')+"  "+ str(data)+""" 
    </body>
    </html>
    """)
    c.close()
print 'Got connection from', client_host, client_port, track[client_host], 'times'
