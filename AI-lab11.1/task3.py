# Write Python code to implement a Singly Linked List.
# Create a Node class and a LinkedList class.
# Include methods to insert elements and display the list.
# Add clear docstrings and comments explaining each method.
# Provide an example showing insertion and display operations.
class Node:
    """A Node in a singly linked list."""
    def __init__(self, data):
        self.data = data  # The data stored in the node
        self.next = None  # Pointer to the next node
class LinkedList:
    """A singly linked list."""
    def __init__(self):
        self.head = None  # The head of the linked list
    def insert(self, data):
        """Insert a new node with the given data at the end of the list."""
        new_node = Node(data)  # Create a new node
        if self.head is None:
            self.head = new_node  # If the list is empty, set head to the new node
            return
        last_node = self.head
        while last_node.next:  # Traverse to the end of the list
            last_node = last_node.next
        last_node.next = new_node  # Link the last node to the new node
    def display(self):
        """Display the elements in the linked list."""
        current_node = self.head
        while current_node:
            print(current_node.data, end=' -> ')  # Print current node's data
            current_node = current_node.next  # Move to the next node
        print('None')  # Indicate the end of the list
# Example usage
if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.insert(10)
    linked_list.insert(20)
    linked_list.insert(30)
    print("Linked List contents:")
    linked_list.display()  # Output: 10 -> 20 -> 30 -> None