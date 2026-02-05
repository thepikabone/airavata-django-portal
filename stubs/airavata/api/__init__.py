"""Stub for airavata.api - provides Airavata client class.

All method calls are logged at DEBUG level for observability.
"""
import logging

logger = logging.getLogger("airavata_stubs.api")


class _NoOpClient:
    """Client that returns None for any method call and logs it."""
    def __init__(self, *args, **kwargs):
        logger.debug("[API] Airavata.Client created (stub)")

    def __getattr__(self, name):
        def _noop(*args, **kwargs):
            logger.debug("[API] Airavata.Client.%s(...) -> None (stub)", name)
            return None
        return _noop


class Airavata:
    """Stub Airavata module with Client class."""
    Client = _NoOpClient
