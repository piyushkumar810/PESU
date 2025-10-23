// Insert at Front: Write a function that inserts a new integer node at the front of the
// linked list.
// ■ Hint: The new node should point to the current head of the list, and then the head pointer should be
// updated to the new node.

#include <stdio.h>
#include <stdlib.h>

// Define the node structure
typedef struct node {
    int data;
    struct node* link;
} *NODE;

// Function to initialize a linked list
NODE initialize_list() {
    return NULL;  // Empty list
}

// Function to insert a new node at the front
NODE insert_front(NODE head, int value) {
    // Create a new node
    NODE newnode = (NODE)malloc(sizeof(struct node));
    if (newnode == NULL) {
        printf("Memory allocation failed.\n");
        return head;  // Return existing head if malloc fails
    }

    // Assign value and link
    newnode->data = value;
    newnode->link = head;  // New node points to current head

    // Update head to point to new node
    head = newnode;

    return head;
}

// Function to display the list
void display(NODE head) {
    if (head == NULL) {
        printf("List is empty.\n");
        return;
    }
    printf("Linked List: ");
    NODE temp = head;
    while (temp != NULL) {
        printf("%d -> ", temp->data);
        temp = temp->link;
    }
    printf("NULL\n");
}

int main() {
    NODE head;

    // Step 1: Initialize the list
    head = initialize_list();

    // Step 2: Insert elements at the front
    head = insert_front(head, 10);
    head = insert_front(head, 20);
    head = insert_front(head, 30);

    // Step 3: Display the list
    display(head);

    return 0;
}
