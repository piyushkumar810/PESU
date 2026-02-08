#include <stdio.h>
#include <stdlib.h>

// Circular Linked List Node
typedef struct node {
    int data;
    struct node *next;
} *CLL;

// Create a new node
CLL create_node(int data) {
    CLL new_node = (CLL)malloc(sizeof(struct node));
    if (new_node == NULL) {
        printf("Memory allocation failed\n");
        exit(1);
    }
    new_node->data = data;
    new_node->next = new_node;   // circular link
    return new_node;
}

// Display Circular Linked List
void display(CLL head) {
    if (head == NULL) {
        printf("List is empty\n");
        return;
    }

    CLL temp = head;
    printf("HEAD -> ");
    do {
        printf("%d -> ", temp->data);
        temp = temp->next;
    } while (temp != head);
    printf("HEAD\n");
}

// Insert at front
CLL insert_front(CLL head, int data) {
    CLL new_node = create_node(data);

    if (head == NULL)
        return new_node;

    CLL temp = head;
    while (temp->next != head)
        temp = temp->next;

    new_node->next = head;
    temp->next = new_node;
    return new_node;   // new node becomes head
}

// Insert at end
CLL insert_end(CLL head, int data) {
    CLL new_node = create_node(data);

    if (head == NULL)
        return new_node;

    CLL temp = head;
    while (temp->next != head)
        temp = temp->next;

    temp->next = new_node;
    new_node->next = head;
    return head;
}

// Insert at a given position (1-based index)
CLL insert_at_position(CLL head, int data, int pos) {
    if (pos <= 0) {
        printf("Invalid position\n");
        return head;
    }

    if (pos == 1)
        return insert_front(head, data);

    CLL temp = head;
    for (int i = 1; i < pos - 1 && temp->next != head; i++)
        temp = temp->next;

    if (temp->next == head && pos > 2) {
        printf("Position out of range\n");
        return head;
    }

    CLL new_node = create_node(data);
    new_node->next = temp->next;
    temp->next = new_node;
    return head;
}

// Delete from front
CLL delete_front(CLL head) {
    if (head == NULL) {
        printf("List is empty\n");
        return NULL;
    }

    if (head->next == head) {   // only one node
        free(head);
        return NULL;
    }

    CLL temp = head;
    while (temp->next != head)
        temp = temp->next;

    CLL del = head;
    head = head->next;
    temp->next = head;
    free(del);
    return head;
}

// Delete from end
CLL delete_end(CLL head) {
    if (head == NULL) {
        printf("List is empty\n");
        return NULL;
    }

    if (head->next == head) {
        free(head);
        return NULL;
    }

    CLL temp = head;
    CLL prev = NULL;

    while (temp->next != head) {
        prev = temp;
        temp = temp->next;
    }

    prev->next = head;
    free(temp);
    return head;
}

// Delete at a given position
CLL delete_at_position(CLL head, int pos) {
    if (head == NULL || pos <= 0) {
        printf("Invalid operation\n");
        return head;
    }

    if (pos == 1)
        return delete_front(head);

    CLL temp = head;
    CLL prev = NULL;

    for (int i = 1; i < pos && temp->next != head; i++) {
        prev = temp;
        temp = temp->next;
    }

    if (temp->next == head && pos > 1) {
        printf("Position out of range\n");
        return head;
    }

    prev->next = temp->next;
    free(temp);
    return head;
}

// Search an element
void search(CLL head, int key) {
    if (head == NULL) {
        printf("List is empty\n");
        return;
    }

    int pos = 1;
    CLL temp = head;

    do {
        if (temp->data == key) {
            printf("Element %d found at position %d\n", key, pos);
            return;
        }
        temp = temp->next;
        pos++;
    } while (temp != head);

    printf("Element %d not found\n", key);
}

// Count nodes
int count_nodes(CLL head) {
    if (head == NULL)
        return 0;

    int count = 0;
    CLL temp = head;
    do {
        count++;
        temp = temp->next;
    } while (temp != head);

    return count;
}

// Main function
int main() {
    CLL head = NULL;

    head = insert_front(head, 10);
    head = insert_end(head, 20);
    head = insert_end(head, 30);
    head = insert_at_position(head, 15, 2);

    display(head);

    head = delete_front(head);
    head = delete_end(head);
    head = delete_at_position(head, 2);

    display(head);

    search(head, 20);
    printf("Total nodes: %d\n", count_nodes(head));

    return 0;
}
