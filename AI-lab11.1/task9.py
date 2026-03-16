# Analyze the following campus management features and suggest the most suitable data structure for each:
# 1. Student Attendance Tracking
# 2. Event Registration System
# 3. Library Book Borrowing
# 4. Bus Scheduling System
# 5. Cafeteria Order Queue

# Choose from: Stack, Queue, Priority Queue, Linked List, Binary Search Tree, Graph, Hash Table, Deque.

# Provide a table mapping:
# Feature → Data Structure → Justification (2–3 sentences).

# Then implement one selected feature as a Python program with comments and docstrings.
# Feature → Data Structure → Justification
# 1. Student Attendance Tracking → Hash Table → A hash table allows for efficient storage and retrieval of student attendance records using student IDs as keys, enabling quick updates and lookups.
# 2. Event Registration System → Queue → A queue is suitable for managing event registrations as
#    it follows a first-come, first-served order, ensuring that registrations are processed in the sequence they were received.
# 3. Library Book Borrowing → Linked List → A linked list can efficiently manage the borrowing and returning of books, allowing for dynamic addition and removal of book records without needing to shift elements as in an array.
# 4. Bus Scheduling System → Graph → A graph is ideal for modeling bus routes and
#    schedules, as it can represent the connections between different bus stops and routes, allowing for efficient route planning and scheduling.
# 5. Cafeteria Order Queue → Queue → A queue is perfect for managing cafeteria orders as it ensures that orders are processed in the order they were placed, providing a fair and organized system for handling customer requests.
# Implementing the Cafeteria Order Queue using a Queue data structure.
class CafeteriaOrderQueue:
    """A class to manage cafeteria orders using a queue data structure.
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
        True if the queue is empty, False otherwise.
        """
        return len(self.orders) == 0
# Example usage of the CafeteriaOrderQueue class
if __name__ == "__main__":
    order_queue = CafeteriaOrderQueue()
    order_queue.place_order("Burger and Fries")
    order_queue.place_order("Pizza")
    order_queue.place_order("Salad")

    print("Next order to process:", order_queue.peek_next_order())
    print("Processing order:", order_queue.process_order())
    print("Next order to process:", order_queue.peek_next_order())