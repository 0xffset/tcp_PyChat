import socket
import os
import threading
import json
from core.colors import good
from core.MongoDB import MongoDB



class Server:
    """  Server class
         This class make the client-server connections and their broadcasting
         with the connected clients
         :param ip: ip address client
         :param port: port client
         :type ip: str
         :type port: int
    """
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.list_clients = []
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(
            socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((self.ip, self.port))
        self.server_socket.listen(100)
       
        print('''%s Waiting for connections... ''' % (good))
        
    def is_running_port_open(self):
        """Check if already exists a connection in one port."""
        location = (self.ip, self.port)
        result = self.server_socket.connect_ex(location)
        if result == 0:
            return True
        else:
            return False

    def thread_connections(self, conn, address):
        """Build differents threads for each client connection
            :param conn: connection client
            :param address: address client
            :type conn: Object
            :type address: str
        """
        msg = "Welcome to tcp_PyChat"
        conn.send(msg.encode('utf-8'))
        while True:

            try:
                message = conn.recv(2048).decode('utf-8')
                
                if message:
                    
                    print(''' %s %s-%s''' % (good, self.ip, message))
                    

            except Exception as e:
                print(e)

   
    def server_connection(self):
        """ set connection's client """
        while True:
            conn, address = self.server_socket.accept()
            self.list_clients.append(conn)
           
            print(''' %s %s connected''' % (good, self.ip))
            threading._start_new_thread(
                self.thread_connections, (conn, address))
        conn.close()
        self.server_socket.close()

    
