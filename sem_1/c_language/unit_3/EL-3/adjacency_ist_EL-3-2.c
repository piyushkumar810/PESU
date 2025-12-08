#include <stdio.h>
#include <stdlib.h>

struct Node {
    int vertex;
    struct Node* next;
};
struct Node* createNode(int v) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->vertex = v;
    newNode->next = NULL;
    return newNode;
}
int main() {
    int vertices, edges;
    printf("Enter number of vertices: ");
    scanf("%d", &vertices);
    printf("Enter number of edges: ");
    scanf("%d", &edges);
    struct Node* adjList[vertices];
    for (int i = 0; i < vertices; i++) {
        adjList[i] = NULL;
    }
    printf("Enter edges (u v):\n");
    for (int i = 0; i < edges; i++) {
        int u, v;
        scanf("%d %d", &u, &v);
        u--;  
        v--;
        struct Node* newNode = createNode(v + 1);
        newNode->next = adjList[u];
        adjList[u] = newNode;
        newNode = createNode(u + 1);
        newNode->next = adjList[v];
        adjList[v] = newNode;
    }
    printf("\nAdjacency List:\n");
    for (int i = 0; i < vertices; i++) {
        printf("%d -> ", i + 1);
        struct Node* temp = adjList[i];
        while (temp != NULL) {
            printf("%d ", temp->vertex);
            temp = temp->next;
        }
        printf("\n");
    }
    return 0;
}
