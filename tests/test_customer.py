# tests/test_customer.py

import pytest
from ..customer import Customer
from ..coffee import Coffee

def test_customer_name_valid():
    """Test if a valid customer name is accepted."""
    customer = Customer("Alice")
    assert customer.name == "Alice"

def test_customer_name_invalid():
    """Test if an invalid customer name raises a ValueError."""
    with pytest.raises(ValueError):
        Customer("A" * 16)  # Name exceeds 15 characters

def test_create_order():
    """Test if an order is successfully created for a customer."""
    customer = Customer("Alice")
    coffee = Coffee("Espresso")
    order = customer.create_order(coffee, 5.0)
    assert order in customer.orders()  # Ensure order is in customer's orders
    assert coffee in customer.coffees()  # Ensure coffee is in customer's list of coffees

def test_most_aficionado():
    """Test if the customer who spent the most on a specific coffee is identified."""
    customer1 = Customer("Alice")
    customer2 = Customer("Bob")
    coffee = Coffee("Latte")
    customer1.create_order(coffee, 4.5)
    customer1.create_order(coffee, 5.0)
    customer2.create_order(coffee, 3.5)
    assert Customer.most_aficionado(coffee) == customer1  # Alice should be the aficionado
