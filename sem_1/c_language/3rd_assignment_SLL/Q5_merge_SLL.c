/*
Write a C Program to do the following 

Merge Two Sorted Lists: Write a program that takes two sorted linked lists and merges them to produce a single sorted linked list.
■ Hint: Use a new list to store the merged result, comparing the current nodes of both lists and appending the smaller one.

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

// Function to merge two sorted linked lists
NODE merge_sorted(NODE list1, NODE list2) {
    NODE result = NULL, tail = NULL;

    while (list1 != NULL && list2 != NULL) {
        NODE newnode;
        if (list1->data <= list2->data) {
            newnode = create_node(list1->data);
            list1 = list1->link;
        } else {
            newnode = create_node(list2->data);
            list2 = list2->link;
        }

        if (result == NULL) {
            result = newnode;
            tail = newnode;
        } else {
            tail->link = newnode;
            tail = newnode;
        }
    }

    // Attach remaining nodes
    while (list1 != NULL) {
        tail->link = create_node(list1->data);
        tail = tail->link;
        list1 = list1->link;
    }

    while (list2 != NULL) {
        tail->link = create_node(list2->data);
        tail = tail->link;
        list2 = list2->link;
    }

    return result;
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
    NODE list1 = NULL, list2 = NULL, merged = NULL;

    // First sorted list
    list1 = insert_end(list1, 10);
    list1 = insert_end(list1, 30);
    list1 = insert_end(list1, 50);

    // Second sorted list
    list2 = insert_end(list2, 20);
    list2 = insert_end(list2, 40);
    list2 = insert_end(list2, 60);

    printf("List 1: ");
    display(list1);
    printf("List 2: ");
    display(list2);

    merged = merge_sorted(list1, list2);

    printf("\nMerged Sorted List: ");
    display(merged);

    return 0;
}
