import select
import socket
from time import time as now
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host='127.0.0.1'
port = 12345 
timeout=120
#s.connect(('127.0.0.1', port))          
s.settimeout(120.0)
print ("Waiting for ",host, port)
if(timeout):
    end_time=timeout+now()
c=1
while(c==1):
    try:
        if(timeout):
            next_timeout=end_time-now()
            if next_timeout<0:
                exit()
            else:
                print ("Next timeout" , round(next_timeout))
                s.settimeout(next_timeout)
        s.connect((host, port))
            
    except socket.timeout, err:
        if timeout:
            exit()
    except socket.error, err:
        c=1#print "Exception"
    else:
        c=0
        print "Server available"
        s.close()


