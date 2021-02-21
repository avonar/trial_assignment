# Количество товаров.
# Цена за товар.
# Код штата.
from typing import Tuple


class PriceCalculator:
    DISCOUNTS = ({
        'price': 1000,
        'discount': 3
    }, {
        'price': 5000,
        'discount': 5
    }, {
        'price': 7000,
        'discount': 7
    }, {
        'price': 10000,
        'discount': 10
    }, {
        'price': 50000,
        'discount': 15
    })
    STATE_TAXES = {'UT': 6.85, 'NV': 8, 'TX': 6.25, 'AL': 4, 'CA': 8.25}

    def __init__(self, state_code: str, price: int, sku_count: int):
        self.state_code = state_code
        self.price = price
        self.sku_count = sku_count

    def calculate(self) -> Tuple[float, float]:
        if self.state_code not in self.STATE_TAXES:
            return 0, 0
        if self.price < 0 or self.sku_count < 0:
            return 0, 0
        price_with_discount = self._calculate_price_with_discount(self.price * self.sku_count)
        total_price = self._calculate_price_with_taxes(price_with_discount, self.state_code)

        return round(price_with_discount, 2), round(total_price, 2)

    def _get_max_dicount(self, total_price):
        avalaible_discounts = [i['discount'] for i in self.DISCOUNTS if total_price >= i['price']]
        return max(avalaible_discounts) if avalaible_discounts else 0

    def _calculate_price_with_discount(self, total_price):
        total_price = total_price - (total_price / 100 * self._get_max_dicount(total_price))
        return total_price

    def _calculate_price_with_taxes(self, total_price, state):
        total_price = total_price + (total_price / 100 * self.STATE_TAXES[state])
        return total_price
