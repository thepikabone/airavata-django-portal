"""Stub for thrift.protocol.TMultiplexedProtocol."""


class TMultiplexedProtocol:
    def __init__(self, proto, serviceName):
        self.proto = proto
        self.serviceName = serviceName
