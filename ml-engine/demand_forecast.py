from statistics import mean


def forecast_next_week(daily_sales: list[float]) -> float:
    if not daily_sales:
        return 0.0
    return mean(daily_sales[-14:]) * 7
