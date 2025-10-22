#include<stdio.h>
#include<stdlib.h>

typedef struct node{
    int data;
    struct node* link;
}*NODE;

int main() {
    NODE head, newnode;
    head = NULL;

    newnode = (NODE) malloc(sizeof(struct node));
    
    // ----------------------------------------- static entry
    // newnode->data = 10;
    // newnode->link = NULL;

    // head = newnode;

    // printf("Node created with data = %d\n", head->data);

    // ------------------------------------------- entering data at runtime

    printf("enter data ");
    scanf("%d", &newnode->data);
    newnode->link=NULL;
    head=newnode;
    printf("your node created with the value of %d \n", head->data);
    printf("address of the data is %d ", &head);
    printf("\naddress of the data is %d ", *head);
    printf("\naddress of the data is %d ", &head->data);
    printf("\nwhat is inside link %d", head->link);

    // newnode->data = 10;
    // newnode->link = NULL;

    // head = newnode;

    // printf("Node created with data = %d\n", head->data);
    return 0;
}
