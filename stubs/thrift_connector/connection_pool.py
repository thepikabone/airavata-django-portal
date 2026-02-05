"""Stub for thrift_connector.connection_pool.

Provides no-op ClientPool and ThriftClient so that the middleware
can assign request.airavata_client without crashing. Any method
called on the pool proxy returns None.

All method calls are logged at DEBUG level for observability.
"""
import logging

logger = logging.getLogger("airavata_stubs.connection_pool")


class ThriftClient:
    secure = False
    validate = False

    @classmethod
    def get_socket_factory(cls):
        return lambda host, port: None

    @classmethod
    def get_protoco_factory(cls):
        return lambda transport: None

    def ping(self):
        pass


class ClientPool:
    """No-op connection pool.  Any attribute access returns a callable that returns None.

    Logs every method call so you can see which Airavata API methods the portal
    is trying to invoke.
    """

    def __init__(self, *args, **kwargs):
        # Capture the service class name for logging context
        # e.g. Airavata, GroupManagerService, IamAdminServices, etc.
        if args and hasattr(args[0], '__name__'):
            self._pool_name = args[0].__name__
        else:
            self._pool_name = "unknown"
        logger.debug("[POOL:%s] ClientPool created (stub)", self._pool_name)

    def __getattr__(self, name):
        pool_name = self._pool_name

        def _noop(*args, **kwargs):
            logger.debug("[POOL:%s] %s(...) -> None (stub)", pool_name, name)
            return None
        return _noop
