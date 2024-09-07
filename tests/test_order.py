# tests/test_order.py

import pytest
from ..customer import Customer
from ..coffee import Coffee
from ..order import Order

def test_order_creation():
    """Test if an order is successfully created with valid inputs."""
    customer = Customer("Alice")
    coffee = Coffee("Latte")
    order = Order(customer, coffee, 4.5)
    assert order.customer == customer  # Ensure the customer is correctly set
    assert order.coffee == coffee  # Ensure the coffee is correctly set
    assert order.price == 4.5  # Ensure the price is correctly set

def test_order_price_invalid():
    """Test if an invalid order price raises a ValueError."""
    customer = Customer("Alice")
    coffee = Coffee("Latte")
    with pytest.raises(ValueError):
        Order(customer, coffee, 0.5)  # Price less than 1.0
    with pytest.raises(ValueError):
        Order(customer, coffee, 10.5)  # Price more than 10.0
