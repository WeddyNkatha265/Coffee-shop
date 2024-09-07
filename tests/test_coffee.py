# tests/test_coffee.py

import pytest
from ..coffee import Coffee
from ..customer import Customer

def test_coffee_name_valid():
    """Test if a valid coffee name is accepted."""
    coffee = Coffee("Latte")
    assert coffee.name == "Latte"

def test_coffee_name_invalid():
    """Test if an invalid coffee name raises a ValueError."""
    with pytest.raises(ValueError):
        Coffee("Al")  # Name less than 3 characters

def test_num_orders():
    """Test if the number of orders for a coffee is correctly counted."""
    coffee = Coffee("Latte")
    customer = Customer("Alice")
    customer.create_order(coffee, 4.5)
    customer.create_order(coffee, 5.0)
    assert coffee.num_orders() == 2  # Should return 2

def test_average_price():
    """Test if the average price for a coffee is correctly calculated."""
    coffee = Coffee("Latte")
    customer = Customer("Alice")
    customer.create_order(coffee, 4.5)
    customer.create_order(coffee, 5.0)
    assert coffee.average_price() == 4.75  # Average of 4.5 and 5.0
