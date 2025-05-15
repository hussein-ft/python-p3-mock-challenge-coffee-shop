class Coffee:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) <= 2:
            raise ValueError("Coffee name must be a string longer than 2 characters.")
        self._name = name
        self._orders = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        raise AttributeError("Coffee name is immutable.")

    def orders(self):
        return self._orders

    def customers(self):
        return list(set(order.customer for order in self._orders))

    def num_orders(self):
        return len(self._orders)

    def average_price(self):
        if not self._orders:
            return 0
        return sum(order.price for order in self._orders) / len(self._orders)


class Customer:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) < 1 or len(name) > 15:
            raise ValueError("Customer name must be a string between 1 and 15 characters.")
        self._name = name
        self._orders = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or len(value) < 1 or len(value) > 15:
            raise ValueError("Customer name must be a string between 1 and 15 characters.")
        self._name = value

    def orders(self):
        return self._orders

    def coffees(self):
        return list(set(order.coffee for order in self._orders))

    def create_order(self, coffee, price):
        if not isinstance(coffee, Coffee):
            raise ValueError("Invalid coffee object.")
        if not isinstance(price, (int, float)) or price <= 0:
            raise ValueError("Price must be a positive number.")
        order = Order(self, coffee, price)
        self._orders.append(order)
        coffee.orders().append(order)
        return order


class Order:
    all = []  # Class-level attribute to track all orders

    def __init__(self, customer, coffee, price):
        if not isinstance(customer, Customer):
            raise ValueError("Invalid customer object.")
        if not isinstance(coffee, Coffee):
            raise ValueError("Invalid coffee object.")
        if not isinstance(price, (int, float)) or price <= 0:
            raise ValueError("Price must be a positive number.")
        self._customer = customer
        self._coffee = coffee
        self._price = price
        customer.orders().append(self)
        coffee.orders().append(self)
        Order.all.append(self)

    @property
    def customer(self):
        return self._customer

    @property
    def coffee(self):
        return self._coffee

    @property
    def price(self):
        return self._price