"""Stub types for airavata.model.group."""
from airavata.model._base import _ThriftEnum, _ThriftStub


class ResourcePermissionType(_ThriftEnum):
    WRITE = 0
    READ = 1
    MANAGE_SHARING = 2

    _VALUES_TO_NAMES = {0: "WRITE", 1: "READ", 2: "MANAGE_SHARING"}
    _NAMES_TO_VALUES = {v: k for k, v in _VALUES_TO_NAMES.items()}


class GroupModel(_ThriftStub):
    pass
