import socket


"""
Decorator example. This scripts starts a simple socket client that connects to
a simple socket server which sends a user response back to the client. The
prints the response from the server and exits.
"""


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 2401))
print('Received: {0}'.format(client.recv(1024)))
client.close()
