from pydantic import BaseModel


class RequestWithURL(BaseModel):
    url: str


class RequestWithCSSSelector(BaseModel):
    selector: str


class RequestWithText(BaseModel):
    text: str


class RequestWithCSSSelectorAndText(BaseModel):
    selector: str
    text: str


class SBCommandResponse(BaseModel):
    result: str


class ImageLocation(BaseModel):
    located: bool
    x: int | None
    y: int | None
