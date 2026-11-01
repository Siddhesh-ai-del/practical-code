class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if not self.root:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node, key):
        if key < node.value:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert(node.left, key)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert(node.right, key)

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None or node.value == key:
            return node
        elif key < node.value:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)

    def inorder(self):
        self._inorder(self.root)

    def _inorder(self, node):
        if node:
            self._inorder(node.left)
            print(node.value, end=" ")
            self._inorder(node.right)


def main():
    bst = BinarySearchTree()

    while True:
        print("\nMenu:")
        print("1. Insert key")
        print("2. Search key")
        print("3. Display tree (In-order traversal)")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            key = int(input("Enter key to insert: "))
            bst.insert(key)
        elif choice == "2":
            key = int(input("Enter key to search: "))
            result = bst.search(key)
            if result:
                print(f"Found {key} in the tree.")
            else:
                print(f"{key} not found in the tree.")
        elif choice == "3":
            print("Tree in-order traversal:")
            bst.inorder()
            print()
        elif choice == "4":
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
