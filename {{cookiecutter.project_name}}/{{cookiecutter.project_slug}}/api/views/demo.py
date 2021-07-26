from fastapi import APIRouter

from {{ cookiecutter.project_slug }}.api.controllers.commmon import get_sum
from {{ cookiecutter.project_slug }}.api.serializers.response import SumResponse

demo_router = APIRouter()


@demo_router.get("/sum", response_model=SumResponse)
async def sum_view(x: int = 5, y: int = 10):
    sum_ = get_sum(x, y)
    return {"sum": sum_}
