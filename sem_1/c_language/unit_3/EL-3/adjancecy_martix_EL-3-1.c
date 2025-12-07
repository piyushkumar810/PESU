#include <stdio.h>

int main() {
    int v, e;
    
    printf("Enter number of vertices: ");
    scanf("%d", &v);
    
    printf("Enter number of edges: ");
    scanf("%d", &e);
    
    int adj[v][v];
    
    // Step 1: Initialize matrix with 0
    for (int i = 0; i < v; i++) {
        for (int j = 0; j < v; j++) {
            adj[i][j] = 0;
        }
    }

    printf("\nprinting 0 matrix \n");
    for(int i=0; i<v; i++){
        for(int j=0; j<v; j++){
            printf("%d",adj[i][j]);
        }
        printf("\n");
    }
    
    // Step 2: Take edges as input
    printf("Enter edges (u v):\n");
    for (int i = 0; i < e; i++) {
        int u, w;
        scanf("%d %d", &u, &w);
        
        // Convert to 0-based index
        u--;
        w--;
        
        adj[u][w] = 1;
        adj[w][u] = 1; // Undirected graph
    }
    
    // Step 3: Print adjacency matrix
    printf("\nAdjacency Matrix:\n");
    for (int i = 0; i < v; i++) {
        for (int j = 0; j < v; j++) {
            printf("%d ", adj[i][j]);
        }
        printf("\n");
    }

    return 0;
}
