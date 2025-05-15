import pytest
from classes.many_to_many import Coffee, Customer, Order

class TestCoffee:
    """Tests for the Coffee class"""

    def test_has_name(self):
        coffee = Coffee("Mocha")
        assert coffee.name == "Mocha"

    def test_name_is_valid_string(self):
        coffee = Coffee("Mocha")
        assert isinstance(coffee.name, str)
        with pytest.raises(ValueError):
            Coffee(2.0)
        with pytest.raises(ValueError):
            Coffee("me")

    def test_name_is_immutable(self):
        coffee = Coffee("Mocha")
        with pytest.raises(AttributeError):
            coffee.name = "Peppermint Mocha"

    def test_has_many_orders(self):
        coffee = Coffee("Latte")
        customer = Customer("Alice")
        order1 = Order(customer, coffee, 3.5)
        order2 = Order(customer, coffee, 4.0)
        assert len(coffee.orders()) == 2
        assert order1 in coffee.orders()
        assert order2 in coffee.orders()

    def test_average_price(self):
        coffee = Coffee("Espresso")
        customer = Customer("Bob")
        Order(customer, coffee, 2.0)
        Order(customer, coffee, 4.0)
        assert coffee.average_price() == 3.0