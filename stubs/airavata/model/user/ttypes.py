"""Stub types for airavata.model.user."""
from airavata.model._base import _ThriftEnum, _ThriftStub


class Status(_ThriftEnum):
    ACTIVE = 0
    CONFIRMED = 1
    APPROVED = 2
    DELETED = 3
    DUPLICATE = 4
    GRACE_PERIOD = 5
    INVITED = 6
    DENIED = 7
    PENDING = 8
    PENDING_CONFIRMATION = 9
    PENDING_APPROVAL = 10
    REJECTED = 11

    _VALUES_TO_NAMES = {
        0: "ACTIVE", 1: "CONFIRMED", 2: "APPROVED", 3: "DELETED",
        4: "DUPLICATE", 5: "GRACE_PERIOD", 6: "INVITED", 7: "DENIED",
        8: "PENDING", 9: "PENDING_CONFIRMATION", 10: "PENDING_APPROVAL",
        11: "REJECTED",
    }
    _NAMES_TO_VALUES = {v: k for k, v in _VALUES_TO_NAMES.items()}


class UserProfile(_ThriftStub):
    pass
