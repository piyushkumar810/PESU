# Kruskal's Algorithm in Python
# -----------------------------------------
# Goal:
# Find the Minimum Spanning Tree (MST) of a graph
# MST = subset of edges with minimum total weight that connects all vertices without cycles

# Step 1: Define Disjoint Set (Union-Find) data structure
# This helps in detecting cycles efficiently

class DisjointSet:
    def __init__(self, vertices):
        # Initially, each vertex is its own parent (self root)
        self.parent = {v: v for v in vertices}
        # Rank is used to keep tree shallow (optimization)
        self.rank = {v: 0 for v in vertices}

    def find(self, node):
        # Path Compression:
        # Recursively find root and attach node directly to root
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, u, v):
        # Find roots of both nodes
        root_u = self.find(u)
        root_v = self.find(v)

        # If they are already in same set → cycle → do nothing
        if root_u == root_v:
            return False

        # Union by rank:
        # Attach smaller tree under larger tree
        if self.rank[root_u] > self.rank[root_v]:
            self.parent[root_v] = root_u
        elif self.rank[root_u] < self.rank[root_v]:
            self.parent[root_u] = root_v
        else:
            # If ranks equal, choose one and increase rank
            self.parent[root_v] = root_u
            self.rank[root_u] += 1

        return True


# Step 2: Kruskal Algorithm function
def kruskal(vertices, edges):
    # Sort edges based on weight (smallest first)
    edges.sort(key=lambda x: x[2])

    ds = DisjointSet(vertices)

    mst = []           # Stores MST edges
    total_weight = 0   # Stores total cost

    # Iterate through sorted edges
    for u, v, weight in edges:
        # Check if adding this edge forms a cycle
        if ds.union(u, v):   # If no cycle
            mst.append((u, v, weight))
            total_weight += weight

    return mst, total_weight


# Step 3: Example graph
# Graph represented as edge list: (u, v, weight)
vertices = ['A', 'B', 'C', 'D', 'E']

edges = [
    ('A', 'B', 1),
    ('A', 'C', 3),
    ('B', 'C', 1),
    ('B', 'D', 6),
    ('C', 'D', 4),
    ('C', 'E', 2),
    ('D', 'E', 5)
]

# Step 4: Run Kruskal Algorithm
mst, total_cost = kruskal(vertices, edges)

# Step 5: Output result
print("Edges in Minimum Spanning Tree:")
for u, v, w in mst:
    print(f"{u} - {v} : {w}")

print("Total Cost of MST:", total_cost)


# -----------------------------------------
# Time Complexity:
# Sorting edges → O(E log E)
# Union-Find operations → nearly O(1)
# Overall → O(E log E)

# Key Concept:
# Always pick smallest edge that DOES NOT form a cycle