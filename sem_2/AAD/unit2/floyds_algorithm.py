# ==============================
# FLOYD-WARSHALL ALGORITHM
# ==============================

# We use a very large value to represent "infinity"
# This means there is NO direct edge between two vertices
INF = float('inf')

def floyd_warshall(graph):
    """
    graph: adjacency matrix (2D list)
           graph[i][j] represents distance from vertex i to j
    """

    # Step 1: Number of vertices
    V = len(graph)

    # Step 2: Create a distance matrix
    # We copy the graph so that original graph remains unchanged
    dist = []

    for i in range(V):
        row = []
        for j in range(V):
            row.append(graph[i][j])
        dist.append(row)

    # IMPORTANT:
    # dist[i][j] initially stores direct distances

    # ==============================
    # Step 3: Main Logic (Triple Loop)
    # ==============================

    # k → intermediate vertex
    for k in range(V):
        # i → source vertex
        for i in range(V):
            # j → destination vertex
            for j in range(V):

                # Check:
                # Is going through k shorter?
                # i → k → j

                # Avoid overflow / invalid paths:
                if dist[i][k] != INF and dist[k][j] != INF:
                    
                    # Relaxation step
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]

    # ==============================
    # Step 4: Detect Negative Cycle
    # ==============================

    # If distance from a vertex to itself becomes negative
    # then a negative cycle exists
    for i in range(V):
        if dist[i][i] < 0:
            print("Graph contains NEGATIVE cycle!")
            return

    # ==============================
    # Step 5: Print Result
    # ==============================

    print("Shortest distance matrix:")

    for i in range(V):
        for j in range(V):
            if dist[i][j] == INF:
                print("INF", end=" ")
            else:
                print(dist[i][j], end=" ")
        print()

# ==============================
# DRIVER CODE (Example Graph)
# ==============================

# Example graph (Adjacency Matrix)
# 4 vertices: 0, 1, 2, 3

graph = [
    [0,   5,  INF, 10],
    [INF, 0,   3, INF],
    [INF, INF, 0,   1],
    [INF, INF, INF, 0]
]

# Call the function
floyd_warshall(graph)