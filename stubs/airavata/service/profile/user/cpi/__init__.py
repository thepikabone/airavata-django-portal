"""Stub for airavata.service.profile.user.cpi.

All method calls are logged at DEBUG level for observability.
"""
import logging

logger = logging.getLogger("airavata_stubs.service")


class _NoOpClient:
    def __init__(self, *args, **kwargs):
        pass

    def __getattr__(self, name):
        def _noop(*args, **kwargs):
            logger.debug("[SERVICE:UserProfileService] %s(...) -> None (stub)", name)
            return None
        return _noop


class UserProfileService:
    Client = _NoOpClient
