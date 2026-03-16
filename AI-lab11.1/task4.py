# Generate a Python implementation of a Binary Search Tree (BST).
# Include methods for inserting nodes and performing an in-order traversal.
# Use recursion for the insert and traversal methods.
# Add comments and docstrings explaining how the BST works.
# Provide a small example demonstrating the BST operations.
class TreeNode:
    """A node in the binary search tree."""
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
class BinarySearchTree:
    """A binary search tree (BST) implementation."""
    def __init__(self):
        self.root = None  # The root of the BST
    def insert(self, key):
        """Insert a new node with the given key into the BST."""
        if self.root is None:
            self.root = TreeNode(key)  # If the tree is empty, set root to the new node
        else:
            self._insert_recursive(self.root, key)  # Otherwise, insert recursively
    def _insert_recursive(self, node, key):
        """Helper method to insert a node recursively."""
        if key < node.val:  # If the key is smaller than the current node's value
            if node.left is None:
                node.left = TreeNode(key)  # Insert as left child
            else:
                self._insert_recursive(node.left, key)  # Recur on the left subtree
        else:  # If the key is greater than or equal to the current node's value
            if node.right is None:
                node.right = TreeNode(key)  # Insert as right child
            else:
                self._insert_recursive(node.right, key)  # Recur on the right subtree
    def in_order_traversal(self):
        """Perform an in-order traversal of the BST and return a list of values."""
        return self._in_order_recursive(self.root)
    def _in_order_recursive(self, node):
        """Helper method to perform in-order traversal recursively."""
        res = []
        if node:
            res = self._in_order_recursive(node.left)  # Traverse left subtree
            res.append(node.val)  # Visit current node
            res = res + self._in_order_recursive(node.right)  # Traverse right subtree
        return res
# Example usage
if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.insert(5)
    bst.insert(3)
    bst.insert(7)
    bst.insert(2)
    bst.insert(4)
    bst.insert(6)
    bst.insert(8)
    print("In-order traversal of the BST:", bst.in_order_traversal())  # Output: [2, 3, 4, 5, 6, 7, 8]