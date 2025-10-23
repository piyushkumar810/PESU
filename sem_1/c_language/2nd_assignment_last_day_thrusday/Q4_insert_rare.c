



#include <stdio.h>
#include <stdlib.h>

typedef struct node {
    int data;
    struct node* link;
} *NODE;

// Function to insert a new node at the rear (end)
NODE insert_rear(NODE head, int value) {
    NODE newnode = (NODE)malloc(sizeof(struct node));
    if (newnode == NULL) {
        printf("Memory allocation failed.\n");
        return head;
    }

    newnode->data = value;
    newnode->link = NULL;  // new node will be last, so link = NULL

    if (head == NULL) {
        // If list is empty, new node becomes head
        head = newnode;
    } else {
        // Traverse to the last node
        NODE temp = head;
        while (temp->link != NULL)
            temp = temp->link;
        temp->link = newnode;  // attach new node at the end
    }

    return head;
}

// Function to display the list
void display(NODE head) {
    if (head == NULL) {
        printf("List is empty.\n");
        return;
    }

    NODE temp = head;
    printf("Linked List: ");
    while (temp != NULL) {
        printf("%d -> ", temp->data);
        temp = temp->link;
    }
    printf("NULL\n");
}

int main() {
    NODE head = NULL;  // Initialize empty list

    head = insert_rear(head, 10);
    head = insert_rear(head, 20);
    head = insert_rear(head, 30);

    display(head);

    return 0;
}
