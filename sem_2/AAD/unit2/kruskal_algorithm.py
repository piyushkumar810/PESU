# Kruskal's Algorithm using Union-Find (Disjoint Set)

# Number of vertices
V = 5

# List of edges: (u, v, weight)
edges = [
    (0, 1, 2),
    (0, 3, 6),
    (1, 2, 3),
    (1, 3, 8),
    (1, 4, 5),
    (2, 4, 7),
    (3, 4, 9)
]

# -------------------------------
# DISJOINT SET (UNION-FIND)
# -------------------------------

# Parent array: initially each node is its own parent
parent = list(range(V))

# Rank array: used to keep tree shallow (optimization)
rank = [0] * V


# Find function with Path Compression
def find(u):
    # If u is not its own parent
    if parent[u] != u:
        # Recursively find root and compress path
        parent[u] = find(parent[u])
    return parent[u]


# Union function with Rank Optimization
def union(u, v):
    root_u = find(u)
    root_v = find(v)

    # If both have same root → cycle detected → do nothing
    if root_u == root_v:
        return False

    # Attach smaller tree under bigger tree
    if rank[root_u] < rank[root_v]:
        parent[root_u] = root_v
    elif rank[root_u] > rank[root_v]:
        parent[root_v] = root_u
    else:
        parent[root_v] = root_u
        rank[root_u] += 1

    return True


# -------------------------------
# KRUSKAL'S ALGORITHM
# -------------------------------

def kruskal():
    # Step 1: Sort edges by weight
    edges.sort(key=lambda x: x[2])

    mst = []        # To store MST edges
    total_cost = 0 # Total weight of MST

    # Step 2: Process edges one by one
    for u, v, w in edges:

        # Try to include edge (u, v)
        if union(u, v):  # If no cycle is formed
            mst.append((u, v, w))
            total_cost += w

        # Stop when MST has V-1 edges
        if len(mst) == V - 1:
            break

    # Print result
    print("Edge \tWeight")
    for u, v, w in mst:
        print(f"{u} - {v} \t {w}")

    print("Total Cost:", total_cost)


# Call function
kruskal()