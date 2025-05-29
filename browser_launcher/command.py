from abc import ABC, abstractmethod

from seleniumbase import SB


class SBCommandResult:
    def __init__(self, raw_result) -> None:
        self.raw_result = raw_result

    @classmethod
    def error(cls) -> 'SBCommandResult':
        return cls('error')

    def __repr__(self) -> str:
        return f'SBCommandResult("{self.raw_result}")'


class SBCommand(ABC):

    @abstractmethod
    def execute_on_sb_driver(self, sb: SB) -> SBCommandResult: ...

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}()'


class ActivateCDPMode(SBCommand):

    def __init__(self, url: str) -> None:
        self.url = url

    def execute_on_sb_driver(self, sb: SB) -> SBCommandResult:
        result = sb.activate_cdp_mode(self.url)
        return SBCommandResult(result)

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}("{self.url}")'


class Connect(SBCommand):

    def execute_on_sb_driver(self, sb: SB) -> SBCommandResult:
        result = sb.connect()
        return SBCommandResult(result)


class Reconnect(SBCommand):

    def execute_on_sb_driver(self, sb: SB) -> SBCommandResult:
        result = sb.reconnect()
        return SBCommandResult(result)


class Disconnect(SBCommand):

    def execute_on_sb_driver(self, sb: SB) -> SBCommandResult:
        result = sb.disconnect()
        return SBCommandResult(result)


class IsConnected(SBCommand):

    def execute_on_sb_driver(self, sb: SB) -> SBCommandResult:
        result = sb.is_connected()
        return SBCommandResult(result)


class UCGUIHandleCaptcha(SBCommand):

    def execute_on_sb_driver(self, sb: SB) -> SBCommandResult:
        result = sb.uc_gui_handle_captcha()
        return SBCommandResult(result)


class UCGUIClickCaptcha(SBCommand):

    def execute_on_sb_driver(self, sb: SB) -> SBCommandResult:
        result = sb.uc_gui_click_captcha()
        return SBCommandResult(result)


class CDPGet(SBCommand):

    def __init__(self, url: str) -> None:
        self.url = url

    def execute_on_sb_driver(self, sb: SB) -> SBCommandResult:
        result = sb.cdp.get(self.url)
        return SBCommandResult(result)

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}("{self.url}")'


class CDPClick(SBCommand):

    def __init__(self, selector: str) -> None:
        self.selector = selector

    def execute_on_sb_driver(self, sb: SB) -> SBCommandResult:
        result = sb.cdp.click(self.selector)
        return SBCommandResult(result)

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}("{self.selector}")'


class CDPGUIClickCoordinates(SBCommand):

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def execute_on_sb_driver(self, sb: SB) -> SBCommandResult:
        result = sb.cdp.gui_click_x_y(self.x, self.y)
        return SBCommandResult(result)

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.x}, {self.y})'


class CDPPressKeys(SBCommand):

    def __init__(self, selector: str, text: str) -> None:
        self.selector = selector
        self.text = text

    def execute_on_sb_driver(self, sb: SB) -> SBCommandResult:
        result = sb.cdp.press_keys(self.selector, self.text)
        return SBCommandResult(result)

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}("{self.selector}", "{self.text}")'


class CDPGetText(SBCommand):

    def __init__(self, selector: str) -> None:
        self.selector = selector

    def execute_on_sb_driver(self, sb: SB) -> SBCommandResult:
        result =  sb.cdp.get_text(self.selector)
        return SBCommandResult(result)

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}("{self.selector}")'


class CDPIsElementVisible(SBCommand):

    def __init__(self, selector: str) -> None:
        self.selector = selector

    def execute_on_sb_driver(self, sb: SB) -> SBCommandResult:
        result = sb.cdp.is_element_visible(self.selector)
        return SBCommandResult(result)

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}("{self.selector}")'


class CDPGetCurrentUrl(SBCommand):

    def execute_on_sb_driver(self, sb: SB) -> SBCommandResult:
        result = sb.cdp.get_current_url()
        return SBCommandResult(result)


class CDPGetPageSource(SBCommand):

    def execute_on_sb_driver(self, sb: SB) -> SBCommandResult:
        result = sb.cdp.get_page_source()
        return SBCommandResult(result)


class CDPFindElementByText(SBCommand):

    def __init__(self, text: str) -> None:
        self.text = text

    def execute_on_sb_driver(self, sb: SB) -> SBCommandResult:
        try:
            result = sb.cdp.find_element_by_text(self.text, timeout=0.1)
        except Exception:
            result = None
        return SBCommandResult(result)

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}("{self.text}")'
