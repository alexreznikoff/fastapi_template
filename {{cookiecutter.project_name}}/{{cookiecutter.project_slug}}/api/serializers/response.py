from pydantic import BaseModel


class SumResponse(BaseModel):
    sum: int
