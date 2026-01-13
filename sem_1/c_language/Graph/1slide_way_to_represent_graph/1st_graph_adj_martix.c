#include <stdio.h>
#include <stdlib.h>

/*
   Graph structure definition
   --------------------------
   numVertices : stores number of vertices in the graph
   adjMatrix   : pointer to 2D array (adjacency matrix)
*/
struct Graph {
    int numVertices;
    int **adjMatrix;
};

/*
   Function: createGraph
   ---------------------
   Creates a graph with given number of vertices
   Allocates memory for adjacency matrix
   Initializes all matrix values to 0
*/
struct Graph* createGraph(int vertices) {
    int i, j;

    // Allocate memory for Graph structure
    struct Graph* graph = (struct Graph*)malloc(sizeof(struct Graph));

    // Store number of vertices
    graph->numVertices = vertices;

    // Allocate memory for rows of adjacency matrix
    graph->adjMatrix = (int**)malloc(vertices * sizeof(int*));

    // Allocate memory for each row and initialize to 0
    for (i = 0; i < vertices; i++) {
        graph->adjMatrix[i] = (int*)malloc(vertices * sizeof(int));

        for (j = 0; j < vertices; j++) {
            // Initially no edges, so set all values to 0
            graph->adjMatrix[i][j] = 0;
        }
    }

    // Return created graph
    return graph;
}

/*
   Function: addEdge
   -----------------
   Adds an edge between src and dest
   For undirected graph:
   adjMatrix[src][dest] = 1
   adjMatrix[dest][src] = 1
*/
void addEdge(struct Graph* graph, int src, int dest) {

    // Add edge from src to dest
    graph->adjMatrix[src][dest] = 1;

    // Add edge from dest to src (undirected graph)
    graph->adjMatrix[dest][src] = 1;
}

/*
   Function: printGraph
   --------------------
   Prints adjacency matrix of the graph
*/
void printGraph(struct Graph* graph) {
    int i, j;

    printf("\nAdjacency Matrix:\n");

    // Traverse rows
    for (i = 0; i < graph->numVertices; i++) {

        // Traverse columns
        for (j = 0; j < graph->numVertices; j++) {
            printf("%d ", graph->adjMatrix[i][j]);
        }

        // Move to next row
        printf("\n");
    }
}

/*
   Function: freeGraph
   -------------------
   Frees all dynamically allocated memory
*/
void freeGraph(struct Graph* graph) {
    int i;

    // Free each row of adjacency matrix
    for (i = 0; i < graph->numVertices; i++) {
        free(graph->adjMatrix[i]);
    }

    // Free adjacency matrix pointer
    free(graph->adjMatrix);

    // Free graph structure
    free(graph);
}

/*
   Main Function
   -------------
   Demonstrates Graph ADT operations
*/
int main() {

    // Create a graph with 4 vertices
    struct Graph* graph = createGraph(4);

    // Add edges
    addEdge(graph, 0, 1);
    addEdge(graph, 0, 2);
    addEdge(graph, 1, 2);
    addEdge(graph, 2, 3);

    // Print adjacency matrix
    printGraph(graph);

    // Free allocated memory
    freeGraph(graph);

    return 0;
}
