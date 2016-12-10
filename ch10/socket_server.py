import socket
from socket_decorator import LogSocket
from socket_decorator import GzipSocket

"""
This is a decorator example. The script creates an interactive shell that waits
for a connection from a client and then prompts the user for a string response.
This particular script uses the raw (undecorated) Python socket object. It is
used as an example of the socket interface, which will be decorated in another
script.
"""


def respond(client):
    """
    Prompts the user to input a response and sends the data as a reply to the
    socket parameter.
    :param client: socket connected to the client to send the response to.
    :return: None
    """
    response = input("Enter a value: ")
    client.send(bytes(response, 'utf8'))
    client.close()


# Construct a server socket and listen on localhost:2401
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 2401))
server.listen()
try:
    while True:
        client, addr = server.accept()
        # respond(client)
        #respond(LogSocket(client))
        respond(GzipSocket(client))
finally:
    server.close()
