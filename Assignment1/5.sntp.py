import ntplib
import socket
import struct
import sys
import time
from time import ctime
def print_time():
	ntp_client = ntplib.NTPClient()
	response = ntp_client.request('pool.ntp.org')
	print "Internet time",ctime(response.tx_time)


def sntp_client():
	NTP_SERVER = "asia.pool.ntp.org"
	TIME1970 = 2208988800L
	client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	data = '\x1b' + 47 * '\0'

	client.sendto(data, (NTP_SERVER, 123))
	data, address = client.recvfrom( 1024 )
	if data:
		print 'Response received from:', address
	t = struct.unpack( '!12I', data )[10]
	t -= TIME1970
	print '\tSNTP client Time=%s' % time.ctime(t)

sntp_client()
print_time()


