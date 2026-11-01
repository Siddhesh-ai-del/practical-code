from collections import deque


class PizzaDelivery:
    def __init__(self):
        self.graph = {}

    def add_location(self, location):
        if location not in self.graph:
            self.graph[location] = []

    def add_road(self, location1, location2):
        self.graph[location1].append(location2)
        self.graph[location2].append(location1)

    def dfs(self, start):
        visited = set()
        stack = [start]

        print("DFS Traversal:")

        while stack:
            location = stack.pop()

            if location not in visited:
                print(location, end=" ")
                visited.add(location)

                for neighbor in reversed(self.graph[location]):
                    if neighbor not in visited:
                        stack.append(neighbor)

    def bfs(self, start):
        visited = set()
        queue = deque([start])
        visited.add(start)

        print("\nBFS Traversal:")

        while queue:
            location = queue.popleft()
            print(location, end=" ")

            for neighbor in self.graph[location]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)


pizza = PizzaDelivery()

pizza.add_location("Shop")
pizza.add_location("A")
pizza.add_location("B")
pizza.add_location("C")
pizza.add_location("D")

pizza.add_road("Shop", "A")
pizza.add_road("Shop", "B")
pizza.add_road("A", "C")
pizza.add_road("B", "D")

pizza.dfs("Shop")
pizza.bfs("Shop")
