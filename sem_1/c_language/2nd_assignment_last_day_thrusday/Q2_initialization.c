#include <stdio.h>
#include <stdlib.h>

// Define the node structure
typedef struct node {
    int data;
    struct node* link;
} *NODE;

// Function to initialize a linked list
NODE initialize_list() {
    // Initially, the list is empty, so head = NULL
    return NULL;
}

int main() {
    NODE head;

    // Initialize the list
    head = initialize_list();

    if (head == NULL)
        printf("Linked list initialized. It is currently empty.\n");
    else
        printf("Linked list not empty.\n");

    return 0;
}
