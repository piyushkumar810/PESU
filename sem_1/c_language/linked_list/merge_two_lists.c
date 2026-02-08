// merge two sorted list

#include <stdio.h>
#include <stdlib.h>

// Node definition
typedef struct node {
    int data;
    struct node *next;
} *NODE;

// Create a new node
NODE create_node(int data) {
    NODE new_node = (NODE)malloc(sizeof(struct node));
    if (new_node == NULL) {
        printf("Memory allocation failed\n");
        exit(1);
    }
    new_node->data = data;
    new_node->next = NULL;
    return new_node;
}

// Insert at end (used to build sorted lists)
NODE insert_end(NODE head, int data) {
    NODE new_node = create_node(data);

    if (head == NULL)
        return new_node;

    NODE temp = head;
    while (temp->next != NULL)
        temp = temp->next;

    temp->next = new_node;
    return head;
}

// Merge two sorted lists (OPTIMAL METHOD)
NODE merge_sorted_lists(NODE head1, NODE head2) {
    if (head1 == NULL) return head2;
    if (head2 == NULL) return head1;

    NODE result = NULL;

    if (head1->data < head2->data) {
        result = head1;
        result->next = merge_sorted_lists(head1->next, head2);
    } else {
        result = head2;
        result->next = merge_sorted_lists(head1, head2->next);
    }
    return result;
}

// Display list
void display(NODE head) {
    NODE temp = head;
    while (temp != NULL) {
        printf("%d -> ", temp->data);
        temp = temp->next;
    }
    printf("NULL\n");
}

// Main function
int main() {
    NODE Head1 = NULL;
    NODE Head2 = NULL;
    NODE Merged = NULL;

    // First sorted list
    Head1 = insert_end(Head1, 10);
    Head1 = insert_end(Head1, 20);
    Head1 = insert_end(Head1, 30);

    // Second sorted list
    Head2 = insert_end(Head2, 15);
    Head2 = insert_end(Head2, 25);
    Head2 = insert_end(Head2, 35);

    printf("List 1: ");
    display(Head1);

    printf("List 2: ");
    display(Head2);

    // Merge lists
    Merged = merge_sorted_lists(Head1, Head2);

    printf("Merged Sorted List: ");
    display(Merged);

    return 0;
}
