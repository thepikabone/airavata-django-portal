"""Stub types for airavata.model.experiment."""
from airavata.model._base import _ThriftEnum, _ThriftStub


class ExperimentSearchFields(_ThriftEnum):
    EXPERIMENT_NAME = 0
    EXPERIMENT_DESC = 1
    APPLICATION_ID = 2
    FROM_DATE = 3
    TO_DATE = 4
    STATUS = 5
    PROJECT_ID = 6
    JOB_ID = 7
    USER_NAME = 8

    _VALUES_TO_NAMES = {
        0: "EXPERIMENT_NAME", 1: "EXPERIMENT_DESC", 2: "APPLICATION_ID",
        3: "FROM_DATE", 4: "TO_DATE", 5: "STATUS",
        6: "PROJECT_ID", 7: "JOB_ID", 8: "USER_NAME",
    }
    _NAMES_TO_VALUES = {v: k for k, v in _VALUES_TO_NAMES.items()}


class ExperimentModel(_ThriftStub):
    pass


class ExperimentStatistics(_ThriftStub):
    pass


class ExperimentSummaryModel(_ThriftStub):
    pass
