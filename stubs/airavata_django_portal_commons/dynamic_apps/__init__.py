"""Proxy stub for airavata_django_portal_commons.dynamic_apps.

Tries to delegate to the real package if installed; otherwise provides
no-op implementations for dynamic app loading.
"""
import logging
from _proxy import load_real_module, call_real

logger = logging.getLogger(__name__)

_real = load_real_module(
    'airavata_django_portal_commons.dynamic_apps',
    'airavata_django_portal_commons'
)


def load(installed_apps, entry_point_group):
    """Discover and load dynamic Django apps from entry points."""
    return call_real(_real, 'load', None, installed_apps, entry_point_group)


def merge_settings(settings_module):
    """Merge settings from dynamically loaded apps."""
    return call_real(_real, 'merge_settings', None, settings_module)
