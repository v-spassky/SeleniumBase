from abc import ABC, abstractmethod

from seleniumbase import SB


class SBCommand(ABC):

    @abstractmethod
    def execute_on_sb_driver(self, sb: SB) -> None: ...

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}()'


class ActivateCDPMode(SBCommand):

    def __init__(self, url: str) -> None:
        self.url = url

    def execute_on_sb_driver(self, sb: SB) -> None:
        sb.activate_cdp_mode(self.url)

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.url})'


class Connect(SBCommand):

    def execute_on_sb_driver(self, sb: SB) -> None:
        sb.connect()


class Reconnect(SBCommand):

    def execute_on_sb_driver(self, sb: SB) -> None:
        sb.reconnect()


class Disconnect(SBCommand):

    def execute_on_sb_driver(self, sb: SB) -> None:
        sb.disconnect()


class UCGUIHandleCaptcha(SBCommand):

    def execute_on_sb_driver(self, sb: SB) -> None:
        sb.uc_gui_handle_captcha()


class UCGUIClickCaptcha(SBCommand):

    def execute_on_sb_driver(self, sb: SB) -> None:
        sb.uc_gui_click_captcha()


class CDPClick(SBCommand):

    def __init__(self, selector: str) -> None:
        self.selector = selector

    def execute_on_sb_driver(self, sb: SB) -> None:
        sb.cdp.click(self.selector)

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.selector})'


class CDPPressKeys(SBCommand):

    def __init__(self, selector: str, text: str) -> None:
        self.selector = selector
        self.text = text

    def execute_on_sb_driver(self, sb: SB) -> None:
        sb.cdp.press_keys(self.selector, self.text)

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.selector}, {self.keys})'
