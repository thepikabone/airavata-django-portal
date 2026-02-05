"""Shared proxy helper for SDK stub modules.

Provides utilities to attempt loading the real package (if installed)
and delegating calls to it, falling back to defaults on any error.
All calls are logged at DEBUG level for full observability.
"""
import sys
import os
import importlib
import logging

logger = logging.getLogger("airavata_stubs")
_stubs_dir = os.path.normpath(os.path.dirname(os.path.abspath(__file__)))

MAX_REPR_LEN = 200


def _summarize(value):
    """Produce a short, readable representation of a value for log messages."""
    if value is None:
        return "None"
    if isinstance(value, (bool, int, float)):
        return repr(value)
    if isinstance(value, str):
        if len(value) > 80:
            return repr(value[:77] + "...")
        return repr(value)
    if isinstance(value, dict):
        return "<dict(%d keys)>" % len(value)
    if isinstance(value, (list, tuple)):
        return "<%s(%d items)>" % (type(value).__name__, len(value))
    r = repr(value)
    if len(r) > MAX_REPR_LEN:
        return r[:MAX_REPR_LEN - 3] + "..."
    return r


def _summarize_args(args, kwargs):
    """Produce a short summary of function arguments for log messages.

    Avoids dumping large objects like Django request objects.
    """
    parts = []
    for a in args:
        cls_name = type(a).__name__
        if cls_name in ('WSGIRequest', 'HttpRequest', 'DRFRequest',
                        'ASGIRequest', 'Request'):
            parts.append("<%s>" % cls_name)
        elif isinstance(a, str):
            if len(a) > 60:
                parts.append(repr(a[:57] + "..."))
            else:
                parts.append(repr(a))
        elif isinstance(a, (bool, int, float, type(None))):
            parts.append(repr(a))
        elif isinstance(a, (list, tuple)):
            parts.append("<%s(%d)>" % (type(a).__name__, len(a)))
        elif isinstance(a, dict):
            parts.append("<dict(%d)>" % len(a))
        else:
            parts.append("<%s>" % cls_name)
    for k, v in kwargs.items():
        cls_name = type(v).__name__
        if cls_name in ('WSGIRequest', 'HttpRequest', 'DRFRequest',
                        'ASGIRequest', 'Request'):
            parts.append("%s=<%s>" % (k, cls_name))
        elif isinstance(v, (bool, int, float, str, type(None))):
            r = repr(v)
            if len(r) > 60:
                r = r[:57] + "..."
            parts.append("%s=%s" % (k, r))
        else:
            parts.append("%s=<%s>" % (k, cls_name))
    return ", ".join(parts)


def load_real_module(module_name, package_prefix):
    """Try to import the real module by temporarily hiding stubs from sys.path.

    Returns the real module if found, or None if not installed / failed.
    """
    saved_path = sys.path[:]
    saved_modules = {}
    sys.path = [p for p in sys.path if os.path.normpath(p) != _stubs_dir]
    to_remove = [
        k for k in sys.modules
        if k == module_name or k.startswith(package_prefix + ".")
    ]
    for k in to_remove:
        saved_modules[k] = sys.modules.pop(k)
    try:
        real = importlib.import_module(module_name)
        logger.info("[PROXY] Loaded real module: %s", module_name)
        return real
    except ImportError:
        logger.info("[PROXY] Using stub fallback for: %s (real package not installed)", module_name)
        return None
    except Exception as e:
        logger.warning("[PROXY] Failed to load real %s: %s", module_name, e)
        return None
    finally:
        sys.path = saved_path
        for k, v in saved_modules.items():
            sys.modules[k] = v


def call_real(real_module, func_name, default, *args, **kwargs):
    """Call a function on the real module, falling back to default on error.

    Logs every call at DEBUG level with [REAL] or [STUB] prefix.
    """
    if real_module is not None:
        try:
            result = getattr(real_module, func_name)(*args, **kwargs)
            logger.debug(
                "[REAL] %s.%s(%s) -> %s",
                real_module.__name__, func_name,
                _summarize_args(args, kwargs), _summarize(result),
            )
            return result
        except Exception as e:
            logger.error(
                "[REAL] %s.%s(%s) raised %s: %s",
                real_module.__name__, func_name,
                _summarize_args(args, kwargs),
                type(e).__name__, e,
                exc_info=True,
            )
    logger.debug(
        "[STUB] %s(%s) -> %s (default)",
        func_name, _summarize_args(args, kwargs), _summarize(default),
    )
    return default
