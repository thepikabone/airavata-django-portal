"""Proxy stub for airavata_django_portal_sdk.experiment_util.

Tries to delegate to the real SDK if installed; otherwise returns defaults.
"""
import logging
from _proxy import load_real_module, call_real

logger = logging.getLogger(__name__)

_real = load_real_module(
    'airavata_django_portal_sdk.experiment_util',
    'airavata_django_portal_sdk'
)


def launch(*args, **kwargs):
    return call_real(_real, 'launch', None, *args, **kwargs)


def clone(*args, **kwargs):
    return call_real(_real, 'clone', None, *args, **kwargs)


class _IntermediateOutputProxy:
    """Proxy for experiment_util.intermediate_output sub-module."""

    def __init__(self):
        self._real_io = None
        if _real is not None:
            self._real_io = getattr(_real, 'intermediate_output', None)

    def fetch_intermediate_output(self, *args, **kwargs):
        if self._real_io is not None:
            try:
                return self._real_io.fetch_intermediate_output(*args, **kwargs)
            except Exception as e:
                logger.error(
                    "Real intermediate_output.fetch_intermediate_output failed: %s",
                    e, exc_info=True
                )
        return None

    def can_fetch_intermediate_output(self, *args, **kwargs):
        if self._real_io is not None:
            try:
                return self._real_io.can_fetch_intermediate_output(*args, **kwargs)
            except Exception as e:
                logger.error(
                    "Real intermediate_output.can_fetch_intermediate_output failed: %s",
                    e, exc_info=True
                )
        return False

    def get_intermediate_output_process_status(self, *args, **kwargs):
        if self._real_io is not None:
            try:
                return self._real_io.get_intermediate_output_process_status(*args, **kwargs)
            except Exception as e:
                logger.error(
                    "Real intermediate_output.get_intermediate_output_process_status failed: %s",
                    e, exc_info=True
                )
        return None

    def get_intermediate_output_data_products(self, *args, **kwargs):
        if self._real_io is not None:
            try:
                return self._real_io.get_intermediate_output_data_products(*args, **kwargs)
            except Exception as e:
                logger.error(
                    "Real intermediate_output.get_intermediate_output_data_products failed: %s",
                    e, exc_info=True
                )
        return []


intermediate_output = _IntermediateOutputProxy()
