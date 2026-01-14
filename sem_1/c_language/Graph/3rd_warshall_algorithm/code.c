#include <stdio.h>

#define MAX 10   // Maximum number of vertices

// Function to implement Warshall's Algorithm
void warshall(int A[MAX][MAX], int n)
{
    int R[MAX][MAX];
    int i, j, k;

    // STEP 1: Initialize R = A (copy adjacency matrix)
    for (i = 0; i < n; i++)
    {
        for (j = 0; j < n; j++)
        {
            R[i][j] = A[i][j];
        }
    }

    // STEP 2: Allow each vertex as intermediate
    for (k = 0; k < n; k++)
    {
        for (i = 0; i < n; i++)
        {
            for (j = 0; j < n; j++)
            {
                R[i][j] = R[i][j] || (R[i][k] && R[k][j]);
            }
        }
    }

    // STEP 3: Print Transitive Closure
    printf("\nTransitive Closure Matrix:\n");
    for (i = 0; i < n; i++)
    {
        for (j = 0; j < n; j++)
        {
            printf("%d ", R[i][j]);
        }
        printf("\n");
    }
}

int main()
{
    int A[MAX][MAX], n, i, j;

    printf("Enter number of vertices: ");
    scanf("%d", &n);

    printf("Enter adjacency matrix:\n");
    for (i = 0; i < n; i++)
    {
        for (j = 0; j < n; j++)
        {
            scanf("%d", &A[i][j]);
        }
    }

    warshall(A, n);

    return 0;
}
