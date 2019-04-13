import socket 

ip = socket.gethostbyname('www.google.com')
print "Remote server ip for google.com",ip


from binascii import hexlify
def convert_ip4_address():
	for ip_addr in ['127.0.0.1', ip]:
		packed_ip_addr = socket.inet_aton(ip_addr)
		unpacked_ip_addr = socket.inet_ntoa(packed_ip_addr)
		print "IP Address: %s => Packed: %s, Unpacked: %s"\
	%(ip_addr, hexlify(packed_ip_addr), unpacked_ip_addr)


convert_ip4_address()
