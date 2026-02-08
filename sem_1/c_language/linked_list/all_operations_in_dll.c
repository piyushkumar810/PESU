#include <stdio.h>
#include <stdlib.h>

// Doubly Linked List Node
typedef struct node {
    int data;
    struct node *prev;
    struct node *next;
} *DLL;

// Create a new node
DLL create_node(int data) {
    DLL new_node = (DLL)malloc(sizeof(struct node));
    if (new_node == NULL) {
        printf("Memory allocation failed\n");
        exit(1);
    }
    new_node->data = data;
    new_node->prev = NULL;
    new_node->next = NULL;
    return new_node;
}

// Display list (forward)
void display_forward(DLL head) {
    if (head == NULL) {
        printf("List is empty\n");
        return;
    }

    DLL temp = head;
    printf("NULL <-> ");
    while (temp != NULL) {
        printf("%d <-> ", temp->data);
        temp = temp->next;
    }
    printf("NULL\n");
}

// Display list (backward)
void display_backward(DLL head) {
    if (head == NULL) {
        printf("List is empty\n");
        return;
    }

    DLL temp = head;
    while (temp->next != NULL)
        temp = temp->next;

    printf("NULL <-> ");
    while (temp != NULL) {
        printf("%d <-> ", temp->data);
        temp = temp->prev;
    }
    printf("NULL\n");
}

// Insert at front
DLL insert_front(DLL head, int data) {
    DLL new_node = create_node(data);

    if (head != NULL) {
        new_node->next = head;
        head->prev = new_node;
    }
    return new_node;
}

// Insert at end
DLL insert_end(DLL head, int data) {
    DLL new_node = create_node(data);

    if (head == NULL)
        return new_node;

    DLL temp = head;
    while (temp->next != NULL)
        temp = temp->next;

    temp->next = new_node;
    new_node->prev = temp;
    return head;
}

// Insert at a given position (1-based index)
DLL insert_at_position(DLL head, int data, int pos) {
    if (pos <= 0) {
        printf("Invalid position\n");
        return head;
    }

    if (pos == 1)
        return insert_front(head, data);

    DLL temp = head;
    for (int i = 1; i < pos - 1 && temp != NULL; i++)
        temp = temp->next;

    if (temp == NULL) {
        printf("Position out of range\n");
        return head;
    }

    DLL new_node = create_node(data);
    new_node->next = temp->next;
    new_node->prev = temp;

    if (temp->next != NULL)
        temp->next->prev = new_node;

    temp->next = new_node;
    return head;
}

// Delete from front
DLL delete_front(DLL head) {
    if (head == NULL) {
        printf("List is empty\n");
        return NULL;
    }

    DLL temp = head;
    head = head->next;

    if (head != NULL)
        head->prev = NULL;

    free(temp);
    return head;
}

// Delete from end
DLL delete_end(DLL head) {
    if (head == NULL) {
        printf("List is empty\n");
        return NULL;
    }

    if (head->next == NULL) {
        free(head);
        return NULL;
    }

    DLL temp = head;
    while (temp->next != NULL)
        temp = temp->next;

    temp->prev->next = NULL;
    free(temp);
    return head;
}

// Delete at a given position
DLL delete_at_position(DLL head, int pos) {
    if (head == NULL || pos <= 0) {
        printf("Invalid operation\n");
        return head;
    }

    if (pos == 1)
        return delete_front(head);

    DLL temp = head;
    for (int i = 1; i < pos && temp != NULL; i++)
        temp = temp->next;

    if (temp == NULL) {
        printf("Position out of range\n");
        return head;
    }

    if (temp->next != NULL)
        temp->next->prev = temp->prev;

    if (temp->prev != NULL)
        temp->prev->next = temp->next;

    free(temp);
    return head;
}

// Search an element
void search(DLL head, int key) {
    int pos = 1;
    DLL temp = head;

    while (temp != NULL) {
        if (temp->data == key) {
            printf("Element %d found at position %d\n", key, pos);
            return;
        }
        temp = temp->next;
        pos++;
    }
    printf("Element %d not found\n", key);
}

// Count nodes
int count_nodes(DLL head) {
    int count = 0;
    while (head != NULL) {
        count++;
        head = head->next;
    }
    return count;
}

// Main function
int main() {
    DLL head = NULL;

    head = insert_front(head, 10);
    head = insert_end(head, 20);
    head = insert_end(head, 30);
    head = insert_at_position(head, 15, 2);

    printf("DLL Forward: ");
    display_forward(head);

    printf("DLL Backward: ");
    display_backward(head);

    head = delete_front(head);
    head = delete_end(head);
    head = delete_at_position(head, 2);

    printf("After Deletions: ");
    display_forward(head);

    search(head, 20);
    printf("Total Nodes: %d\n", count_nodes(head));

    return 0;
}
