import pytest
from classes.many_to_many import Coffee

class TestCofi:
    """Additional tests for Coffee class"""

    def test_empty_orders(self):
        coffee = Coffee("Americano")
        assert coffee.num_orders() == 0
        assert coffee.average_price() == 0