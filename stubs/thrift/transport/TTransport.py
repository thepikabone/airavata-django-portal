"""Stub for thrift.transport.TTransport."""
from thrift.Thrift import TException


class TTransportException(TException):
    UNKNOWN = 0
    NOT_OPEN = 1
    ALREADY_OPEN = 2
    TIMED_OUT = 3
    END_OF_FILE = 4

    def __init__(self, type=UNKNOWN, message=None):
        super().__init__(message)
        self.type = type
        self.message = message


class TTransportBase:
    def isOpen(self):
        return False

    def open(self):
        pass

    def close(self):
        pass

    def read(self, sz):
        return b""

    def readAll(self, sz):
        return b""

    def write(self, buf):
        pass

    def flush(self):
        pass


class TBufferedTransport(TTransportBase):
    def __init__(self, trans):
        self._trans = trans

    def isOpen(self):
        return False

    def open(self):
        pass

    def close(self):
        pass
