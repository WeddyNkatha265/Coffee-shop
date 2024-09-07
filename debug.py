# debug.py
from customer import Customer
from coffee import Coffee
from order import Order

customer1 = Customer("Alice")
coffee1 = Coffee("Latte")

order1 = customer1.create_order(coffee1, 4.5)
print(customer1.orders())
print(coffee1.customers())
