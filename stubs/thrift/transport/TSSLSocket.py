"""Stub for thrift.transport.TSSLSocket."""
from thrift.transport.TSocket import TSocket


class TSSLSocket(TSocket):
    def __init__(self, host="localhost", port=9090, validate=True,
                 ca_certs=None, keyfile=None, certfile=None, cert_reqs=None):
        super().__init__(host, port)
        self.validate = validate
        self.ca_certs = ca_certs
        self.cert_reqs = cert_reqs
