from abc import ABC, abstractmethod

from pydantic import BaseModel
from seleniumbase import SB


class SBCommandResult(BaseModel):

    @classmethod
    def error(cls, message: str) -> 'SBCommandResult':
        return ErrorResult(message=message)


class ErrorResult(SBCommandResult):
    message: str


class EmptyResult(SBCommandResult):
    ...


class IsDriverConnectedResult(SBCommandResult):
    is_connected: bool


class GetTextResult(SBCommandResult):
    text: str | None


class IsElementVisibleResult(SBCommandResult):
    is_visible: bool


class GetCurrentURLResult(SBCommandResult):
    url: str


class GetPageSourceResult(SBCommandResult):
    page_source: str


class IsTextOnPageResult(SBCommandResult):
    is_found: bool


class SBCommand(ABC):

    @abstractmethod
    def execute_on_sb_driver(self, sb: SB) -> SBCommandResult: ...

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}()'


class ActivateCDPMode(SBCommand):

    def __init__(self, url: str) -> None:
        self.url = url

    def execute_on_sb_driver(self, sb: SB) -> SBCommandResult:
        sb.activate_cdp_mode(self.url)
        return EmptyResult()

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}("{self.url}")'


class Connect(SBCommand):

    def execute_on_sb_driver(self, sb: SB) -> SBCommandResult:
        sb.connect()
        return EmptyResult()


class Reconnect(SBCommand):

    def execute_on_sb_driver(self, sb: SB) -> SBCommandResult:
        sb.reconnect()
        return EmptyResult()


class Disconnect(SBCommand):

    def execute_on_sb_driver(self, sb: SB) -> SBCommandResult:
        sb.disconnect()
        return EmptyResult()


class IsConnected(SBCommand):

    def execute_on_sb_driver(self, sb: SB) -> SBCommandResult:
        is_connected = sb.is_connected()
        return IsDriverConnectedResult(is_connected)


class UCGUIHandleCaptcha(SBCommand):

    def execute_on_sb_driver(self, sb: SB) -> SBCommandResult:
        sb.uc_gui_handle_captcha()
        return EmptyResult()


class UCGUIClickCaptcha(SBCommand):

    def execute_on_sb_driver(self, sb: SB) -> SBCommandResult:
        sb.uc_gui_click_captcha()
        return EmptyResult()


class CDPGet(SBCommand):

    def __init__(self, url: str) -> None:
        self.url = url

    def execute_on_sb_driver(self, sb: SB) -> SBCommandResult:
        sb.cdp.get(self.url)
        return EmptyResult()

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}("{self.url}")'


class CDPClick(SBCommand):

    def __init__(self, selector: str) -> None:
        self.selector = selector

    def execute_on_sb_driver(self, sb: SB) -> SBCommandResult:
        sb.cdp.click(self.selector)
        return EmptyResult()

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}("{self.selector}")'


class CDPGUIClickCoordinates(SBCommand):

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def execute_on_sb_driver(self, sb: SB) -> SBCommandResult:
        sb.cdp.gui_click_x_y(self.x, self.y)
        return EmptyResult()

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.x}, {self.y})'


class CDPPressKeys(SBCommand):

    def __init__(self, selector: str, text: str) -> None:
        self.selector = selector
        self.text = text

    def execute_on_sb_driver(self, sb: SB) -> SBCommandResult:
        sb.cdp.press_keys(self.selector, self.text)
        return EmptyResult()

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}("{self.selector}", "{self.text}")'


class CDPGetText(SBCommand):

    def __init__(self, selector: str) -> None:
        self.selector = selector

    def execute_on_sb_driver(self, sb: SB) -> SBCommandResult:
        text = sb.cdp.get_text(self.selector)
        return GetTextResult(text=text)

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}("{self.selector}")'


class CDPIsElementVisible(SBCommand):

    def __init__(self, selector: str) -> None:
        self.selector = selector

    def execute_on_sb_driver(self, sb: SB) -> SBCommandResult:
        is_visible = sb.cdp.is_element_visible(self.selector)
        return IsElementVisibleResult(is_visible=is_visible)

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}("{self.selector}")'


class CDPGetCurrentUrl(SBCommand):

    def execute_on_sb_driver(self, sb: SB) -> SBCommandResult:
        url = sb.cdp.get_current_url()
        return GetCurrentURLResult(url=url)


class CDPGetPageSource(SBCommand):

    def execute_on_sb_driver(self, sb: SB) -> SBCommandResult:
        page_source = sb.cdp.get_page_source()
        return GetPageSourceResult(page_source=page_source)


class CDPIsTextOnPage(SBCommand):

    def __init__(self, text: str) -> None:
        self.text = text

    def execute_on_sb_driver(self, sb: SB) -> SBCommandResult:
        try:
            _element = sb.cdp.find_element_by_text(self.text, timeout=0.1)
            return IsTextOnPageResult(is_found=True)
        except Exception:
            return IsTextOnPageResult(is_found=False)

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}("{self.text}")'


class CDPCloseActiveTab(SBCommand):

    def execute_on_sb_driver(self, sb: SB) -> SBCommandResult:
        sb.cdp.close_active_tab()
        return EmptyResult()


class CDPSwitchToNewestTab(SBCommand):

    def execute_on_sb_driver(self, sb: SB) -> SBCommandResult:
        sb.cdp.switch_to_newest_tab()
        return EmptyResult()
