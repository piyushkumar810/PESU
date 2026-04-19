# Prim's Algorithm using Adjacency Matrix

# Number of vertices in graph
V = 5

# Graph represented as adjacency matrix
# 0 means no edge
graph = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]

# This function finds the vertex with minimum key value
# which is not yet included in MST
def min_key(key, mst_set):
    min_value = float('inf')   # Initialize minimum value as infinity
    min_index = -1             # To store index of minimum value

    # Loop through all vertices
    for v in range(V):
        # Check two conditions:
        # 1. vertex is not yet included in MST
        # 2. key value is smaller than current minimum
        if mst_set[v] == False and key[v] < min_value:
            min_value = key[v]
            min_index = v

    return min_index


# Function to print the constructed MST
def print_mst(parent):
    print("Edge \tWeight")
    for i in range(1, V):
        # parent[i] --> i shows the edge
        print(parent[i], "-", i, "\t", graph[i][parent[i]])


# Main function to implement Prim's Algorithm
def prim_mst():
    # Key values used to pick minimum weight edge
    key = [float('inf')] * V   # Initialize all keys as infinite

    # To store constructed MST
    parent = [None] * V        # parent[i] will store parent of i

    # To represent set of vertices included in MST
    mst_set = [False] * V

    # Start from first vertex (index 0)
    key[0] = 0        # Make key 0 so that this vertex is picked first
    parent[0] = -1    # First node is always root of MST

    # MST will have V vertices
    for _ in range(V):

        # Step 1: Pick the minimum key vertex not yet included in MST
        u = min_key(key, mst_set)

        # Step 2: Include this vertex in MST
        mst_set[u] = True

        # Step 3: Update key and parent for adjacent vertices
        for v in range(V):

            # Conditions:
            # 1. There is an edge from u to v (graph[u][v] != 0)
            # 2. v is not yet included in MST
            # 3. weight of edge u-v is smaller than current key[v]
            if graph[u][v] != 0 and mst_set[v] == False and graph[u][v] < key[v]:
                
                key[v] = graph[u][v]   # Update key value
                parent[v] = u          # Set parent

    # Print the result
    print_mst(parent)


# Call the function
prim_mst()