# Coffee-shop

# Coffee Shop Domain Modeling

## Objective
Using object-oriented programming principles, create a Python application from scratch to model a Coffee Shop domain. This assessment will test your ability to design classes, implement methods, establish relationships between objects, and handle data appropriately.

## Scenario
You are tasked with building a domain model for a Coffee Shop. Your model will consist of three main entities: `Customer`, `Coffee`, and `Order`. The relationships are as follows:
- A `Customer` can place many `Orders`.
- A `Coffee` can have many `Orders`.
- An `Order` belongs to one `Customer` and one `Coffee`.

The `Customer` and `Coffee` entities have a many-to-many relationship through the `Order` entity.

## Instructions

### 1. Setup and Preparation
- Create a new directory for your project named `coffee_shop`.
- Set up a virtual environment within this directory using `pipenv`:
  ```bash
  pipenv install
  pipenv shell
  ```
- Install any necessary packages, such as `pytest` for testing:
  ```bash
  pipenv install pytest
  ```

### 2. Domain Model Design
- Before coding, sketch your domain model on paper or a whiteboard:
  - Identify the three main classes: `Customer`, `Coffee`, and `Order`.
  - Establish the relationships between these classes.
  - Determine the attributes and methods that each class will have.
  - Keep in mind the concept of a single source of truth for your data.
  - In my Coffee Shop domain model, the single source of truth for the relationships between `Customer`, `Coffee`, and `Order` is the `Order` entity. 

Here's why:
- The `Order` entity holds references to both the `Customer` and the `Coffee` involved in each order.
- It contains the details of the transaction, such as the `price`.
- By querying the `Order` entity, you can derive all necessary information about which customers ordered which coffees and how many times.

This ensures that all data about the interactions between customers and coffees is centralized in one place, maintaining consistency and integrity in your model. If you need to know which coffees a customer has ordered or which customers have ordered a specific coffee, you can always refer to the `Order` entity.

  - Here's a simple sketch of the domain model for the Coffee Shop project. 
```plaintext
+-----------+          +-----------+          +-----------+
|  Customer |          |   Order   |          |   Coffee  |
+-----------+          +-----------+          +-----------+
| - name    |<-------->| - customer|<-------->| - name    |
|           |          | - coffee  |          |           |
|           |          | - price   |          |           |
+-----------+          +-----------+          +-----------+
      ^                      ^                      ^
      |                      |                      |
      +----------------------+----------------------+
```

### Explanation:
- **Customer**: Represents a customer with a `name`.
- **Order**: Represents an order with a `customer`, `coffee`, and `price`.
- **Coffee**: Represents a coffee with a `name`.

### Relationships:
- A `Customer` can place many `Orders`.
- A `Coffee` can have many `Orders`.
- An `Order` belongs to one `Customer` and one `Coffee`.

You can use this sketch to illustrate the relationships between the entities. 


### 3. Create Class Files
- Create three Python files in your project directory:
  - `customer.py`
  - `coffee.py`
  - `order.py`
- In each file, define a class corresponding to the file name (e.g., `class Customer` in `customer.py`).

### 4. Implement Initializers and Properties
- **Customer Class (`customer.py`)**:
  - Initialize a `Customer` with a `name` (string between 1 and 15 characters).
  - Implement a property `name` with the necessary validation.
- **Coffee Class (`coffee.py`)**:
  - Initialize a `Coffee` with a `name` (string, at least 3 characters long).
  - Implement a property `name` with the necessary validation.
- **Order Class (`order.py`)**:
  - Initialize an `Order` with a `Customer` instance, a `Coffee` instance, and a `price` (float between 1.0 and 10.0).
  - Implement properties `customer`, `coffee`, and `price` with the necessary validation.

### 5. Define Object Relationship Methods and Properties
- Implement methods that establish relationships between objects:
  - **Order Class (`order.py`)**:
    - `customer` property returns the `Customer` instance for the order.
    - `coffee` property returns the `Coffee` instance for the order.
  - **Coffee Class (`coffee.py`)**:
    - `orders()` method returns a list of all `Order` instances for that coffee.
    - `customers()` method returns a unique list of `Customer` instances who have ordered that coffee.
  - **Customer Class (`customer.py`)**:
    - `orders()` method returns a list of all `Order` instances for that customer.
    - `coffees()` method returns a unique list of `Coffee` instances that the customer has ordered.

### 6. Implement Aggregate and Association Methods
- **Customer Class (`customer.py`)**:
  - `create_order(coffee, price)` method: Receives a `Coffee` instance and a price, creates a new `Order` instance, and associates it with that customer and the coffee.
- **Coffee Class (`coffee.py`)**:
  - `num_orders()` method: Returns the total number of times a coffee has been ordered.
  - `average_price()` method: Returns the average price for a coffee based on its orders.

### 7. Bonus Task (Optional)
- Implement the `most_aficionado(coffee)` class method in the `Customer` class:
  - Receives a `coffee` object as an argument.
  - Returns the `Customer` instance that has spent the most money on the provided `coffee`.
  - Returns `None` if there are no customers for the provided `coffee`.

### 8. Testing
- Create a `tests` directory and write unit tests for your classes and methods using `pytest`.

## Conclusion
This project will help you practice and demonstrate your understanding of object-oriented programming principles, class design, and relationships between objects. Good luck!
```
