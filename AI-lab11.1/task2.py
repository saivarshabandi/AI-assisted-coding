# Create a Python class for a Queue using a Python list.
# The queue should follow the FIFO principle.
# Implement the methods enqueue(), dequeue(), peek(), and size().
# Include proper comments and docstrings.
# Also provide a small example showing how the queue works.
class Queue:
    """
    A Queue data structure implementation using a Python list.
    The queue follows the First In First Out (FIFO) principle.
    """

    def __init__(self):
        """Initialize an empty queue."""
        self.queue = []

    def enqueue(self, item):
        """
        Add an item to the end of the queue.

        Parameters:
        item: The element to be added to the queue.
        """
        self.queue.append(item)

    def dequeue(self):
        """
        Remove and return the item at the front of the queue.

        Returns:
        The item at the front of the queue.

        Raises:
        IndexError: If the queue is empty when trying to dequeue an item.
        """
        if self.is_empty():
            raise IndexError("Dequeue from an empty queue")
        return self.queue.pop(0)

    def peek(self):
        """
        Return the item at the front of the queue without removing it.

        Returns:
        The item at the front of the queue.

        Raises:
        IndexError: If the queue is empty when trying to peek an item.
        """
        if self.is_empty():
            raise IndexError("Peek from an empty queue")
        return self.queue[0]

    def size(self):
        """
        Return the number of items in the queue.

        Returns:
        The size of the queue as an integer.
        """
        return len(self.queue)

    def is_empty(self):
        """
        Check if the queue is empty.

        Returns:
        True if the queue is empty, False otherwise.
        """
        return len(self.queue) == 0

# Example usage of the Queue class
if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    print("Front item (peek):", queue.peek())  # Output: 1
    print("Queue size:", queue.size())  # Output: 3
    print("Queue is empty:", queue.is_empty())  # Output: False

    print("Dequeued item:", queue.dequeue())  # Output: 1
    print("Front item after dequeue (peek):", queue.peek())  # Output: 2

    queue.dequeue()
    queue.dequeue()
    print("Queue is empty after dequeuing all items:", queue.is_empty())  # Output: True