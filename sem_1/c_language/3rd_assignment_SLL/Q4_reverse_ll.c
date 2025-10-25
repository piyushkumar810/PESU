/*
Write a C Program to do the following 

Reverse Linked List: Implement a function that reverses the linked list.
■ Hint: You may need to keep track of three pointers as you reassign each node’s next pointer to its previous node.

typedef struct mynode {
      int data; 
      structure dynode *link;
} *NODE;

*/

#include <stdio.h>
#include <stdlib.h>

typedef struct mynode {
    int data;
    struct mynode *link;
} *NODE;

// Function to create a new node
NODE create_node(int data) {
    NODE temp = (NODE)malloc(sizeof(struct mynode));
    if (temp == NULL) {
        printf("Memory allocation failed\n");
        exit(1);
    }
    temp->data = data;
    temp->link = NULL;
    return temp;
}

// Function to insert node at the end
NODE insert_end(NODE head, int data) {
    NODE newnode = create_node(data);
    if (head == NULL)
        return newnode;

    NODE temp = head;
    while (temp->link != NULL)
        temp = temp->link;

    temp->link = newnode;
    return head;
}

// Function to reverse the linked list
NODE reverse_list(NODE head) {
    NODE prev = NULL, current = head, next = NULL;

    while (current != NULL) {
        next = current->link;   // Store next node
        current->link = prev;   // Reverse the link
        prev = current;         // Move prev forward
        current = next;         // Move current forward
    }
    head = prev; // Update head
    return head;
}

// Function to display the list
void display(NODE head) {
    NODE temp = head;
    printf("HEAD -> ");
    while (temp != NULL) {
        printf("%d -> ", temp->data);
        temp = temp->link;
    }
    printf("NULL\n");
}

// Main function
int main() {
    NODE head = NULL;

    head = insert_end(head, 10);
    head = insert_end(head, 20);
    head = insert_end(head, 30);
    head = insert_end(head, 40);

    printf("Original Linked List:\n");
    display(head);

    head = reverse_list(head);
    printf("\nReversed Linked List:\n");
    display(head);

    return 0;
}
