# Create a Python class implementing a Priority Queue using the heapq module.
# Include methods enqueue(item, priority), dequeue(), and display().
# Ensure that elements with higher priority are removed first.
# Add clear docstrings and comments explaining the implementation.
# Include an example demonstrating priority queue operations.
import heapq
class PriorityQueue:
    """
    A Priority Queue implementation using the heapq module.
    Elements with higher priority are removed first.
    """

    def __init__(self):
        """Initialize an empty priority queue."""
        self.elements = []

    def enqueue(self, item, priority):
        """
        Add an item to the priority queue with a given priority.

        Parameters:
        item: The element to be added to the queue.
        priority: The priority of the element (lower values indicate higher priority).
        """
        heapq.heappush(self.elements, (priority, item))

    def dequeue(self):
        """
        Remove and return the item with the highest priority from the queue.

        Returns:
        The item with the highest priority.

        Raises:
        IndexError: If the priority queue is empty when trying to dequeue an item.
        """
        if not self.elements:
            raise IndexError("Dequeue from an empty priority queue")
        return heapq.heappop(self.elements)[1]

    def display(self):
        """Display the elements in the priority queue."""
        print("Priority Queue contents:")
        for priority, item in sorted(self.elements):
            print(f"Priority: {priority}, Item: {item}")
# Example usage of the PriorityQueue class
if __name__ == "__main__":
    pq = PriorityQueue()
    pq.enqueue("Task A", priority=2)
    pq.enqueue("Task B", priority=1)
    pq.enqueue("Task C", priority=3)

    print("Before dequeue:")
    pq.display()

    print("\nDequeueing items:")
    while True:
        try:
            item = pq.dequeue()
            print(f"Dequeued: {item}")
        except IndexError:
            print("Priority Queue is empty.")
            break