import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def _load_module(file_name: str, module_name: str):
    module_path = ROOT / 'ml-engine' / file_name
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    module = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(module)
    return module


def test_forecast_positive():
    demand_forecast = _load_module('demand_forecast.py', 'demand_forecast')
    assert demand_forecast.forecast_next_week([10, 11, 12, 13, 14, 15, 16]) > 0


def test_fraud_range():
    fraud_detection = _load_module('fraud_detection.py', 'fraud_detection')
    score = fraud_detection.fraud_risk_score(500, 3, True)
    assert 0 <= score <= 1
