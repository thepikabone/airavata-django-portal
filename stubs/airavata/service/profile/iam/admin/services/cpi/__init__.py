"""Stub for airavata.service.profile.iam.admin.services.cpi.

All method calls are logged at DEBUG level for observability.
"""
import logging

logger = logging.getLogger("airavata_stubs.service")


class _NoOpClient:
    def __init__(self, *args, **kwargs):
        pass

    def __getattr__(self, name):
        def _noop(*args, **kwargs):
            logger.debug("[SERVICE:IamAdminServices] %s(...) -> None (stub)", name)
            return None
        return _noop


class IamAdminServices:
    Client = _NoOpClient
