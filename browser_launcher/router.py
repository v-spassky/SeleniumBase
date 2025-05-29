import pyautogui
from fastapi import APIRouter

from command import (
    ActivateCDPMode,
    CDPClick,
    CDPIsElementVisible,
    CDPGet,
    CDPGetCurrentUrl,
    CDPGetPageSource,
    CDPGUIClickCoordinates,
    CDPFindElementByText,
    CDPGetText,
    CDPPressKeys,
    Connect,
    Disconnect,
    IsConnected,
    Reconnect,
    UCGUIClickCaptcha,
    UCGUIHandleCaptcha,
)
from mediator import mediator
from schema import (
    ImageLocation,
    RequestWithCoordinates,
    RequestWithURL,
    RequestWithCSSSelector,
    RequestWithCSSSelectorAndText,
    SBCommandResponse,
    RequestWithText,
)

router = APIRouter()


@router.post('/activate_cdp_mode')
def activate_cdp_mode(request: RequestWithURL) -> SBCommandResponse:
    result = mediator.send_and_wait_until_executed(ActivateCDPMode(request.url))
    return SBCommandResponse(result=str(result.raw_result))


@router.post('/connect')
def connect() -> SBCommandResponse:
    result = mediator.send_and_wait_until_executed(Connect())
    return SBCommandResponse(result=str(result.raw_result))

@router.post('/reconnect')
def reconnect() -> SBCommandResponse:
    result = mediator.send_and_wait_until_executed(Reconnect())
    return SBCommandResponse(result=str(result.raw_result))


@router.post('/disconnect')
def disconnect() -> SBCommandResponse:
    result = mediator.send_and_wait_until_executed(Disconnect())
    return SBCommandResponse(result=str(result.raw_result))


@router.post('/is_connected')
def is_connected() -> SBCommandResponse:
    result = mediator.send_and_wait_until_executed(IsConnected())
    return SBCommandResponse(result=str(result.raw_result))


@router.post('/uc_gui_handle_captcha')
def uc_gui_handle_captcha() -> SBCommandResponse:
    result = mediator.send_and_wait_until_executed(UCGUIHandleCaptcha())
    return SBCommandResponse(result=str(result.raw_result))


@router.post('/uc_gui_click_captcha')
def uc_gui_click_captcha() -> SBCommandResponse:
    result = mediator.send_and_wait_until_executed(UCGUIClickCaptcha())
    return SBCommandResponse(result=str(result.raw_result))


@router.post('/cdp_get')
def cdp_get(request: RequestWithURL) -> SBCommandResponse:
    result = mediator.send_and_wait_until_executed(CDPGet(request.url))
    return SBCommandResponse(result=str(result.raw_result))


@router.post('/cdp_click')
def cdp_click(request: RequestWithCSSSelector) -> SBCommandResponse:
    result = mediator.send_and_wait_until_executed(CDPClick(request.selector))
    return SBCommandResponse(result=str(result.raw_result))


@router.post('/cdp_press_keys')
def cdp_press_keys(request: RequestWithCSSSelectorAndText) -> SBCommandResponse:
    result = mediator.send_and_wait_until_executed(CDPPressKeys(request.selector, request.text))
    return SBCommandResponse(result=str(result.raw_result))


@router.post('/cdp_get_text')
def cdp_get_text(request: RequestWithCSSSelector) -> SBCommandResponse:
    result = mediator.send_and_wait_until_executed(CDPGetText(request.selector))
    return SBCommandResponse(result=str(result.raw_result))


@router.post('/cdp_is_element_visible')
def cdp_is_element_visible(request: RequestWithCSSSelector) -> SBCommandResponse:
    result = mediator.send_and_wait_until_executed(CDPIsElementVisible(request.selector))
    return SBCommandResponse(result=str(result.raw_result))


@router.post('/cdp_get_current_url')
def cdp_get_current_url() -> SBCommandResponse:
    result = mediator.send_and_wait_until_executed(CDPGetCurrentUrl())
    return SBCommandResponse(result=str(result.raw_result))


@router.post('/cdp_get_page_source')
def cdp_get_page_source() -> SBCommandResponse:
    result = mediator.send_and_wait_until_executed(CDPGetPageSource())
    return SBCommandResponse(result=str(result.raw_result))


@router.post('/cdp_is_text_on_page')
def cdp_is_text_on_page(request: RequestWithText) -> SBCommandResponse:
    result = mediator.send_and_wait_until_executed(CDPFindElementByText(request.text))
    return SBCommandResponse(result=str(result.raw_result))


@router.post('/cdp_gui_click_coordinates')
def cdp_gui_click_coordinates(request: RequestWithCoordinates) -> SBCommandResponse:
    result = mediator.send_and_wait_until_executed(CDPGUIClickCoordinates(request.x, request.y))
    return SBCommandResponse(result=str(result.raw_result))


@router.get('/locate_on_screen/recaptcha_check_mark')
def locate_recaptcha_check_mark() -> ImageLocation:
    try:
        bounding_box = pyautogui.locateOnScreen('images/recaptcha_check_mark.png', confidence=0.8)
        center = pyautogui.center(bounding_box)
        return ImageLocation(located=True, x=int(center.x), y=int(center.y))
    except pyautogui.ImageNotFoundException:
        return ImageLocation(located=False, x=None, y=None)
