def suggest_price(base_price: float, demand_index: float, stock_level: int) -> float:
    demand_factor = 1 + (demand_index - 1) * 0.2
    stock_factor = 1.1 if stock_level < 10 else 1.0
    return round(base_price * demand_factor * stock_factor, 2)
