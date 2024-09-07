# customer.py

class Customer:
    def __init__(self, name):
        """
        Initialize a Customer with a name.
        Args:
            name (str): The name of the customer.
        """
        self.name = name  # Validate and set the name
        self._orders = []  # Initialize an empty list to store the customer's orders

    @property
    def name(self):
        """
        Get the customer's name.
        Returns:
            str: The customer's name.
        """
        return self._name

    @name.setter
    def name(self, value):
        """
        Set the customer's name with validation.
        Args:
            value (str): The name to set.
        Raises:
            ValueError: If the name is not a string or is not between 1 and 15 characters long.
        """
        if isinstance(value, str) and 1 <= len(value) <= 15:
            self._name = value
        else:
            raise ValueError("Name must be a string between 1 and 15 characters long.")

    def orders(self):
        """
        Get all orders associated with the customer.
        Returns:
            list: List of Order objects associated with the customer.
        """
        return self._orders

    def coffees(self):
        """
        Get a list of unique Coffee instances that the customer has ordered.
        Returns:
            list: List of unique Coffee objects.
        """
        return list(set(order.coffee for order in self._orders))

    def create_order(self, coffee, price):
        """
        Create a new order for the customer.
        Args:
            coffee (Coffee): The Coffee object associated with the order.
            price (float): The price of the coffee.
        Returns:
            Order: The newly created Order object.
        """
        from .order import Order  # Import to avoid circular dependency
        new_order = Order(self, coffee, price)  # Create a new order
        self._orders.append(new_order)  # Add the order to the customer's orders list
        return new_order  # Return the newly created order

    @classmethod
    def most_aficionado(cls, coffee):
        """
        Determine the customer who has spent the most on a specific coffee.
        Args:
            coffee (Coffee): The coffee to analyze.
        Returns:
            Customer: The customer who has spent the most on the specified coffee.
            None: If no orders exist for the coffee.
        """
        customers_spending = {}
        for order in coffee.orders():
            if order.customer in customers_spending:
                customers_spending[order.customer] += order.price
            else:
                customers_spending[order.customer] = order.price

        if customers_spending:
            return max(customers_spending, key=customers_spending.get)
        return None
