import heapq  # heapq is used to implement a priority queue (min-heap)

def a_star(graph, start, goal, heuristic):
    """
    A* Algorithm to find the shortest path from start to goal.

    graph: adjacency list where
           graph[node] = list of (neighbor, cost)
    start: starting node
    goal: destination node
    heuristic: dictionary with estimated distance to goal for each node
    """

    # OPEN LIST (priority queue)
    # Stores nodes to be explored, ordered by lowest f(n)
    # Each element: (f(n), node)
    open_list = [(0, start)]

    # g_cost stores the actual cost from start node to current node
    # Initialize start node cost as 0
    g_cost = {start: 0}

    # parent dictionary is used to reconstruct the final path
    # It stores from where we reached a node
    parent = {start: None}

    # Loop until there are nodes to explore
    while open_list:

        # Pop the node with smallest f(n) value
        # heapq ensures this is always the minimum
        current_f, current = heapq.heappop(open_list)

        # If we reached the goal, reconstruct the path
        if current == goal:
            path = []

            # Backtrack from goal to start using parent dictionary
            while current is not None:
                path.append(current)
                current = parent[current]

            # Reverse path because we built it from goal → start
            return path[::-1]

        # Explore all neighbors of current node
        for neighbor, cost in graph[current]:

            # Calculate new cost to reach neighbor via current node
            new_g = g_cost[current] + cost

            # If neighbor is not visited OR we found a shorter path
            if neighbor not in g_cost or new_g < g_cost[neighbor]:

                # Update the best known cost to reach neighbor
                g_cost[neighbor] = new_g

                # f(n) = g(n) + h(n)
                # g(n) = actual cost from start to neighbor
                # h(n) = estimated cost from neighbor to goal
                f = new_g + heuristic[neighbor]

                # Push neighbor into priority queue
                heapq.heappush(open_list, (f, neighbor))

                # Update parent to reconstruct path later
                parent[neighbor] = current

    # If goal is not reachable, return None
    return None


# ------------------ EXAMPLE ------------------

# Graph represented as adjacency list
# Each node has a list of (neighbor, cost)
graph = {
    'A': [('B', 1), ('C', 3)],   # From A → B (cost 1), A → C (cost 3)
    'B': [('D', 3), ('E', 1)],
    'C': [('F', 5)],
    'D': [],
    'E': [('F', 2)],
    'F': []
}

# Heuristic values (estimated distance to goal node F)
# IMPORTANT: h(goal) must be 0
heuristic = {
    'A': 5,
    'B': 3,
    'C': 4,
    'D': 6,
    'E': 1,
    'F': 0
}

# Run A* algorithm from A to F
path = a_star(graph, 'A', 'F', heuristic)

# Print the shortest path
print("Shortest Path:", path)