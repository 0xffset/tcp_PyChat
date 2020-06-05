#!/usr/bin/env python3

__author__ = "Rogger Garcia Diaz (rolEYder)"
__copyright__ = "Copyright 2020, tcp_Pychat"
__license__ = "MIT"
__version__ = "1.0.1"
__maintainer__ = "rolEYder"
__email__ = "roleyder02@gmail.com"
__status__ = "Production"


import os
from core.client import Client
import sys
import argparse
from core.colors import red, white, end, info, error, green
import json

with open('config.json', 'r') as f:
    config = json.load(f)


print('''%s
\t 
 
  _              _____        _____ _           _   
 | |            |  __ \      / ____| |         | |  
 | |_ ___ _ __  | |__) |   _| |    | |__   __ _| |_ 
 | __/ __| '_ \ |  ___/ | | | |    | '_ \ / _` | __|
 | || (__| |_) || |   | |_| | |____| | | | (_| | |_ 
  \__\___| .__/ |_|    \__, |\_____|_| |_|\__,_|\__|
         | |______      __/ |                       
         |_|______|    |___/  

 %s%s
%s''' % (red, green, config['version'], end))


parser = argparse.ArgumentParser()
parser.add_argument('-ip', '--ip_address',
                    help='IP address to set the client connection', dest='ip')
parser.add_argument(
    '-p', '--port', help='Port to set the client connection', dest='port')
args = parser.parse_args()

ip_address = args.ip
port = args.port


if ip_address and port:

    try:
        client = Client(str(ip_address), int(port))
        client.get_connection_server()

    except Exception as identifier:
        print(''' %s %s''' % (error, identifier))
else:
    print(''' %s Error: Set ip address server and a port   ''' % (error))
    exit
