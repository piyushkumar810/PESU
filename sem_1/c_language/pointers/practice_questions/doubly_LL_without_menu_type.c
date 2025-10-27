#include<stdio.h>
#include<stdlib.h>

typedef struct node {
    int data;
    struct node *next, *prev;
} *NODE;

// Create a new node
NODE create_node(int data) {
    NODE newnode = (NODE) malloc(sizeof(struct node));
    if(newnode == NULL) {
        printf("\nOut of memory");
        return NULL;
    }
    newnode->data = data;
    newnode->prev = NULL;
    newnode->next = NULL;
    return newnode;
}

// Display list from head to tail
void Display(NODE head) {
    if(head == NULL)
        printf("Empty List\n");
    else {
        printf("\nHEAD->");
        for(NODE temp = head; temp != NULL; temp = temp->next)
            printf("%d->", temp->data);
        printf("NULL\n");
    }
}

// Insert node at front
NODE insert_front(int data, NODE head) {
    NODE newnode = create_node(data);
    if(head != NULL) {
        newnode->next = head;
        head->prev = newnode;
    }
    printf("Node inserted at front: [%d]\n", newnode->data);
    return newnode;
}

// Insert node at end
NODE insert_last(int data, NODE head) {
    NODE newnode = create_node(data);
    if(head == NULL) {
        printf("Node inserted at last: [%d]\n", newnode->data);
        return newnode;
    }
    NODE temp = head;
    while(temp->next != NULL)
        temp = temp->next;

    temp->next = newnode;
    newnode->prev = temp;
    printf("Node inserted at last: [%d]\n", newnode->data);
    return head;
}

// Delete node from front
NODE delete_front(NODE head) {
    if(head == NULL) {
        printf("\nEmpty list");
        return head;
    }
    NODE temp = head;
    head = head->next;
    if(head != NULL)
        head->prev = NULL;
    printf("\nDeleted node is [%d]\n", temp->data);
    free(temp);
    return head;
}

// Delete node from last
NODE delete_last(NODE head) {
    if(head == NULL) {
        printf("\nEmpty list");
        return head;
    }
    if(head->next == NULL) {
        printf("Deleted node is: [%d]\n", head->data);
        free(head);
        return NULL;
    }

    NODE temp = head;
    while(temp->next != NULL)
        temp = temp->next;

    printf("Deleted node is [%d]\n", temp->data);
    temp->prev->next = NULL;
    free(temp);
    return head;
}

// Insert at specific position (1-based index)
NODE insert_at_position(int data, NODE head, int pos) {
    NODE newnode = create_node(data);
    if(pos <= 1 || head == NULL) {
        newnode->next = head;
        if(head) head->prev = newnode;
        printf("Node [%d] inserted at position [%d]\n", data, pos);
        return newnode;
    }

    NODE temp = head;
    int i = 1;
    while(i < pos - 1 && temp->next != NULL) {
        temp = temp->next;
        i++;
    }

    newnode->next = temp->next;
    newnode->prev = temp;
    if(temp->next != NULL)
        temp->next->prev = newnode;
    temp->next = newnode;

    printf("Node [%d] inserted at position [%d]\n", data, pos);
    return head;
}

// Insert in sorted order
NODE insert_ordered(int data, NODE head) {
    NODE newnode = create_node(data);
    if(head == NULL || data < head->data) {
        newnode->next = head;
        if(head) head->prev = newnode;
        printf("Node [%d] inserted in ordered list\n", data);
        return newnode;
    }

    NODE temp = head;
    while(temp->next != NULL && temp->next->data < data)
        temp = temp->next;

    newnode->next = temp->next;
    newnode->prev = temp;
    if(temp->next)
        temp->next->prev = newnode;
    temp->next = newnode;

    printf("Node [%d] inserted in ordered list\n", data);
    return head;
}

// Delete at specific position (1-based index)
NODE delete_at_position(NODE head, int pos) {
    if(head == NULL) {
        printf("\nEmpty list");
        return head;
    }
    if(pos <= 1) {
        NODE temp = head;
        head = head->next;
        if(head) head->prev = NULL;
        printf("Deleted node at position [%d] is [%d]\n", pos, temp->data);
        free(temp);
        return head;
    }

    NODE temp = head;
    int i = 1;
    while(i < pos && temp != NULL) {
        temp = temp->next;
        i++;
    }

    if(temp == NULL) {
        printf("Position [%d] not found\n", pos);
        return head;
    }

    printf("Deleted node at position [%d] is [%d]\n", pos, temp->data);
    if(temp->prev) temp->prev->next = temp->next;
    if(temp->next) temp->next->prev = temp->prev;
    free(temp);

    return head;
}

// Count number of nodes
int count_nodes(NODE head) {
    int count = 0;
    for(NODE temp = head; temp != NULL; temp = temp->next)
        count++;
    return count;
}

// Sort the doubly linked list (ascending)
NODE sort_dll(NODE head) {
    if(head == NULL)
        return head;

    for(NODE i = head; i->next != NULL; i = i->next) {
        for(NODE j = i->next; j != NULL; j = j->next) {
            if(i->data > j->data) {
                int temp = i->data;
                i->data = j->data;
                j->data = temp;
            }
        }
    }
    printf("List sorted in ascending order.\n");
    return head;
}

// MAIN FUNCTION
int main() {
    NODE head = NULL;

    // basic insertions
    head = insert_front(10, head);
    head = insert_last(20, head);
    head = insert_front(5, head);
    head = insert_last(30, head);
    Display(head);

    // insert at specific position
    head = insert_at_position(15, head, 3);
    Display(head);

    // ordered insertion
    head = insert_ordered(25, head);
    head = insert_ordered(1, head);
    Display(head);

    // delete at specific position
    head = delete_at_position(head, 4);
    Display(head);

    // count nodes
    printf("\nTotal nodes = %d\n", count_nodes(head));

    // sort DLL
    head = sort_dll(head);
    Display(head);

    return 0;
}
