#include<stdio.h>
#include<stdlib.h>

typedef struct node {
    int data;
    struct node *next, *prev;
} *NODE;

// Function to create a new node
NODE create_node(int data) {
    NODE newnode = (NODE) malloc(sizeof(struct node));
    if(newnode == NULL) {
        printf("\nOut of memory");
        return NULL;
    }
    newnode->data = data;
    newnode->next = NULL;
    newnode->prev = NULL;
    return newnode;
}

// Display list
void Display(NODE head) {
    if(head == NULL)
        printf("\nList is empty.\n");
    else {
        NODE temp = head;
        printf("\nHEAD->");
        while(temp != NULL) {
            printf("%d->", temp->data);
            temp = temp->next;
        }
        printf("NULL\n");
    }
}

// Insert at front
NODE insert_front(int data, NODE head) {
    NODE newnode = create_node(data);
    if(head != NULL) {
        newnode->next = head;
        head->prev = newnode;
    }
    printf("Node inserted at front: [%d]\n", newnode->data);
    return newnode;
}

// Insert at last
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

// Insert after given position
NODE insert_after_position(NODE head, int data, int pos) {
    if(head == NULL) {
        printf("\nList is empty. Cannot insert.\n");
        return head;
    }

    NODE temp = head;
    for(int i=1; i<pos && temp!=NULL; i++)
        temp = temp->next;

    if(temp == NULL) {
        printf("\nPosition not found.\n");
        return head;
    }

    NODE newnode = create_node(data);
    newnode->next = temp->next;
    newnode->prev = temp;
    if(temp->next != NULL)
        temp->next->prev = newnode;
    temp->next = newnode;

    printf("Node [%d] inserted after position [%d]\n", data, pos);
    return head;
}

// Delete from front
NODE delete_front(NODE head) {
    if(head == NULL) {
        printf("\nList is empty.\n");
        return head;
    }
    NODE temp = head;
    head = head->next;
    if(head != NULL)
        head->prev = NULL;

    printf("Deleted node: [%d]\n", temp->data);
    free(temp);
    return head;
}

// Delete from last
NODE delete_last(NODE head) {
    if(head == NULL) {
        printf("\nList is empty.\n");
        return head;
    }
    if(head->next == NULL) {
        printf("Deleted node: [%d]\n", head->data);
        free(head);
        return NULL;
    }

    NODE temp = head;
    while(temp->next != NULL)
        temp = temp->next;

    printf("Deleted node: [%d]\n", temp->data);
    temp->prev->next = NULL;
    free(temp);
    return head;
}

// Delete at position
NODE delete_at_position(NODE head, int pos) {
    if(head == NULL) {
        printf("\nList is empty.\n");
        return head;
    }

    if(pos == 1)
        return delete_front(head);

    NODE temp = head;
    for(int i=1; i<pos && temp!=NULL; i++)
        temp = temp->next;

    if(temp == NULL) {
        printf("\nPosition not found.\n");
        return head;
    }

    if(temp->next != NULL)
        temp->next->prev = temp->prev;

    if(temp->prev != NULL)
        temp->prev->next = temp->next;

    printf("Deleted node: [%d]\n", temp->data);
    free(temp);
    return head;
}

// Count nodes
int count_nodes(NODE head) {
    int count = 0;
    for(NODE temp = head; temp != NULL; temp = temp->next)
        count++;
    return count;
}

// Sort DLL (ascending)
NODE sort_dll(NODE head) {
    if(head == NULL)
        return head;

    NODE i, j;
    int temp;
    for(i = head; i->next != NULL; i = i->next) {
        for(j = i->next; j != NULL; j = j->next) {
            if(i->data > j->data) {
                temp = i->data;
                i->data = j->data;
                j->data = temp;
            }
        }
    }
    printf("\nList sorted successfully.\n");
    return head;
}

// ------------------------ MAIN ------------------------
int main() {
    NODE head = NULL;
    int choice, data, pos;

    while(1) {
        printf("\n----- Doubly Linked List Menu -----\n");
        printf("1. Insert at Front\n");
        printf("2. Insert at Last\n");
        printf("3. Insert After Position\n");
        printf("4. Delete from Front\n");
        printf("5. Delete from Last\n");
        printf("6. Delete at Position\n");
        printf("7. Display\n");
        printf("8. Count Nodes\n");
        printf("9. Sort List\n");
        printf("10. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch(choice) {
            case 1:
                printf("Enter data: ");
                scanf("%d", &data);
                head = insert_front(data, head);
                break;

            case 2:
                printf("Enter data: ");
                scanf("%d", &data);
                head = insert_last(data, head);
                break;

            case 3:
                printf("Enter position after which to insert: ");
                scanf("%d", &pos);
                printf("Enter data: ");
                scanf("%d", &data);
                head = insert_after_position(head, data, pos);
                break;

            case 4:
                head = delete_front(head);
                break;

            case 5:
                head = delete_last(head);
                break;

            case 6:
                printf("Enter position to delete: ");
                scanf("%d", &pos);
                head = delete_at_position(head, pos);
                break;

            case 7:
                Display(head);
                break;

            case 8:
                printf("Total nodes = %d\n", count_nodes(head));
                break;

            case 9:
                head = sort_dll(head);
                Display(head);
                break;

            case 10:
                printf("Exiting...\n");
                exit(0);

            default:
                printf("Invalid choice! Try again.\n");
        }
    }
    return 0;
}
