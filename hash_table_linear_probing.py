class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    # Division method hash function
    def hash(self, key):
        return key % self.size

    def insert(self, key):
        index = self.hash(key)
        for i in range(self.size):
            pos = (index + i) % self.size  # linear probing
            if self.table[pos] is None or self.table[pos] == -1:
                self.table[pos] = key
                print(f"Inserted {key} at index {pos}")
                return
            if self.table[pos] == key:
                print(f"Key {key} already exists at index {pos}")
                return
        print("Hash table is full! Cannot insert", key)

    def search(self, key):
        index = self.hash(key)
        for i in range(self.size):
            pos = (index + i) % self.size
            if self.table[pos] is None:
                break  # key cannot be further
            if self.table[pos] == key:
                print(f"Key {key} found at index {pos}")
                return pos
        print(f"Key {key} not found")
        return -1

    def delete(self, key):
        index = self.hash(key)
        for i in range(self.size):
            pos = (index + i) % self.size
            if self.table[pos] is None:
                break
            if self.table[pos] == key:
                self.table[pos] = -1
                print(f"Key {key} deleted from index {pos}")
                return
        print(f"Key {key} not found, cannot delete")

    def display(self):
        print("\nIndex | Value")
        print("------------------")
        for i, v in enumerate(self.table):
            if v is None:
                print(f"{i:5} | ---")
            elif v == -1:
                print(f"{i:5} | (deleted)")
            else:
                print(f"{i:5} | {v}")
        print()


size = int(input("Enter size of hash table: "))
ht = HashTable(size)

while True:
    print("1.Insert 2.Search 3.Delete 4.Display 5.Exit")
    ch = int(input("Enter choice: "))
    if ch == 1:
        ht.insert(int(input("Enter key to insert: ")))
    elif ch == 2:
        ht.search(int(input("Enter key to search: ")))
    elif ch == 3:
        ht.delete(int(input("Enter key to delete: ")))
    elif ch == 4:
        ht.display()
    elif ch == 5:
        print("Exiting...")
        break
    else:
        print("Invalid choice")
