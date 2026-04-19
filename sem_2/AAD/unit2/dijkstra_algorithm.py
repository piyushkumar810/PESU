# Dijkstra's Algorithm using Adjacency Matrix

# Number of vertices
V = 5

# Graph representation (adjacency matrix)
# 0 means no edge
graph = [
    [0, 10, 0, 5, 0],
    [0, 0, 1, 2, 0],
    [0, 0, 0, 0, 4],
    [0, 3, 9, 0, 2],
    [7, 0, 6, 0, 0]
]


# Function to find vertex with minimum distance
def min_distance(dist, visited):
    min_value = float('inf')
    min_index = -1

    for v in range(V):
        # Choose the smallest distance vertex not yet visited
        if visited[v] == False and dist[v] < min_value:
            min_value = dist[v]
            min_index = v

    return min_index


def dijkstra(src):
    # Step 1: Initialize distances
    dist = [float('inf')] * V   # All distances = infinity
    dist[src] = 0               # Distance to source = 0

    # Track visited nodes
    visited = [False] * V

    # Run loop V times
    for _ in range(V):

        # Step 2: Pick minimum distance vertex
        u = min_distance(dist, visited)

        # Mark it as visited
        visited[u] = True

        # Step 3: Update distances of adjacent vertices
        for v in range(V):

            # Conditions:
            # 1. There is an edge (graph[u][v] != 0)
            # 2. v is not visited
            # 3. New distance is smaller
            if graph[u][v] != 0 and visited[v] == False:
                
                # Relaxation step
                if dist[u] + graph[u][v] < dist[v]:
                    dist[v] = dist[u] + graph[u][v]

    # Print result
    print("Vertex \t Distance from Source")
    for i in range(V):
        print(i, "\t", dist[i])


# Call function (source = 0)
dijkstra(0)