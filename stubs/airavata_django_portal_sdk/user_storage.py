"""Proxy stub for airavata_django_portal_sdk.user_storage.

Tries to delegate to the real SDK if installed; otherwise returns defaults.
"""
import logging
from _proxy import load_real_module, call_real

logger = logging.getLogger(__name__)

_real = load_real_module(
    'airavata_django_portal_sdk.user_storage',
    'airavata_django_portal_sdk'
)


def exists(*args, **kwargs):
    return call_real(_real, 'exists', False, *args, **kwargs)


def dir_exists(*args, **kwargs):
    return call_real(_real, 'dir_exists', False, *args, **kwargs)


def experiment_dir_exists(*args, **kwargs):
    return call_real(_real, 'experiment_dir_exists', False, *args, **kwargs)


def get_data_product_metadata(*args, **kwargs):
    return call_real(
        _real, 'get_data_product_metadata',
        {"path": "", "userHasWriteAccess": False},
        *args, **kwargs
    )


def get_file_metadata(*args, **kwargs):
    return call_real(_real, 'get_file_metadata', {}, *args, **kwargs)


def save(*args, **kwargs):
    return call_real(_real, 'save', None, *args, **kwargs)


def save_input_file(*args, **kwargs):
    return call_real(_real, 'save_input_file', None, *args, **kwargs)


def update_file_content(*args, **kwargs):
    return call_real(_real, 'update_file_content', None, *args, **kwargs)


def update_data_product_content(*args, **kwargs):
    return call_real(_real, 'update_data_product_content', None, *args, **kwargs)


def delete(*args, **kwargs):
    return call_real(_real, 'delete', None, *args, **kwargs)


def delete_dir(*args, **kwargs):
    return call_real(_real, 'delete_dir', None, *args, **kwargs)


def delete_user_file(*args, **kwargs):
    return call_real(_real, 'delete_user_file', None, *args, **kwargs)


def listdir(*args, **kwargs):
    return call_real(_real, 'listdir', ([], []), *args, **kwargs)


def list_experiment_dir(*args, **kwargs):
    return call_real(_real, 'list_experiment_dir', ([], []), *args, **kwargs)


def get_download_url(*args, **kwargs):
    return call_real(_real, 'get_download_url', "", *args, **kwargs)


def get_lazy_download_url(*args, **kwargs):
    return call_real(_real, 'get_lazy_download_url', "", *args, **kwargs)


def is_input_file(*args, **kwargs):
    return call_real(_real, 'is_input_file', False, *args, **kwargs)


def create_user_dir(*args, **kwargs):
    return call_real(_real, 'create_user_dir', None, *args, **kwargs)


def create_symlink(*args, **kwargs):
    return call_real(_real, 'create_symlink', None, *args, **kwargs)


def open_file(*args, **kwargs):
    return call_real(_real, 'open_file', None, *args, **kwargs)
