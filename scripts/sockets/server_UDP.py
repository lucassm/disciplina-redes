"""simple UDP sever."""

import socket
import signal
import sys

def signal_handler(signal, frame):
    global server_socket
    print('\nClosing socket...')
    server_socket.close()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

server_port = 12000
server_socket = socket.socket(socket.AF_INET,
                              socket.SOCK_DGRAM)
server_socket.setsockopt(socket.SOL_SOCKET,
                         socket.SO_REUSEADDR,
                         1)
server_socket.bind(('', server_port))
print('The server is ready to receive')

while True:
    message, client_address = server_socket.recvfrom(2048)
    print('Message received: {}'.format(message.decode()))
    modified_message = message.upper()
    server_socket.sendto(modified_message, client_address)
