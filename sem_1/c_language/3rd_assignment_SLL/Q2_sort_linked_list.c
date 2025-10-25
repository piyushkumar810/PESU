/*
Write a C Program to do the following 

Construct a Basic Node: Define a structure in C that represents a single node in a linked list containing an integer data and a pointer to the next node.
■ Hint: Use struct in C to define your node. The node typically contains data of type int and a pointer to the next struct.
Initialization Function: Write a function that initializes a linked list and returns a pointer to the head node.
■ Hint: This function should return a NULL pointer to signify that the list is empty at the beginning.
Insert in Order: Assuming the linked list stores integers, write a function that inserts a new node in such a way that the linked list remains sorted in increasing order.
■ Hint: Traverse the list to find the appropriate position where the new node’s value fits, then insert the node at this position.
Sort Linked List Using New Header: Implement a function that sorts a linked list of integers by creating a new header node and transferring nodes from the original list to the new list in sorted order.
■ Hint: Traverse the original list, remove the first node, and insert it into the new list at the correct position. Continue this process until the original list is empty.

typedef struct mynode {
      int data; 
      structure dynode *link;
} *NODE;

*/
#include<stdio.h>
#include<stdlib.h>

typedef struct mynode {
    int data;
    struct mynode *link;
} *NODE;

NODE initialize_list() {
    return NULL;
}

NODE create_node(int data) {
    NODE temp = (NODE) malloc(sizeof(struct mynode));
    if (temp == NULL) {
        printf("\nMemory allocation failed\n");
        exit(1);
    }
    temp->data = data;
    temp->link = NULL;
    return temp;
}

NODE insert_in_order(NODE head, int data) {
    NODE newnode = create_node(data);

    // Case 1: empty list or new node goes at the beginning
    if (head == NULL || data < head->data) {
        newnode->link = head;
        head = newnode;
        return head;
    }

    NODE current = head;
    // ✅ Fixed: removed the extra semicolon here
    while (current->link != NULL && current->link->data < data) {
        current = current->link;
    }

    newnode->link = current->link;
    current->link = newnode;

    return head;
}

NODE sort_using_new_head(NODE head) {
    NODE sorted = NULL;
    NODE current;

    while (head != NULL) {
        current = head;
        head = head->link;

        if (sorted == NULL || current->data < sorted->data) {
            current->link = sorted;
            sorted = current;
        } else {
            NODE temp = sorted;
            while (temp->link != NULL && temp->link->data < current->data) {
                temp = temp->link;
            }
            current->link = temp->link;
            temp->link = current;
        }
    }
    return sorted;
}

void display(NODE head) {
    if (head == NULL) {
        printf("\nList is empty.\n");
        return;
    }

    printf("\nHEAD -> ");
    NODE temp = head;
    while (temp != NULL) {
        printf("%d -> ", temp->data);
        temp = temp->link;
    }
    printf("NULL\n");
}

int main() {
    NODE head = initialize_list();

    head = insert_in_order(head, 30);
    head = insert_in_order(head, 10);
    head = insert_in_order(head, 20);
    head = insert_in_order(head, 40);

    printf("\nAfter inserting in order: ");
    display(head);

    head = sort_using_new_head(head);
    printf("\nAfter sorting using new head: ");
    display(head);

    return 0;
}
