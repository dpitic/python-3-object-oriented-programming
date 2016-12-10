import gzip
from io import BytesIO


"""
This is an example of a decorator. It is a logging decorator which decorates
the socket object. This class outputs any data being sent to the server's
console before it sends it to the client.
"""


class LogSocket:
    """
    Socket decorator used to log the data being sent to the server's console
    before sending it to the client. It implements the identical send() and
    close() interfaces that the socket objects have.
    """
    def __init__(self, socket):
        self.socket = socket

    def send(self, data):
        """
        Send data to the socket and log the output to console.
        :param data: to send to the socket.
        :return: None
        """
        print('Sending {0} to {1}'.format(data, self.socket.getpeername()[0]))
        self.socket.send(data)

    def close(self):
        self.socket.close()


class GzipSocket:
    """
    Socket decorator that compresses data using gzip compression before sending
    the data.
    """
    def __init__(self, socket):
        self.socket = socket

    def send(self, data):
        """
        Compress the data using gzip compression and send the data.
        :param data: data to be sent by the socket.
        :return: None
        """
        buf = BytesIO()
        zipfile = gzip.GzipFile(fileobj=buf, mode="w")
        zipfile.write(data)
        zipfile.close()
        self.socket.send(buf.getvalue())

    def close(self):
        self.socket.close()
