"""Proxy stub for airavata_django_portal_commons.dynamic_apps.context_processors."""
import logging
from _proxy import load_real_module, call_real

logger = logging.getLogger(__name__)

_real = load_real_module(
    'airavata_django_portal_commons.dynamic_apps.context_processors',
    'airavata_django_portal_commons'
)


def custom_app_registry(request):
    """Return custom app registry for template context."""
    return call_real(_real, 'custom_app_registry', {'custom_apps': []}, request)
