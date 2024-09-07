# coffee.py

class Coffee:
    def __init__(self, name):
        """
        Initialize a Coffee with a name.
        Args:
            name (str): The name of the coffee.
        """
        self.name = name  # Validate and set the name
        self._orders = []  # Initialize an empty list to store orders associated with the coffee

    @property
    def name(self):
        """
        Get the coffee's name.
        Returns:
            str: The coffee's name.
        """
        return self._name

    @name.setter
    def name(self, value):
        """
        Set the coffee's name with validation.
        Args:
            value (str): The name to set.
        Raises:
            ValueError: If the name is not a string or is less than 3 characters long.
        """
        if isinstance(value, str) and len(value) >= 3:
            self._name = value
        else:
            raise ValueError("Name must be a string with at least 3 characters.")

    def orders(self):
        """
        Get all orders associated with the coffee.
        Returns:
            list: List of Order objects associated with the coffee.
        """
        return self._orders

    def customers(self):
        """
        Get a list of unique customers who have ordered this coffee.
        Returns:
            list: List of unique Customer objects.
        """
        return list(set(order.customer for order in self._orders))

    def num_orders(self):
        """
        Get the total number of orders for this coffee.
        Returns:
            int: Number of orders.
        """
        return len(self._orders)

    def average_price(self):
        """
        Calculate the average price of the coffee based on all its orders.
        Returns:
            float: The average price of the coffee.
        """
        if not self._orders:  # Check if there are no orders
            return 0
        total_price = sum(order.price for order in self._orders)  # Sum of all order prices
        return total_price / len(self._orders)  # Calculate the average price
# coffee.py

class Coffee:
    def __init__(self, name):
        """
        Initialize a Coffee with a name.
        Args:
            name (str): The name of the coffee.
        """
        self.name = name  # Validate and set the name
        self._orders = []  # Initialize an empty list to store orders associated with the coffee

    @property
    def name(self):
        """
        Get the coffee's name.
        Returns:
            str: The coffee's name.
        """
        return self._name

    @name.setter
    def name(self, value):
        """
        Set the coffee's name with validation.
        Args:
            value (str): The name to set.
        Raises:
            ValueError: If the name is not a string or is less than 3 characters long.
        """
        if isinstance(value, str) and len(value) >= 3:
            self._name = value
        else:
            raise ValueError("Name must be a string with at least 3 characters.")

    def orders(self):
        """
        Get all orders associated with the coffee.
        Returns:
            list: List of Order objects associated with the coffee.
        """
        return self._orders

    def customers(self):
        """
        Get a list of unique customers who have ordered this coffee.
        Returns:
            list: List of unique Customer objects.
        """
        return list(set(order.customer for order in self._orders))

    def num_orders(self):
        """
        Get the total number of orders for this coffee.
        Returns:
            int: Number of orders.
        """
        return len(self._orders)

    def average_price(self):
        """
        Calculate the average price of the coffee based on all its orders.
        Returns:
            float: The average price of the coffee.
        """
        if not self._orders:  # Check if there are no orders
            return 0
        total_price = sum(order.price for order in self._orders)  # Sum of all order prices
        return total_price / len(self._orders)  # Calculate the average price
