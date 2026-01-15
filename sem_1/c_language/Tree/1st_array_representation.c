#include <stdio.h>

#define MAX 100   // Maximum size of tree

// Function to insert an element into the tree (level order)
void insert(int tree[], int *size, int value)
{
    // Insert value at the next available position
    tree[*size] = value;

    // Increase the size of the tree
    (*size)++;
}

// Function to display the tree (level order traversal)
void display(int tree[], int size)
{
    // Check if tree is empty
    if (size == 0)
    {
        printf("Tree is empty!\n");
        return;
    }

    // Print elements in level order
    printf("Binary Tree (Level Order): ");
    for (int i = 0; i < size; i++)
    {
        printf("%d ", tree[i]);
    }
    printf("\n");
}

int main()
{
    int tree[MAX];   // Array to store tree nodes
    int size = 0;    // Current number of nodes in tree
    int choice, value;

    while (1)
    {
        printf("\n--- MENU ---\n");
        printf("1. Insert node\n");
        printf("2. Display tree\n");
        printf("3. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice)
        {
        case 1:
            if (size >= MAX)
            {
                printf("Tree is full!\n");
            }
            else
            {
                printf("Enter value to insert: ");
                scanf("%d", &value);
                insert(tree, &size, value);
            }
            break;

        case 2:
            display(tree, size);
            break;

        case 3:
            return 0;

        default:
            printf("Invalid choice!\n");
        }
    }
}
