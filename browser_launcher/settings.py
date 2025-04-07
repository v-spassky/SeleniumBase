import os

PROXY_SOCKET = os.getenv('PROXY_SOCKET')
if not PROXY_SOCKET:
    raise RuntimeError('The `PROXY_SOCKET` environment variable is not set.')

USER_DATA_DIR_PATH = '/user_data'

EXTENSIONS = os.getenv('EXTENSIONS').split(',') if os.getenv('EXTENSIONS') else []
