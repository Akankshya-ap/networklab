
import argparse
import xmlrpc
# Comment out the above line and uncomment the below line for Python 2.x.
#import xmlrpclib

from xmlrpc.server import SimpleXMLRPCServer
# Comment out the above line for Python 2.x.

def run_client(host, port, username, password):
    server = xmlrpc.client.ServerProxy('http://%s:%s@%s:%s' %(username, password, host, port, ))
    # Comment out the above line and uncomment the below line for Python 2.x.
    #server = xmlrpclib.ServerProxy('http://%s:%s@%s:%s' %(username, password, host, port, ))
    msg = "hello server..."
    print ("Sending message to server: %s  " %msg)
    print ("Got reply: %s" %server.echo(msg))

if __name__ == '__main__':
   
    host, port =  'localhost', 5600
    username, password = 'user1', 'pass1'
    run_client(host, port, username, password)
