# Implement a Hash Table in Python.
# Include methods insert(), search(), and delete().
# Use chaining (linked list or list of lists) for collision handling.
# Add proper comments and docstrings to explain the implementation.
# Also include an example demonstrating insertion, searching, and deletion.
class HashTable:
    """
    A Hash Table implementation using chaining for collision handling.
    The hash table supports insertion, searching, and deletion of key-value pairs.
    """

    def __init__(self, size=10):
        """Initialize the hash table with a specified size."""
        self.size = size
        self.table = [[] for _ in range(size)]  # Create a list of empty lists for chaining

    def _hash(self, key):
        """Generate a hash value for the given key."""
        return hash(key) % self.size

    def insert(self, key, value):
        """
        Insert a key-value pair into the hash table.

        Parameters:
        key: The key to be inserted.
        value: The value associated with the key.
        """
        index = self._hash(key)
        # Check if the key already exists and update it
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)  # Update existing key
                return
        # If the key does not exist, add a new key-value pair
        self.table[index].append((key, value))

    def search(self, key):
        """
        Search for a value associated with the given key.

        Parameters:
        key: The key to be searched.

        Returns:
        The value associated with the key if found, otherwise None.
        """
        index = self._hash(key)
        for k, v in self.table[index]:
            if k == key:
                return v  # Return the value if the key is found
        return None  # Return None if the key is not found

    def delete(self, key):
        """
        Delete a key-value pair from the hash table.

        Parameters:
        key: The key to be deleted.

        Returns:
        True if the deletion was successful, False if the key was not found.
        """
        index = self._hash(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]  # Remove the key-value pair
                return True  # Return True if deletion was successful
        return False  # Return False if the key was not found
# Example usage of the HashTable class
if __name__ == "__main__":
    hash_table = HashTable()
    hash_table.insert("name", "Alice")
    hash_table.insert("age", 30)
    hash_table.insert("city", "New York")

    print("Search for 'name':", hash_table.search("name"))  # Output: Alice
    print("Search for 'age':", hash_table.search("age"))  # Output: 30
    print("Search for 'country':", hash_table.search("country"))  # Output: None

    print("Delete 'age':", hash_table.delete("age"))  # Output: True
    print("Search for 'age' after deletion:", hash_table.search("age"))  # Output: None