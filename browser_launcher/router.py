import pyautogui
from fastapi import APIRouter

from command import (
    ActivateCDPMode,
    CDPClearCookies,
    CDPClick,
    CDPCloseActiveTab,
    CDPIsElementVisible,
    CDPGet,
    CDPGetCurrentUrl,
    CDPGetPageSource,
    CDPGUIClickCoordinates,
    CDPIsTextOnPage,
    CDPGetText,
    CDPPressKeys,
    CDPSwitchToNewestTab,
    Connect,
    Disconnect,
    IsConnected,
    Reconnect,
    UCGUIClickCaptcha,
    UCGUIHandleCaptcha,
    GetCurrentURLResult,
    EmptyResult,
    IsDriverConnectedResult,
    GetTextResult,
    IsElementVisibleResult,
    GetPageSourceResult,
    IsTextOnPageResult,
)
from mediator import mediator
from schema import (
    ImageLocation,
    RequestWithCoordinates,
    RequestWithURL,
    RequestWithCSSSelector,
    RequestWithCSSSelectorAndText,
    RequestWithText,
)

router = APIRouter()


@router.post('/activate_cdp_mode')
def activate_cdp_mode(request: RequestWithURL) -> EmptyResult:
    return mediator.send_and_wait_until_executed(ActivateCDPMode(request.url))


@router.post('/connect')
def connect() -> EmptyResult:
    return mediator.send_and_wait_until_executed(Connect())

@router.post('/reconnect')
def reconnect() -> EmptyResult:
    return mediator.send_and_wait_until_executed(Reconnect())


@router.post('/disconnect')
def disconnect() -> EmptyResult:
    return mediator.send_and_wait_until_executed(Disconnect())


@router.post('/is_connected')
def is_connected() -> IsDriverConnectedResult:
    return mediator.send_and_wait_until_executed(IsConnected())


@router.post('/uc_gui_handle_captcha')
def uc_gui_handle_captcha() -> EmptyResult:
    return mediator.send_and_wait_until_executed(UCGUIHandleCaptcha())


@router.post('/uc_gui_click_captcha')
def uc_gui_click_captcha() -> EmptyResult:
    return mediator.send_and_wait_until_executed(UCGUIClickCaptcha())


@router.post('/cdp_get')
def cdp_get(request: RequestWithURL) -> EmptyResult:
    return mediator.send_and_wait_until_executed(CDPGet(request.url))


@router.post('/cdp_click')
def cdp_click(request: RequestWithCSSSelector) -> EmptyResult:
    return mediator.send_and_wait_until_executed(CDPClick(request.selector))


@router.post('/cdp_press_keys')
def cdp_press_keys(request: RequestWithCSSSelectorAndText) -> EmptyResult:
    return mediator.send_and_wait_until_executed(CDPPressKeys(request.selector, request.text))


@router.post('/cdp_get_text')
def cdp_get_text(request: RequestWithCSSSelector) -> GetTextResult:
    return mediator.send_and_wait_until_executed(CDPGetText(request.selector))


@router.post('/cdp_is_element_visible')
def cdp_is_element_visible(request: RequestWithCSSSelector) -> IsElementVisibleResult:
    return mediator.send_and_wait_until_executed(CDPIsElementVisible(request.selector))


@router.post('/cdp_get_current_url')
def cdp_get_current_url() -> GetCurrentURLResult:
    return mediator.send_and_wait_until_executed(CDPGetCurrentUrl())


@router.post('/cdp_get_page_source')
def cdp_get_page_source() -> GetPageSourceResult:
    return mediator.send_and_wait_until_executed(CDPGetPageSource())


@router.post('/cdp_is_text_on_page')
def cdp_is_text_on_page(request: RequestWithText) -> IsTextOnPageResult:
    return mediator.send_and_wait_until_executed(CDPIsTextOnPage(request.text))


@router.post('/cdp_gui_click_coordinates')
def cdp_gui_click_coordinates(request: RequestWithCoordinates) -> EmptyResult:
    return mediator.send_and_wait_until_executed(CDPGUIClickCoordinates(request.x, request.y))


@router.post('/cdp_close_active_tab')
def cdp_close_active_tab() -> EmptyResult:
    return mediator.send_and_wait_until_executed(CDPCloseActiveTab())


@router.post('/cdp_switch_to_newest_tab')
def cdp_switch_to_newest_tab() -> EmptyResult:
    return mediator.send_and_wait_until_executed(CDPSwitchToNewestTab())


@router.post('/cdp_clear_cookies')
def cdp_clear_cookies() -> EmptyResult:
    return mediator.send_and_wait_until_executed(CDPClearCookies())


@router.get('/locate_on_screen/{image_name}')
def locate_on_screen(image_name: str) -> ImageLocation:
    try:
        bounding_box = pyautogui.locateOnScreen(f'images/{image_name}.png', confidence=0.8)
        center = pyautogui.center(bounding_box)
        return ImageLocation(located=True, x=int(center.x), y=int(center.y))
    except pyautogui.ImageNotFoundException:
        return ImageLocation(located=False, x=None, y=None)
