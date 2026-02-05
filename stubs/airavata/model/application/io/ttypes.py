"""Stub types for airavata.model.application.io."""
from airavata.model._base import _ThriftEnum, _ThriftStub


class DataType(_ThriftEnum):
    STRING = 0
    INTEGER = 1
    FLOAT = 2
    URI = 3
    URI_COLLECTION = 4
    STDOUT = 5
    STDERR = 6

    _VALUES_TO_NAMES = {
        0: "STRING",
        1: "INTEGER",
        2: "FLOAT",
        3: "URI",
        4: "URI_COLLECTION",
        5: "STDOUT",
        6: "STDERR",
    }
    _NAMES_TO_VALUES = {v: k for k, v in _VALUES_TO_NAMES.items()}


class InputDataObjectType(_ThriftStub):
    pass


class OutputDataObjectType(_ThriftStub):
    pass
