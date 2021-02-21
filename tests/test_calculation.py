import pytest
from app.calculation import PriceCalculator


# state_code: str, price: int, sku_count: int
@pytest.mark.parametrize("test_input,expected", [(('UT', 100, 1), (100.0, 106.85)),
                                                 (('TX', 10000, 1), (9000.0, 9562.5)),
                                                 (('AL', 50000, 2), (85000.0, 88400.0)), (('TX', 0, 0), (0.0, 0.0)),
                                                 (('', 4324, 23423), (0.0, 0.0)), (('AL', 50000, 0), (0.0, 0.0)),
                                                 (('UT', 423424, 233), (83859123.2, 89603473.14))])
def test_eval(test_input, expected):
    output = PriceCalculator(*test_input).calculate()
    assert output == expected