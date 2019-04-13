import os
import socket
import fcntl
import struct

def get_interface_ip(ifname):
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	return socket.inet_ntoa(fcntl.ioctl(s.fileno(), 0x8915, struct.pack('256s',ifname[:15]))[20:24])


def get_host_name():
    host_name = socket.gethostname()
    return host_name

print "Host IP Address is ",get_interface_ip('eth0')
print "Host name is ",get_host_name()
#print (1)
