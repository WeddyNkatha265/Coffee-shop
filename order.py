# order.py

class Order:
    def __init__(self, customer, coffee, price):
        """
        Initialize an Order with a customer, coffee, and price.
        Args:
            customer (Customer): The customer placing the order.
            coffee (Coffee): The coffee being ordered.
            price (float): The price of the coffee.
        """
        self.customer = customer  # Validate and set the customer
        self.coffee = coffee  # Validate and set the coffee
        self.price = price  # Validate and set the price

        customer.orders().append(self)  # Add the order to the customer's list of orders
        coffee.orders().append(self)  # Add the order to the coffee's list of orders

    @property
    def customer(self):
        """
        Get the customer associated with the order.
        Returns:
            Customer: The customer who placed the order.
        """
        return self._customer

    @customer.setter
    def customer(self, value):
        """
        Set the customer with validation.
        Args:
            value (Customer): The customer to set.
        Raises:
            ValueError: If the customer is not an instance of Customer.
        """
        from .customer import Customer  # Import to avoid circular dependency
        if isinstance(value, Customer):
            self._customer = value
        else:
            raise ValueError("Customer must be an instance of Customer.")

    @property
    def coffee(self):
        """
        Get the coffee associated with the order.
        Returns:
            Coffee: The coffee that was ordered.
        """
        return self._coffee

    @coffee.setter
    def coffee(self, value):
        """
        Set the coffee with validation.
        Args:
            value (Coffee): The coffee to set.
        Raises:
            ValueError: If the coffee is not an instance of Coffee.
        """
        from .coffee import Coffee  # Import to avoid circular dependency
        if isinstance(value, Coffee):
            self._coffee = value
        else:
            raise ValueError("Coffee must be an instance of Coffee.")

    @property
    def price(self):
        """
        Get the price of the order.
        Returns:
            float: The price of the order.
        """
        return self._price

    @price.setter
    def price(self, value):
        """
        Set the price with validation.
        Args:
            value (float): The price to set.
        Raises:
            ValueError: If the price is not a float or is not between 1.0 and 10.0.
        """
        if isinstance(value, float) and 1.0 <= value <= 10.0:
            self._price = value
        else:
            raise ValueError("Price must be a float between 1.0 and 10.0.")
