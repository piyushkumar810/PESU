#include <stdio.h>
#include <stdlib.h>

typedef struct node {
    int data;
    struct node* link;
} *NODE;

// Function to insert a node at rear (for testing)
NODE insert_rear(NODE head, int value) {
    NODE newnode = (NODE)malloc(sizeof(struct node));
    if (newnode == NULL) {
        printf("Memory allocation failed.\n");
        return head;
    }

    newnode->data = value;
    newnode->link = NULL;

    if (head == NULL)
        head = newnode;
    else {
        NODE temp = head;
        while (temp->link != NULL)
            temp = temp->link;
        temp->link = newnode;
    }
    return head;
}

// LEVEL - 1 : Delete at Front
NODE delete_front(NODE head) {
    if (head == NULL) {
        printf("List is empty. Nothing to delete.\n");
        return NULL;
    }

    NODE temp = head;
    head = head->link;   // Move head to next node
    printf("Deleted element from front: %d\n", temp->data);
    free(temp);

    return head;
}

// LEVEL - 1 : Delete at Rear
NODE delete_rear(NODE head) {
    if (head == NULL) {
        printf("List is empty. Nothing to delete.\n");
        return NULL;
    }

    if (head->link == NULL) {
        // Only one node
        printf("Deleted element from rear: %d\n", head->data);
        free(head);
        return NULL;
    }

    NODE prev = NULL, temp = head;
    while (temp->link != NULL) {
        prev = temp;
        temp = temp->link;
    }

    printf("Deleted element from rear: %d\n", temp->data);
    free(temp);
    prev->link = NULL;

    return head;
}

// LEVEL - 2 : Insert at Position
NODE insert_position(NODE head, int value, int pos) {
    NODE newnode = (NODE)malloc(sizeof(struct node));
    if (newnode == NULL) {
        printf("Memory allocation failed.\n");
        return head;
    }

    newnode->data = value;
    newnode->link = NULL;

    if (pos <= 0) {
        printf("Invalid position.\n");
        free(newnode);
        return head;
    }

    if (pos == 1) {  // insert at front
        newnode->link = head;
        head = newnode;
        return head;
    }

    NODE temp = head;
    int count = 1;

    while (temp != NULL && count < pos - 1) {
        temp = temp->link;
        count++;
    }

    if (temp == NULL) {
        printf("Position out of range.\n");
        free(newnode);
        return head;
    }

    newnode->link = temp->link;
    temp->link = newnode;

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
    NODE head = NULL;

    // Insert few nodes
    head = insert_rear(head, 10);
    head = insert_rear(head, 20);
    head = insert_rear(head, 30);
    head = insert_rear(head, 40);
    display(head);

    // Delete at front
    head = delete_front(head);
    display(head);

    // Delete at rear
    head = delete_rear(head);
    display(head);

    // Insert at position
    head = insert_position(head, 25, 2);
    display(head);

    // Invalid position example
    head = insert_position(head, 50, 10);

    return 0;
}
