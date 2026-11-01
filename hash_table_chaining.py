# Program: Hash Function (Separate Chaining)


class HashTable:
    def __init__(self):
        self.size = 10
        self.table = [[] for _ in range(self.size)]

    # Division Method
    def hash_function(self, key):
        return key % self.size

    # Insert key-value pair
    def insert(self, key, value):
        index = self.hash_function(key)

        # Update value if key already exists
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return

        # Insert new key-value pair
        self.table[index].append([key, value])

    # Search value using key
    def search(self, key):
        index = self.hash_function(key)

        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None

    # Delete key-value pair
    def delete(self, key):
        index = self.hash_function(key)

        for pair in self.table[index]:
            if pair[0] == key:
                self.table[index].remove(pair)
                return True

        return False

    # Display hash table
    def display(self):
        for i in range(self.size):
            print(i, ":", self.table[i])


# Create Hash Table
ht = HashTable()

# Insert
ht.insert(10, "A")
ht.insert(20, "B")
ht.insert(25, "C")
ht.insert(15, "D")
ht.insert(35, "E")

# Display
print("Hash Table:")
ht.display()

# Search
print("\nSearch 25:", ht.search(25))

# Delete
print("Delete 25:", ht.delete(25))

# Display after deletion
print("\nHash Table after deletion:")
ht.display()
