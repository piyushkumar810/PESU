#include<stdio.h>
#include<stdlib.h>

typedef struct node{
    int info;
    struct node *link;
} NODE;

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

void display(NODE *head){
    while(head != NULL){
        printf("%d -> ", head->info);
        head = head->link;
    }
    printf("NULL\n");
}

NODE *reverse_iterative(NODE *head){
    NODE *prev = NULL, *curr = head, *next = NULL;

    while(curr != NULL){
        next = curr->link;
        curr->link = prev;
        prev = curr;
        curr = next;
    }
    return prev;
}

NODE *reverse_recursive(NODE *head){
    if(head == NULL || head->link == NULL)
        return head;

    NODE *newHead = reverse_recursive(head->link);
    head->link->link = head;
    head->link = NULL;

    return newHead;
}

int main(){
    NODE *head = NULL;
    int n, data;

    printf("Enter number of nodes: ");
    scanf("%d", &n);

    for(int i = 0; i < n; i++){
        scanf("%d", &data);
        head = insert_end(head, data);
    }

    printf("Original list:\n");
    display(head);

    head = reverse_iterative(head);
    printf("After iterative reverse:\n");
    display(head);

    head = reverse_recursive(head);
    printf("After recursive reverse:\n");
    display(head);

    return 0;
}
