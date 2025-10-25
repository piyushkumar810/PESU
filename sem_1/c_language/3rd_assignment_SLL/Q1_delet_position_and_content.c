/*
Write a C Program to do the following 

Construct a Basic Node: Define a structure in C that represents a single node in a linked list containing an integer data and a pointer to the next node.
■ Hint: Use struct in C to define your node. The node typically contains data of type int and a pointer to the next struct.
Initialization Function: Write a function that initializes a linked list and returns a pointer to the head node.
■ Hint: This function should return a NULL pointer to signify that the list is empty at the beginning.
Delete at Position: Write a function to delete a node at a specific position.
■ Hint: Traverse to the specific position and adjust pointers.
Delete by Content: Implement a function to delete a node based on content.
■ Hint: Find the node with matching content and remove it by updating pointers.

The Function Prototypes are
NODE Create_Node(int Data);
NODE Delete_Pos(NODE Header, int Data, int pos);
NODE  Delete_Content(NODE Header, int Data);

typedef struct mynode {
      int data; 
      structure dynode *link;
} *NODE;

*/

#include <stdio.h>
#include <stdlib.h>

// Define the node structure
typedef struct mynode {
    int data;
    struct mynode *link;
} *NODE;

// Function to initialize an empty list
NODE Initialize_List() {
    return NULL; // Empty list at the beginning
}

// Function to create a new node
NODE Create_Node(int Data) {
    NODE temp = (NODE)malloc(sizeof(struct mynode));
    if (temp == NULL) {
        printf("\nMemory allocation failed.\n");
        exit(1);
    }
    temp->data = Data;
    temp->link = NULL;
    return temp;
}

// Function to delete a node at a specific position
NODE Delete_Pos(NODE Header, int pos) {
    if (Header == NULL) {
        printf("\nList is empty.\n");
        return Header;
    }

    NODE temp = Header;

    if (pos == 1) { // Delete first node
        Header = Header->link;
        printf("\nDeleted node at position %d with data %d", pos, temp->data);
        free(temp);
        return Header;
    }

    NODE prev = NULL;
    int count = 1;

    // Traverse to the position
    while (temp != NULL && count < pos) {
        prev = temp;
        temp = temp->link;
        count++;
    }

    if (temp == NULL) {
        printf("\nPosition %d not found.", pos);
        return Header;
    }

    prev->link = temp->link;
    printf("\nDeleted node at position %d with data %d", pos, temp->data);
    free(temp);
    return Header;
}

// Function to delete a node by its content
NODE Delete_Content(NODE Header, int Data) {
    if (Header == NULL) {
        printf("\nList is empty.\n");
        return Header;
    }

    NODE temp = Header, prev = NULL;

    // If first node contains the data
    if (temp != NULL && temp->data == Data) {
        Header = temp->link;
        printf("\nDeleted node with data %d", Data);
        free(temp);
        return Header;
    }

    // Search for the data
    while (temp != NULL && temp->data != Data) {
        prev = temp;
        temp = temp->link;
    }

    if (temp == NULL) {
        printf("\nData %d not found in list.", Data);
        return Header;
    }

    prev->link = temp->link;
    printf("\nDeleted node with data %d", Data);
    free(temp);
    return Header;
}

// Function to display the linked list
void Display(NODE Header) {
    if (Header == NULL) {
        printf("\nList is empty.\n");
        return;
    }

    NODE temp = Header;
    printf("\nLinked List: ");
    while (temp != NULL) {
        printf("%d -> ", temp->data);
        temp = temp->link;
    }
    printf("NULL\n");
}

// Main function
int main() {
    NODE head = Initialize_List();

    // Create and link nodes manually for demonstration
    NODE n1 = Create_Node(10);
    NODE n2 = Create_Node(20);
    NODE n3 = Create_Node(30);
    NODE n4 = Create_Node(40);

    head = n1;
    n1->link = n2;
    n2->link = n3;
    n3->link = n4;

    Display(head);

    // Delete by position
    head = Delete_Pos(head, 2);
    Display(head);

    // Delete by content
    head = Delete_Content(head, 30);
    Display(head);

    return 0;
}
