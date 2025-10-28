#include <stdio.h>
#include <stdlib.h>

typedef struct node {
    int data;
    struct node* link;
} *NODE;

NODE create_node(int data) {
    NODE temp = (NODE) malloc(sizeof(struct node));
    if (temp == NULL) {
        printf("Out of memory\n");
        exit(1);
    }
    temp->data = data;
    temp->link = temp; // circular link
    return temp;
}

NODE go_last(NODE head) {
    if (head == NULL) return NULL;
    NODE temp = head;
    while (temp->link != head)
        temp = temp->link;
    return temp;
}

void display(NODE head) {
    if (head == NULL) {
        printf("List is empty\n");
        return;
    }
    NODE temp = head;
    printf("Circular Linked List elements: ");
    do {
        printf("%d ", temp->data);
        temp = temp->link;
    } while (temp != head);
    printf("\n");
}

NODE insert_front(NODE head, int data) {
    NODE newnode = create_node(data);
    if (head == NULL) {
        head = newnode;
    } else {
        NODE last = go_last(head);
        newnode->link = head;
        last->link = newnode;
        head = newnode;
    }
    return head;
}

NODE delete_front(NODE head) {
    if (head == NULL) {
        printf("List is empty, nothing to delete.\n");
        return NULL;
    }

    if (head->link == head) {
        printf("Deleted element: %d\n", head->data);
        free(head);
        return NULL;
    }

    NODE last = go_last(head);
    NODE temp = head;
    printf("Deleted element: %d\n", head->data);
    head = head->link;
    last->link = head;
    free(temp);

    return head;
}

NODE delete_end(NODE head) {
    if (head == NULL) {
        printf("List is empty, nothing to delete.\n");
        return NULL;
    }

    if (head->link == head) {
        printf("Deleted element: %d\n", head->data);
        free(head);
        return NULL;
    }

    NODE temp = head;
    while (temp->link->link != head)
        temp = temp->link;

    NODE last = temp->link;
    printf("Deleted element: %d\n", last->data);
    temp->link = head;
    free(last);

    return head;
}

int main() {
    NODE head = NULL;

    head = insert_front(head, 30);
    head = insert_front(head, 20);
    head = insert_front(head, 10);

    printf("After inserting at front:\n");
    display(head);

    head = delete_front(head);
    display(head);

    head = delete_end(head);
    display(head);

    return 0;
}