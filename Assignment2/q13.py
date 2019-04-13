
BUFSIZE = 4096
import asyncore
import socket
class PortForwarder(asyncore.dispatcher):
        def __init__(self, ip, port, remoteip,remoteport,backlog=5):
                asyncore.dispatcher.__init__(self)
                self.remoteip=remoteip
                self.remoteport=remoteport
                self.create_socket(socket.AF_INET,socket.SOCK_STREAM)
                self.set_reuse_addr()
                self.bind((ip,port))
                self.listen(backlog)
        def handle_accept(self):
                conn, addr = self.accept()
                print "Connected to:",addr
                Sender(Receiver(conn),self.remoteip,self.remoteport)
class Receiver(asyncore.dispatcher):
        def __init__(self,conn):
                asyncore.dispatcher.__init__(self,conn)
                self.from_remote_buffer=''
                self.to_remote_buffer=''
                self.sender=None
        def handle_connect(self):
                pass
        def handle_read(self):
                read = self.recv(BUFSIZE)
                self.from_remote_buffer += read
        def writable(self):
                return (len(self.to_remote_buffer) > 0)
        def handle_write(self):
                sent = self.send(self.to_remote_buffer)
                self.to_remote_buffer = self.to_remote_buffer[sent:]
        def handle_close(self):
                self.close()
                if self.sender:
                        self.sender.close()
class Sender(asyncore.dispatcher):
        def __init__(self, receiver, remoteaddr,remoteport):
                asyncore.dispatcher.__init__(self)
                self.receiver=receiver
                receiver.sender=self
                self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
                self.connect((remoteaddr, remoteport))
        def handle_connect(self):
                pass
        def handle_read(self):
                read = self.recv(BUFSIZE)
                self.receiver.to_remote_buffer += read
        def writable(self):
                return (len(self.receiver.from_remote_buffer) > 0)
        def handle_write(self):
                sent = self.send(self.receiver.from_remote_buffer)
                self.receiver.from_remote_buffer = self.receiver.from_remote_
                buffer[sent:]
        def handle_close(self):
                self.close()
                self.receiver.close()

if __name__ == "__main__":
        local_host = 'localhost'
        remote_host = 'www.google.com'
        local_port=8800
        remote_port=80

        print "Starting port forwarding local %s:%s => remote %s:%s" %(local_host, local_port, remote_host, remote_port)


        PortForwarder(local_host, local_port, remote_host, remote_port)
        asyncore.loop()
