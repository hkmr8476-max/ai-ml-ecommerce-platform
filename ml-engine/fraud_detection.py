def fraud_risk_score(order_total: float, orders_last_hour: int, mismatch_geo: bool) -> float:
    score = min(order_total / 1000, 1) * 0.4 + min(orders_last_hour / 10, 1) * 0.4
    if mismatch_geo:
        score += 0.2
    return min(score, 1.0)
