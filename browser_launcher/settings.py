import os

PROXY_SOCKET = os.getenv('PROXY_SOCKET')
if not PROXY_SOCKET:
    raise RuntimeError('The `PROXY_SOCKET` environment variable is not set.')
