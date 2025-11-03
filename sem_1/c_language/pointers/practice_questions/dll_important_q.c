// You’ve been hired to build a backend for a ticket counter system where people stand in a queue that 
// operates in a loop. The first and last person are linked, and people can join or leave from both ends.
//  The system should manage the line efficiently using a Circular Doubly Linked List (CDLL) — a structure 
//  that allows you to move in both directions and wrap around the list from end to start. Your job is to: 
//  Build the CDLL-based queue handler Allow insertion and deletion from both ends Display the queue in both 
//  forward and reverse directions Implement one extra feature to enhance the system - (Choose One) : 
//  Count people, Search for ticket, Display Reverse, Insert After/Before ticket dont include comments

#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node *next, *prev;
};

struct Node *head = NULL;

void insertFront(int value) {
    struct Node *newNode = malloc(sizeof(struct Node));
    newNode->data = value;
    if (head == NULL) {
        newNode->next = newNode->prev = newNode;
        head = newNode;
        return;
    }
    struct Node *tail = head->prev;
    newNode->next = head;
    newNode->prev = tail;
    tail->next = newNode;
    head->prev = newNode;
    head = newNode;
}

void insertRear(int value) {
    struct Node *newNode = malloc(sizeof(struct Node));
    newNode->data = value;
    if (head == NULL) {
        newNode->next = newNode->prev = newNode;
        head = newNode;
        return;
    }
    struct Node *tail = head->prev;
    newNode->next = head;
    newNode->prev = tail;
    tail->next = newNode;
    head->prev = newNode;
}

void deleteFront() {
    if (head == NULL) {
        printf("Queue empty\n");
        return;
    }
    if (head->next == head) {
        free(head);
        head = NULL;
        return;
    }
    struct Node *tail = head->prev;
    struct Node *temp = head;
    head = head->next;
    head->prev = tail;
    tail->next = head;
    free(temp);
}

void deleteRear() {
    if (head == NULL) {
        printf("Queue empty\n");
        return;
    }
    struct Node *tail = head->prev;
    if (tail == head) {
        free(head);
        head = NULL;
        return;
    }
    struct Node *newTail = tail->prev;
    newTail->next = head;
    head->prev = newTail;
    free(tail);
}

void displayForward() {
    if (head == NULL) {
        printf("Queue empty\n");
        return;
    }
    struct Node *temp = head;
    printf("Forward: ");
    do {
        printf("%d ", temp->data);
        temp = temp->next;
    } while (temp != head);
    printf("\n");
}

void displayBackward() {
    if (head == NULL) {
        printf("Queue empty\n");
        return;
    }
    struct Node *tail = head->prev, *temp = tail;
    printf("Backward: ");
    do {
        printf("%d ", temp->data);
        temp = temp->prev;
    } while (temp != tail);
    printf("\n");
}

void searchTicket(int value) {
    if (head == NULL) {
        printf("Queue empty\n");
        return;
    }
    struct Node *temp = head;
    int pos = 1, found = 0;
    do {
        if (temp->data == value) {
            printf("Ticket %d found at position %d\n", value, pos);
            found = 1;
            break;
        }
        temp = temp->next;
        pos++;
    } while (temp != head);
    if (!found)
        printf("Ticket %d not found\n", value);
}

int main() {
    int choice, value;
    while (1) {
        printf("\n1.Insert Front\n2.Insert Rear\n3.Delete Front\n4.Delete Rear\n5.Display Forward\n6.Display Backward\n7.Search Ticket\n8.Exit\nEnter choice: ");
        scanf("%d", &choice);
        switch (choice) {
            case 1:
                printf("Enter ticket number: ");
                scanf("%d", &value);
                insertFront(value);
                break;
            case 2:
                printf("Enter ticket number: ");
                scanf("%d", &value);
                insertRear(value);
                break;
            case 3:
                deleteFront();
                break;
            case 4:
                deleteRear();
                break;
            case 5:
                displayForward();
                break;
            case 6:
                displayBackward();
                break;
            case 7:
                printf("Enter ticket to search: ");
                scanf("%d", &value);
                searchTicket(value);
                break;
            case 8:
                exit(0);
            default:
                printf("Invalid choice\n");
        }
    }
    return 0;
}
