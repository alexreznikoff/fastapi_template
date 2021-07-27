from uuid import uuid4

from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.requests import Request
from starlette.responses import Response

from {{ cookiecutter.project_slug }}.utils.request_id import X_REQUEST_ID, request_id_manager


class RequestIdMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
        request_id = request.headers.get(X_REQUEST_ID) or str(uuid4())
        request_id_manager.set(request_id)
        response = await call_next(request)
        response.headers[X_REQUEST_ID] = request_id
        return response
