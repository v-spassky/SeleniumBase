from fastapi import APIRouter

from command import (
    ActivateCDPMode,
    CDPClick,
    CDPPressKeys,
    Connect,
    Disconnect,
    Reconnect,
    UCGUIClickCaptcha,
    UCGUIHandleCaptcha,
)
from mediator import mediator
from schema import RequestWithURL, RequestWithCSSSelector, RequestWithCSSSelectorAndText

router = APIRouter()


@router.post('/activate_cdp_mode')
def activate_cdp_mode(request: RequestWithURL) -> None:
    mediator.send_and_wait_until_executed(ActivateCDPMode(request.url))


@router.post('/connect')
def connect() -> None:
    mediator.send_and_wait_until_executed(Connect())

@router.post('/reconnect')
def reconnect() -> None:
    mediator.send_and_wait_until_executed(Reconnect())


@router.post('/disconnect')
def disconnect() -> None:
    mediator.send_and_wait_until_executed(Disconnect())


@router.post('/uc_gui_handle_captcha')
def uc_gui_handle_captcha() -> None:
    mediator.send_and_wait_until_executed(UCGUIHandleCaptcha())


@router.post('/uc_gui_click_captcha')
def uc_gui_click_captcha() -> None:
    mediator.send_and_wait_until_executed(UCGUIClickCaptcha())


@router.post('/cdp_click')
def cdp_click(request: RequestWithCSSSelector) -> None:
    mediator.send_and_wait_until_executed(CDPClick(request.selector))


@router.post('/cdp_press_keys')
def cdp_press_keys(request: RequestWithCSSSelectorAndText) -> None:
    mediator.send_and_wait_until_executed(CDPPressKeys(request.selector, request.text))
