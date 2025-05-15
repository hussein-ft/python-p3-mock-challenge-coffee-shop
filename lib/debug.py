#!/usr/bin/env python3
import ipdb
from classes.many_to_many import Coffee, Customer, Order

def debug():
    coffee = Coffee("Latte")
    customer = Customer("Alice")
    order = Order(customer, coffee, 3.5)
    print(f"Coffee: {coffee.name}")
    print(f"Customer: {customer.name}")
    print(f"Order: {order.price}")

if __name__ == "__main__":
    debug()
