import logging

from fastapi import HTTPException
from fastapi.responses import JSONResponse
from starlette.requests import Request

log = logging.getLogger(__name__)


async def on_http_error(request: Request, exc: HTTPException):
    return JSONResponse({'detail': exc.detail}, status_code=exc.status_code)
