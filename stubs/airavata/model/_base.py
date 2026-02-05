"""Base classes for stub Thrift model types."""


class _ThriftStub:
    """Base class for stub Thrift struct types.

    Accepts any keyword arguments and stores them as attributes.
    Has an empty thrift_spec so thrift_utils.create_serializer_class works.
    """
    thrift_spec = ()

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def __repr__(self):
        return "{}({})".format(self.__class__.__name__, self.__dict__)

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__


class _ThriftEnum:
    """Base class for stub Thrift enum types.

    Subclasses should define class-level integer constants and
    _VALUES_TO_NAMES / _NAMES_TO_VALUES dicts.
    """
    _VALUES_TO_NAMES = {}
    _NAMES_TO_VALUES = {}
