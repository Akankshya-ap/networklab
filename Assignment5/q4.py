

import argparse
import xmlrpc
# Comment out the above line and uncomment the below line for Python 2.x.
#import xmlrpclib
import threading

from xmlrpc.server import SimpleXMLRPCServer
# Comment out the above line and uncomment the below line for Python 2.x.
#from SimpleXMLRPCServer import SimpleXMLRPCServer

# some trivial functions
def add(x,y):
    return x+y

def subtract(x, y):
    return x-y

def multiply(x, y):
    return x*y

def divide(x, y):
    return x/y


class ServerThread(threading.Thread):
    def __init__(self, server_addr):
        threading.Thread.__init__(self)
        self.server = SimpleXMLRPCServer(server_addr)
        self.server.register_multicall_functions()
        self.server.register_function(add, 'add')
        self.server.register_function(subtract, 'subtract')
        self.server.register_function(multiply, 'multiply')
        self.server.register_function(divide, 'divide')

    def run(self):
        self.server.serve_forever()
        
def run_server(host, port):
    # server code
    server_addr = (host, port)
    server = ServerThread(server_addr)
    server.start() # The server is now running
    print ("Server thread started. Testing the server...")

def run_client(host, port):

    # client code
    proxy = xmlrpc.client.ServerProxy("http://%s:%s/" %(host, port))
    # Comment out the above line and uncomment the below line for Python 2.x.
    #proxy = xmlrpclib.ServerProxy("http://%s:%s/" %(host, port))

    multicall = xmlrpc.client.MultiCall(proxy)
    # Comment out the above line and uncomment the below line for Python 2.x.
    #multicall = xmlrpclib.MultiCall(proxy)

    multicall.add(41,65)
    multicall.subtract(41,65)
    multicall.multiply(41,65)
    multicall.divide(41,65)
    result = multicall()
    print ("41+65=%d, 41-65=%d, 41*65=%d, 41/65=%d" % tuple(result))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Multithreaded multicall XMLRPC Server/Proxy')
    parser.add_argument('--host', action="store", dest="host", default='localhost')
    parser.add_argument('--port', action="store", dest="port", default=8000, type=int)
    # parse arguments
    given_args = parser.parse_args()
    host, port =  given_args.host, 5000
    run_server(host, port)
    run_client(host, port)

