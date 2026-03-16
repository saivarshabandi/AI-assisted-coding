# For the following e-commerce system features, select the most appropriate data structure:
# 1. Shopping Cart Management
# 2. Order Processing System
# 3. Top-Selling Products Tracker
# 4. Product Search Engine
# 5. Delivery Route Planning

# Choose from: Stack, Queue, Priority Queue, Linked List, Binary Search Tree, Graph, Hash Table, Deque.

# Provide a table mapping:
# Feature → Data Structure → Justification (2–3 sentences).

# Also implement one chosen feature as a Python program with comments and docstrings.
# Table mapping features to data structures
# Feature                     | Data Structure     | Justification
# ----------------------------|--------------------|---------------------------------------------------------------
# 1. Shopping Cart Management   | Hash Table         | A hash table allows for efficient storage and retrieval of items in the shopping cart using product IDs as keys, enabling quick updates and lookups.
# 2. Order Processing System    | Queue              | A queue is suitable for managing order processing as it follows a first-come, first-served order, ensuring that orders are processed in the sequence they were received.
# 3. Top-Selling Products Tracker | Binary Search Tree | A binary search tree can efficiently manage and sort products based on their sales, allowing for quick retrieval of top-selling products.
# 4. Product Search Engine      | Graph              | A graph is ideal for modeling product relationships and categories, enabling efficient search and recommendation based on connections between products.
# 5. Delivery Route Planning     | Graph              | A graph can represent delivery routes and locations, allowing for efficient route planning and optimization based on the connections between different delivery points.
# Implementing the Order Processing System using a Queue data structure.
class OrderProcessingSystem:
    """A class to manage order processing using a queue data structure.
    The queue follows the First In First Out (FIFO) principle, ensuring that orders are processed in the order they were received.
    """
    def __init__(self):
        """Initialize an empty order queue."""
        self.orders = []

    def place_order(self, order):
        """Add a new order to the end of the queue.
        Parameters:
        order: A string representing the customer's order.
        """
        self.orders.append(order)

    def process_order(self):
        """Remove and return the order at the front of the queue.
        Returns:
        The order at the front of the queue.
        Raises:
        IndexError: If there are no orders to process.
        """
        if self.is_empty():
            raise IndexError("No orders to process")
        return self.orders.pop(0)

    def peek_next_order(self):
        """Return the next order to be processed without removing it from the queue.
        Returns:
        The next order in the queue.
        Raises:
        IndexError: If there are no orders to peek at.
        """
        if self.is_empty():
            raise IndexError("No orders to peek at")
        return self.orders[0]

    def is_empty(self):
        """Check if there are any orders in the queue.
        Returns:
        True if there are no orders, False otherwise.
        """
        return len(self.orders) == 0
# Example usage of the OrderProcessingSystem class
if __name__ == "__main__":
    order_system = OrderProcessingSystem()
    order_system.place_order("Order 1: Laptop")
    order_system.place_order("Order 2: Smartphone")
    order_system.place_order("Order 3: Headphones")

    print("Next order to process:", order_system.peek_next_order())
    print("Processing:", order_system.process_order())
    print("Next order to process:", order_system.peek_next_order())