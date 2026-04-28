# Bellman-Ford Algorithm in Python

class Graph:
    def __init__(self, vertices):
        self.V = vertices          # Number of vertices
        self.edges = []            # List to store edges

    # Function to add an edge
    def add_edge(self, u, v, w):
        self.edges.append((u, v, w))  # (source, destination, weight)

    # Bellman-Ford Algorithm
    def bellman_ford(self, src):
        # Step 1: Initialize distances
        dist = [float('inf')] * self.V
        dist[src] = 0   # Distance to source is 0

        # Step 2: Relax all edges V-1 times
        for i in range(self.V - 1):
            print(f"\nIteration {i+1}")
            for u, v, w in self.edges:
                # Relaxation condition
                if dist[u] != float('inf') and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    print(f"Updated dist[{v}] to {dist[v]} using edge ({u}->{v})")

        # Step 3: Check for negative weight cycle
        for u, v, w in self.edges:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                print("\nGraph contains negative weight cycle!")
                return

        # Step 4: Print shortest distances
        print("\nFinal shortest distances from source:")
        for i in range(self.V):
            print(f"Vertex {i} -> Distance {dist[i]}")


# 🔹 Example Usage

g = Graph(5)

g.add_edge(0, 1, -1)
g.add_edge(0, 2, 4)
g.add_edge(1, 2, 3)
g.add_edge(1, 3, 2)
g.add_edge(1, 4, 2)
g.add_edge(3, 2, 5)
g.add_edge(3, 1, 1)
g.add_edge(4, 3, -3)

g.bellman_ford(0)


'''
🔍 Step-by-Step Understanding
Step 1: Initialization
dist = [∞, ∞, ∞, ∞, ∞]
dist[source] = 0
Step 2: Relaxation

For every edge (u → v, weight w):

if dist[u] + w < dist[v]:
    dist[v] = dist[u] + w

👉 This is the heart of the algorithm

Step 3: Repeat V-1 times

Because:

First iteration → shortest path with 1 edge
Second → with 2 edges
...
V-1 → all possible paths
Step 4: Negative Cycle Check

If still improving:

dist[u] + w < dist[v]

👉 means infinite loop possible → negative cycle

🧠 Key Points (GATE Important)
Time Complexity: O(V × E)
Works with negative weights
Fails if negative cycle exists
Slower than Dijkstra but more powerful
'''