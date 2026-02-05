"""Stub types for airavata.model.credential.store."""
from airavata.model._base import _ThriftEnum, _ThriftStub


class SummaryType(_ThriftEnum):
    SSH = 0
    PASSWD = 1
    CERT = 2

    _VALUES_TO_NAMES = {0: "SSH", 1: "PASSWD", 2: "CERT"}
    _NAMES_TO_VALUES = {v: k for k, v in _VALUES_TO_NAMES.items()}


class CredentialSummary(_ThriftStub):
    pass
