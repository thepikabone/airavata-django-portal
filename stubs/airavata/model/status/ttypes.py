"""Stub types for airavata.model.status."""
from airavata.model._base import _ThriftEnum, _ThriftStub


class ExperimentState(_ThriftEnum):
    CREATED = 0
    VALIDATED = 1
    SCHEDULED = 2
    LAUNCHED = 3
    EXECUTING = 4
    CANCELING = 5
    CANCELED = 6
    COMPLETED = 7
    FAILED = 8

    _VALUES_TO_NAMES = {
        0: "CREATED", 1: "VALIDATED", 2: "SCHEDULED", 3: "LAUNCHED",
        4: "EXECUTING", 5: "CANCELING", 6: "CANCELED",
        7: "COMPLETED", 8: "FAILED",
    }
    _NAMES_TO_VALUES = {v: k for k, v in _VALUES_TO_NAMES.items()}


class ExperimentStatus(_ThriftStub):
    pass


class ProcessStatus(_ThriftStub):
    pass
