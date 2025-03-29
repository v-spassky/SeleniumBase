import httpx
from fastapi import FastAPI, Request
from fastapi.responses import Response

from network import get_chromedriver_url

app = FastAPI()


@app.api_route("/{path:path}", methods=["GET", "POST", "PUT", "DELETE", "PATCH", "OPTIONS"])
async def proxy(path: str, request: Request) -> Response:
    chromedriver_url = get_chromedriver_url()
    proxy_url = f"{chromedriver_url}/{path}"

    async with httpx.AsyncClient(cookies=request.cookies) as client:
        response = await client.request(
            method=request.method,
            url=proxy_url,
            headers=request.headers,
            params=request.query_params,
            content=await request.body(),
            timeout=60.0
        )

    return Response(
        content=response.content,
        status_code=response.status_code,
        headers=dict(response.headers),
    )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=4444)
