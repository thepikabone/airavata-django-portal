"""Stub types for airavata.model.workspace."""
from airavata.model._base import _ThriftEnum, _ThriftStub


class NotificationPriority(_ThriftEnum):
    LOW = 0
    NORMAL = 1
    HIGH = 2

    _VALUES_TO_NAMES = {0: "LOW", 1: "NORMAL", 2: "HIGH"}
    _NAMES_TO_VALUES = {v: k for k, v in _VALUES_TO_NAMES.items()}


class Notification(_ThriftStub):
    pass


class Project(_ThriftStub):
    pass
