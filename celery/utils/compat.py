from __future__ import absolute_import
from celery.five import *  # noqa

_environment = None


def _detect_environment():
    import sys
    if 'eventlet' in sys.modules:
        try:
            from eventlet.patcher import is_monkey_patched as is_eventlet
            import socket

            if is_eventlet(socket):
                return 'eventlet'
        except ImportError:
            pass

    if 'gevent' in sys.modules:
        try:
            from gevent import socket as _gsocket
            import socket

            if socket.socket is _gsocket.socket:
                return 'gevent'
        except ImportError:
            pass

    return 'default'


def detect_environment():
    global _environment
    if _environment is None:
        _environment = _detect_environment()
    return _environment
