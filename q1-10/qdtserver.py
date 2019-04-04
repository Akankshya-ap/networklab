import socket
import datetime

def server_program():

    host = socket.gethostname()
    port = 5100  

    server_socket = socket.socket()  
    
    server_socket.bind((host, port))  
    server_socket.listen(4)
    #conn, address = server_socket.accept()  # accept new connection
    #print("Connection from: " + str(address))
    while True:
        conn, address = server_socket.accept()
        print("Connection from: " + str(address))
        data = conn.recv(4096).decode()
        #if not data:
        #    break
        print("from connected user: " + str(data))
        
        data = str(datetime.datetime.now())
        conn.send(data.encode())  # send data to the client

    conn.close() 
if __name__ == '__main__':
    server_program()
