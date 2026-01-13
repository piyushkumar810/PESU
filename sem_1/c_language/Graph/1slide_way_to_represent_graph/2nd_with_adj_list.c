#include <stdio.h>
#include <stdlib.h>

/*
   Node structure
   --------------
   dest : stores the adjacent vertex
   next : pointer to next node in the list
*/
struct Node {
    int dest;
    struct Node* next;
};

/*
   Adjacency List structure
   ------------------------
   head : pointer to first node of the list
*/
struct AdjList {
    struct Node* head;
};

/*
   Graph structure
   ---------------
   numVertices : number of vertices in the graph
   array       : array of adjacency lists
*/
struct Graph {
    int numVertices;
    struct AdjList* array;
};

/*
   Function: createNode
   --------------------
   Creates a new adjacency list node
*/
struct Node* createNode(int dest) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->dest = dest;
    newNode->next = NULL;
    return newNode;
}

/*
   Function: createGraph
   ---------------------
   Creates a graph with given number of vertices
   Initializes all adjacency lists as empty
*/
struct Graph* createGraph(int vertices) {
    int i;

    // Allocate memory for graph
    struct Graph* graph = (struct Graph*)malloc(sizeof(struct Graph));
    graph->numVertices = vertices;

    // Allocate memory for adjacency list array
    graph->array = (struct AdjList*)malloc(vertices * sizeof(struct AdjList));

    // Initialize each adjacency list as empty
    for (i = 0; i < vertices; i++) {
        graph->array[i].head = NULL;
    }

    return graph;
}

/*
   Function: addEdge
   -----------------
   Adds an edge to an undirected graph
   src -> dest
   dest -> src
*/
void addEdge(struct Graph* graph, int src, int dest) {

    // Add edge from src to dest
    struct Node* newNode = createNode(dest);
    newNode->next = graph->array[src].head;
    graph->array[src].head = newNode;

    // Add edge from dest to src (undirected graph)
    newNode = createNode(src);
    newNode->next = graph->array[dest].head;
    graph->array[dest].head = newNode;
}

/*
   Function: printGraph
   --------------------
   Prints adjacency list representation of graph
*/
void printGraph(struct Graph* graph) {
    int v;

    for (v = 0; v < graph->numVertices; v++) {
        struct Node* temp = graph->array[v].head;
        printf("Vertex %d:", v);

        // Traverse adjacency list
        while (temp != NULL) {
            printf(" -> %d", temp->dest);
            temp = temp->next;
        }
        printf("\n");
    }
}

/*
   Function: freeGraph
   -------------------
   Frees all allocated memory
*/
void freeGraph(struct Graph* graph) {
    int v;

    // Free all adjacency list nodes
    for (v = 0; v < graph->numVertices; v++) {
        struct Node* temp = graph->array[v].head;
        while (temp != NULL) {
            struct Node* next = temp->next;
            free(temp);
            temp = next;
        }
    }

    // Free adjacency list array
    free(graph->array);

    // Free graph structure
    free(graph);
}

/*
   Main function
   -------------
   Demonstrates adjacency list graph
*/
int main() {

    // Create graph with 4 vertices
    struct Graph* graph = createGraph(4);

    // Add edges
    addEdge(graph, 0, 1);
    addEdge(graph, 0, 2);
    addEdge(graph, 1, 2);
    addEdge(graph, 2, 3);

    // Print graph
    printGraph(graph);

    // Free memory
    freeGraph(graph);

    return 0;
}
