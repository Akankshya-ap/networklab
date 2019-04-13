

import argparse
import xmlrpc
# Comment out the above line and uncomment the below line for Python 2.x.
#import xmlrpclib
from base64 import b64decode

from xmlrpc.server import SimpleXMLRPCServer, SimpleXMLRPCRequestHandler
# Comment out the above line and uncomment the below line for Python 2.x.
#from SimpleXMLRPCServer  import SimpleXMLRPCServer, SimpleXMLRPCRequestHandler


class SecureXMLRPCServer(SimpleXMLRPCServer):

    def __init__(self, host, port, username, password, *args, **kargs):
        self.username = username
        self.password = password
        # authenticate method is called from inner class
        class VerifyingRequestHandler(SimpleXMLRPCRequestHandler):
              # method to override
              def parse_request(request):
                  if SimpleXMLRPCRequestHandler.parse_request(request):
                      # authenticate
                      if self.authenticate(request.headers):
                          return True
                      else:
                          # if authentication fails return 401
                          request.send_error(401, 'Authentication failed, Try agin.')
                  return False
        # initialize
        SimpleXMLRPCServer.__init__(self, (host, port), requestHandler=VerifyingRequestHandler, *args, **kargs)

    def authenticate(self, headers):
        headers = headers.get('Authorization').split()
        basic, encoded = headers[0], headers[1]
        if basic != 'Basic':
            print ('Only basic authentication supported')
            return False
        secret = b64decode(encoded).split(b':')
        
        username, password = secret[0].decode("utf-8"), secret[1].decode("utf-8")
        return True if (username == self.username and password == self.password) else False
    

def run_server(host, port, username, password):
    server = SecureXMLRPCServer(host, port, username, password)
    # simple test function
    def echo(msg):
        """Reply client in  uppser case """
        reply = msg.upper()
        print ("Client said: %s. So we echo that in uppercase: %s" %(msg, reply))
        return reply
    server.register_function(echo, 'echo')
    print ("Running a HTTP auth enabled XMLRPC server on %s:%s..." %(host, port))
    server.serve_forever()


if __name__ == '__main__':

    host, port =  'localhost', 5600
    username, password = 'user1', 'pass1'
    run_server(host, port, username, password)
