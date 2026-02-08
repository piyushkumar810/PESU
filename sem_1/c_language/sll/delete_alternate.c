#include<stdio.h>
#include<stdlib.h>

typedef struct node{
    int info;
    struct node *link;
} NODE;

/* Insert at end */
NODE *insert_end(NODE *head, int data){
    NODE *newnode = (NODE *)malloc(sizeof(NODE));
    newnode->info = data;
    newnode->link = NULL;

    if(head == NULL)
        return newnode;

    NODE *temp = head;
    while(temp->link != NULL)
        temp = temp->link;

    temp->link = newnode;
    return head;
}

/* Display list */
void display(NODE *head){
    if(head == NULL){
        printf("List is empty\n");
        return;
    }

    NODE *temp = head;
    while(temp != NULL){
        printf("%d -> ", temp->info);
        temp = temp->link;
    }
    printf("NULL\n");
}

/* Delete alternate nodes */
NODE *delete_alternate(NODE *head){
    if(head == NULL || head->link == NULL){
        printf("List is empty or has only one node\n");
        return head;
    }

    NODE *current = head;
    NODE *temp;

    while(current != NULL && current->link != NULL){
        temp = current->link;
        current->link = temp->link;
        printf("Deleted element is %d\n", temp->info);
        free(temp);
        current = current->link;
    }

    return head;
}

int main(){
    NODE *head = NULL;
    int n, data;

    printf("Enter number of nodes: ");
    scanf("%d", &n);

    for(int i = 0; i < n; i++){
        printf("Enter data: ");
        scanf("%d", &data);
        head = insert_end(head, data);
    }

    printf("\nOriginal list:\n");
    display(head);

    head = delete_alternate(head);

    printf("\nList after deleting alternate nodes:\n");
    display(head);

    return 0;
}
