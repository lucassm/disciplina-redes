"""TCP client with random messages in parallel."""
import socket
import time
import lorem
from threading import Thread

server_name = 'localhost'
server_port = 12000

messages = list()

messages = [lorem.sentence() for i in range(10)]


def myfunc(messages):
    """myfunc."""
    for message in messages:
        client_socket = socket.socket(socket.AF_INET,
                                      socket.SOCK_STREAM)
        client_socket.connect((server_name, server_port))
        client_socket.send(message.encode())
        modified_sentence = client_socket.recv(1024)
        print('From Server: {}'.format(modified_sentence.decode()))
        client_socket.close()
        #time.sleep(0.1)

for i in range(200):
    t = Thread(target=myfunc, args=(messages,))
    t.start()
