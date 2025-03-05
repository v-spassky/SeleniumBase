from pydantic import BaseModel


class RequestWithURL(BaseModel):
    url: str


class RequestWithCSSSelector(BaseModel):
    selector: str


class RequestWithCSSSelectorAndText(BaseModel):
    selector: str
    text: str
