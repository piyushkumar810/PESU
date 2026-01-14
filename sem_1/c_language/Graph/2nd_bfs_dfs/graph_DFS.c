#include <stdio.h>
#include <stdbool.h>

#define MAX 10   // Maximum number of nodes

/*
   Function: dfs
   -------------
   Performs Depth First Search on a graph represented
   using adjacency matrix.

   Parameters:
   graph      : adjacency matrix
   visited[]  : array to track visited nodes
   node       : current node being visited
   numNodes   : total number of nodes
*/
void dfs(int graph[MAX][MAX], bool visited[], int node, int numNodes)
{
    // Mark the current node as visited
    visited[node] = true;

    // Print the current node
    printf("%d ", node);

    // Check all possible neighbors of the current node
    for (int neighbor = 0; neighbor < numNodes; neighbor++)
    {
        /*
           If there is an edge from 'node' to 'neighbor'
           AND the neighbor has not been visited yet,
           then perform DFS on that neighbor
        */
        if (graph[node][neighbor] == 1 && !visited[neighbor])
        {
            dfs(graph, visited, neighbor, numNodes); // Recursive DFS call
        }
    }
}

int main()
{
    int numNodes;
    int graph[MAX][MAX];
    bool visited[MAX] = {false}; // Initialize all nodes as unvisited

    // Input number of nodes
    printf("Enter number of nodes: ");
    scanf("%d", &numNodes);

    // Input adjacency matrix
    printf("Enter adjacency matrix:\n");
    for (int i = 0; i < numNodes; i++)
    {
        for (int j = 0; j < numNodes; j++)
        {
            scanf("%d", &graph[i][j]);
        }
    }

    int startNode;
    printf("Enter starting node for DFS: ");
    scanf("%d", &startNode);

    // Perform DFS traversal
    printf("DFS Traversal: ");
    dfs(graph, visited, startNode, numNodes);

    return 0;
}
