#include <stdio.h>
#include <stdlib.h>

// Define the node structure
typedef struct node {
    int data;
    struct node* link;
} *NODE;

// Function to create a new node
NODE create_node(int data) {
    NODE temp = (NODE)malloc(sizeof(struct node));
    if (temp != NULL) {
        temp->data = data;
        temp->link = NULL;
    } else {
        printf("\nUnable to create a Node.\n");
    }
    return temp;
}

// Function to display the linked list
void Display(NODE Head) {
    if (Head == NULL)
        printf("\nList is empty.\n");
    else {
        printf("\nHEAD -> ");
        for (NODE temp = Head; temp != NULL; temp = temp->link)
            printf("%d -> ", temp->data);
        printf("NULL\n");
    }
}

// Insert at the front
NODE ins_front(NODE Head, int data) {
    NODE new_node = create_node(data);
    if (new_node != NULL) {
        new_node->link = Head;
        Head = new_node;
    }
    return Head;
}

// Insert at the end
NODE ins_last(NODE Head, int data) {
    NODE new_node = create_node(data);
    if (new_node == NULL)
        return Head;

    if (Head == NULL)
        return new_node;

    NODE temp = Head;
    while (temp->link != NULL)
        temp = temp->link;

    temp->link = new_node;
    return Head;
}

// Insert at a specific position
NODE insert_position(NODE Head, int data, int pos) {
    if (pos < 0) {
        printf("\nInvalid position. Must be >= 0.\n");
        return Head;
    }

    NODE new_node = create_node(data);
    if (new_node == NULL)
        return Head;

    if (pos == 0 || Head == NULL) {
        new_node->link = Head;
        return new_node;
    }

    NODE curr = Head;
    for (int i = 0; i < pos - 1 && curr != NULL; i++)
        curr = curr->link;

    if (curr == NULL) {
        printf("\nPosition out of range. Not inserted.\n");
        free(new_node);
        return Head;
    }

    new_node->link = curr->link;
    curr->link = new_node;

    return Head;
}

// Delete last node
NODE Delete_Last(NODE Head) {
    if (Head == NULL) {
        printf("\nList is empty. Nothing to delete.\n");
        return NULL;
    }

    if (Head->link == NULL) {
        printf("\nDeleted Node: %d\n", Head->data);
        free(Head);
        return NULL;
    }

    NODE curr = Head;
    while (curr->link->link != NULL)
        curr = curr->link;

    printf("\nDeleted Node: %d\n", curr->link->data);
    free(curr->link);
    curr->link = NULL;

    return Head;
}

// Delete node by position
NODE Delete_Position(NODE Head, int pos) {
    if (Head == NULL) {
        printf("\nList is empty.\n");
        return NULL;
    }

    if (pos < 0) {
        printf("\nInvalid position. Must be >= 0.\n");
        return Head;
    }

    if (pos == 0) {
        NODE temp = Head;
        printf("\nDeleted Node: %d\n", temp->data);
        Head = Head->link;
        free(temp);
        return Head;
    }

    NODE curr = Head;
    for (int i = 0; i < pos - 1 && curr != NULL && curr->link != NULL; i++)
        curr = curr->link;

    if (curr == NULL || curr->link == NULL) {
        printf("\nPosition out of range. Nothing deleted.\n");
        return Head;
    }

    NODE temp = curr->link;
    printf("\nDeleted Node: %d\n", temp->data);
    curr->link = temp->link;
    free(temp);

    return Head;
}

// NODE search_and_return_previous(NODE Head, int value)
// {
//     if(Head == NULL || Head == value)
//     {
//         return NULL;
//     }
//     NODE curr=Head;
//     while(curr -> link != NULL && curr-> link->data!=value)
//     curr=curr->link;

//     return (curr->link == NULL)? NULL : curr;
// }

// Delete node by value
NODE Delete_Value(NODE Head, int value) {
    if (Head == NULL) {
        printf("\nList is empty.\n");
        return NULL;
    }

    if (Head->data == value) {
        NODE temp = Head;
        printf("\nDeleted Node with value: %d\n", value);
        Head = Head->link;
        free(temp);
        return Head;
    }

    NODE curr = Head;
    while (curr->link != NULL && curr->link->data != value)
        curr = curr->link;

    if (curr->link == NULL) {
        printf("\nValue %d not found in the list.\n", value);
        return Head;
    }

    NODE temp = curr->link;
    printf("\nDeleted Node with value: %d\n", value);
    curr->link = temp->link;
    free(temp);

    return Head;
}

// Main function with user menu
int main() {
    NODE Head = NULL;
    int choice, data, pos, value;

    while (1) {
        printf("\n===== LINKED LIST MENU =====");
        printf("\n1. Insert at Front");
        printf("\n2. Insert at End");
        printf("\n3. Insert at Specific Position");
        printf("\n4. Delete Last Node");
        printf("\n5. Delete by Position");
        printf("\n6. Delete by Value");
        printf("\n7. Display List");
        printf("\n8. Exit");
        printf("\nEnter your choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                printf("\nEnter data to insert at front: ");
                scanf("%d", &data);
                Head = ins_front(Head, data);
                break;

            case 2:
                printf("\nEnter data to insert at end: ");
                scanf("%d", &data);
                Head = ins_last(Head, data);
                break;

            case 3:
                printf("\nEnter data to insert: ");
                scanf("%d", &data);
                printf("Enter position (starting from 0): ");
                scanf("%d", &pos);
                Head = insert_position(Head, data, pos);
                break;

            case 4:
                Head = Delete_Last(Head);
                break;

            case 5:
                printf("\nEnter position to delete (starting from 0): ");
                scanf("%d", &pos);
                Head = Delete_Position(Head, pos);
                break;

            case 6:
                printf("\nEnter value to delete: ");
                scanf("%d", &value);
                Head = Delete_Value(Head, value);
                break;

            case 7:
                Display(Head);
                break;

            case 8:
                printf("\nExiting program. Goodbye!\n");
                return 0;

            default:
                printf("\nInvalid choice. Try again.\n");
        }
    }

    return 0;
}
