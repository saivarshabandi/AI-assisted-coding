# Implement a double-ended queue (Deque) in Python using collections.deque.
# Include methods insert_front(), insert_rear(), remove_front(), and remove_rear().
# Add proper comments and docstrings explaining each operation.
# Provide a small example demonstrating deque usage.
from collections import deque
class Deque:
    """
    A double-ended queue (Deque) implementation using collections.deque.
    A deque allows insertion and removal of elements from both ends.
    """

    def __init__(self):
        """Initialize an empty deque."""
        self.deque = deque()

    def insert_front(self, item):
        """
        Add an item to the front of the deque.

        Parameters:
        item: The element to be added to the front of the deque.
        """
        self.deque.appendleft(item)

    def insert_rear(self, item):
        """
        Add an item to the rear of the deque.

        Parameters:
        item: The element to be added to the rear of the deque.
        """
        self.deque.append(item)

    def remove_front(self):
        """
        Remove and return the item at the front of the deque.

        Returns:
        The item at the front of the deque.

        Raises:
        IndexError: If the deque is empty when trying to remove an item from the front.
        """
        if self.is_empty():
            raise IndexError("Remove from an empty deque")
        return self.deque.popleft()

    def remove_rear(self):
        """
        Remove and return the item at the rear of the deque.

        Returns:
        The item at the rear of the deque.

        Raises:
        IndexError: If the deque is empty when trying to remove an item from the rear.
        """
        if self.is_empty():
            raise IndexError("Remove from an empty deque")
        return self.deque.pop()

    def is_empty(self):
        """
        Check if the deque is empty.

        Returns:
        True if the deque is empty, False otherwise.
        """
        return len(self.deque) == 0
# Example usage of the Deque class
if __name__ == "__main__":
    my_deque = Deque()
    my_deque.insert_rear("Task 1")
    my_deque.insert_rear("Task 2")
    my_deque.insert_front("Task 0")

    print("Deque after insertions:")
    print(my_deque.deque)  # Output: deque(['Task 0', 'Task 1', 'Task 2'])

    print("\nRemoving from front:", my_deque.remove_front())  # Output: Task 0
    print("Removing from rear:", my_deque.remove_rear())    # Output: Task 2

    print("\nDeque after removals:")
    print(my_deque.deque)  # Output: deque(['Task 1'])