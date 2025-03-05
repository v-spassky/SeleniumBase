from seleniumbase import SB

import settings
from mediator import mediator


def run_seleniumbase():
    with SB(uc=True, locale_code='en', proxy=settings.PROXY_SOCKET) as sb:
        while True:
            command = mediator.get_command()
            print(f'Received command: {command}, proceeding...')
            command.execute_on_sb_driver(sb)
            print('Command executed.')
            mediator.notify_done()
