from fastapi import APIRouter

from app.schemas.common import HealthResponse
from app.schemas.orders import OrderCreate, OrderResponse
from app.schemas.products import Product
from app.services.recommendations import get_recommendations

router = APIRouter()


@router.get('/health', response_model=HealthResponse)
def health_check() -> HealthResponse:
    return HealthResponse(status='ok')


@router.get('/products', response_model=list[Product])
def list_products() -> list[Product]:
    return [
        Product(id=1, name='AI Running Shoes', price=89.99, category='Footwear'),
        Product(id=2, name='Smart Jacket', price=149.0, category='Apparel'),
    ]


@router.post('/orders', response_model=OrderResponse)
def create_order(payload: OrderCreate) -> OrderResponse:
    return OrderResponse(order_id=5001, status=f'created_for_user_{payload.user_id}')


@router.get('/recommendations/{user_id}')
def recommendations(user_id: int) -> dict:
    return {'user_id': user_id, 'product_ids': get_recommendations(user_id)}


@router.get('/search')
def search(q: str) -> dict:
    return {'query': q, 'results': ['AI Running Shoes', 'Smart Jacket']}


@router.post('/auth/login')
def login() -> dict:
    return {'access_token': 'demo-token', 'token_type': 'bearer'}


@router.get('/admin/analytics')
def admin_analytics() -> dict:
    return {'total_orders': 1234, 'revenue': 98765.43}


@router.post('/payments/checkout')
def checkout() -> dict:
    return {'status': 'initiated', 'providers': ['stripe', 'paypal']}
