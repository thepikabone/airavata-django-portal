"""Proxy stub for airavata_django_portal_sdk.queue_settings_calculators.

Tries to delegate to the real SDK if installed; otherwise returns defaults.
"""
import logging
from _proxy import load_real_module, call_real

logger = logging.getLogger(__name__)

_real = load_real_module(
    'airavata_django_portal_sdk.queue_settings_calculators',
    'airavata_django_portal_sdk'
)


def get_all():
    return call_real(_real, 'get_all', [])


def exists(calculator_id):
    return call_real(_real, 'exists', False, calculator_id)


def calculate_queue_settings(pk, request, experiment_model):
    return call_real(
        _real, 'calculate_queue_settings', {},
        pk, request, experiment_model
    )
