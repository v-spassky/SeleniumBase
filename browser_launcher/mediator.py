import logging
from queue import Queue

from command import SBCommand, SBCommandResult


class SBCommandMediator:

    _logger = logging.getLogger(__name__)

    def __init__(self) -> None:
        self._command_queue: Queue[SBCommand] = Queue()
        self._result_queue: Queue[SBCommandResult] = Queue()

    def send_and_wait_until_executed(self, command: SBCommand) -> SBCommandResult:
        self._command_queue.put(command)
        return self._result_queue.get()

    def get_command(self) -> SBCommand:
        return self._command_queue.get()

    def notify_done(self, command_result: SBCommandResult) -> None:
        self._result_queue.put(command_result)

mediator = SBCommandMediator()
