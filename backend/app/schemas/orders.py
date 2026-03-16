from pydantic import BaseModel


class OrderCreate(BaseModel):
    user_id: int
    product_ids: list[int]


class OrderResponse(BaseModel):
    order_id: int
    status: str
