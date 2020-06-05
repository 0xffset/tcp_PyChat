import socket
import sys
import select
from core.colors import red, good
from core.MongoDB import MongoDB


class Client:
    """ Client class
        This class handler the connections with the IRC server
        
        :param ip: ip address from the client 
        :param port: port connect client
        :type ip: str 
        :type port: int
        :return: None
     """
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.clients = {}
        self.sockets_list = []
        print(''' %s Host Name --> %s ''' % (good, socket.gethostname()))

    def get_connection_server(self):
        """ Make the connection with the socket"""
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.clients[self.ip] = self.port
        server_socket.connect((self.ip, self.port))
        sockets_list = [sys.stdin, server_socket]
        MongoDB().save_client(self.ip, self.port)
       
        while True:

            read_sockets, write_socket, error_socket = select.select(
                sockets_list, [], [])

            for socks in read_sockets:

                if socks == server_socket:

                    message = server_socket.recv(2048).decode('utf-8')
                    print('''%s %s''' % (good, message))
                else:

                    message = sys.stdin.readline()
                    server_socket.send(message.encode('utf-8'))
                    sys.stdout.write('''%s %s : ''' % (good, self.ip))
                    sys.stdout.write(message)
                    sys.stdout.flush()
