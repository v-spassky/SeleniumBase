import logging
from queue import Queue

from command import SBCommand


class SBCommandMediator:

    DONE = object()
    _logger = logging.getLogger(__name__)

    def __init__(self) -> None:
        self._command_queue = Queue()
        self._done_queue = Queue()

    def send_and_wait_until_executed(self, command: SBCommand) -> None:
        self._expect_command_queue_size(0)
        self._expect_done_queue_size(0)
        self._command_queue.put(command)
        self._done_queue.get()

    def get_command(self) -> SBCommand:
        self._expect_command_queue_size(0)
        self._expect_done_queue_size(0)
        return self._command_queue.get()

    def notify_done(self):
        self._expect_command_queue_size(0)
        self._expect_done_queue_size(0)
        self._done_queue.put(self.DONE)

    def _expect_command_queue_size(self, expected_size: int) -> None:
        actual_size = self._command_queue.qsize()
        if not actual_size == expected_size:
            self._logger.warning(f'Expected `self._command_queue` size to be {expected_size}, but got {actual_size}.')

    def _expect_done_queue_size(self, size: int) -> None:
        actual_size = self._done_queue.qsize()
        if not actual_size == size:
            self._logger.warning(f'Expected `self._done_queue` size to be {size}, but got {actual_size}.')


mediator = SBCommandMediator()
