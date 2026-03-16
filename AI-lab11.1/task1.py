# Generate a Python class implementation for a Stack data structure.
# Include the following methods: push(), pop(), peek(), and is_empty().
# Use a Python list internally to store stack elements.
# Add proper docstrings and comments explaining each method.
# Also include a simple example demonstrating stack operations.
class Stack:
    """
    A Stack data structure implementation using a Python list.
    The stack follows the Last In First Out (LIFO) principle.
    """

    def __init__(self):
        """Initialize an empty stack."""
        self.stack = []

    def push(self, item):
        """
        Add an item to the top of the stack.

        Parameters:
        item: The element to be added to the stack.
        """
        self.stack.append(item)

    def pop(self):
        """
        Remove and return the item at the top of the stack.

        Returns:
        The item at the top of the stack.

        Raises:
        IndexError: If the stack is empty when trying to pop an item.
        """
        if self.is_empty():
            raise IndexError("Pop from an empty stack")
        return self.stack.pop()

    def peek(self):
        """
        Return the item at the top of the stack without removing it.

        Returns:
        The item at the top of the stack.

        Raises:
        IndexError: If the stack is empty when trying to peek an item.
        """
        if self.is_empty():
            raise IndexError("Peek from an empty stack")
        return self.stack[-1]

    def is_empty(self):
        """
        Check if the stack is empty.

        Returns:
        True if the stack is empty, False otherwise.
        """
        return len(self.stack) == 0
# Example usage of the Stack class
if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)

    print("Top item (peek):", stack.peek())  # Output: 3
    print("Stack is empty:", stack.is_empty())  # Output: False

    print("Popped item:", stack.pop())  # Output: 3
    print("Top item after pop (peek):", stack.peek())  # Output: 2

    stack.pop()
    stack.pop()
    print("Stack is empty after popping all items:", stack.is_empty())  # Output: True
    