from dataclasses import dataclass
from datetime import date

# frozen = immutable, slots = True (improve mem usage - have to do more research to understand if this is needed)
@dataclass(frozen=True)
class Order:
    order_id: str
    order_date: date
    ship_mode: str
    segment: str
    country: str
    city: str
    state: str
    postal_code: str
    region: str
    category: str
    sub_category: str
    product_id: str
    cost_price: float
    list_price: float
    quantity: int
    discount_percent: float