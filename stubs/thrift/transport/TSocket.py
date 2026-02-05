"""Stub for thrift.transport.TSocket."""
from thrift.transport.TTransport import TTransportBase


class TSocket(TTransportBase):
    def __init__(self, host="localhost", port=9090, unix_socket=None):
        self.host = host
        self.port = port
        self.unix_socket = unix_socket
