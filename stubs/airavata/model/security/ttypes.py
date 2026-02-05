"""Stub types for airavata.model.security."""
from airavata.model._base import _ThriftStub


class AuthzToken(_ThriftStub):
    def __init__(self, accessToken=None, claimsMap=None, **kwargs):
        self.accessToken = accessToken
        self.claimsMap = claimsMap
        super().__init__(**kwargs)
