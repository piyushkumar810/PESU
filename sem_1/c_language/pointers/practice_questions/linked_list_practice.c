#include<stdio.h>
#include<stdlib.h>

// creation of node
typedef struct node{
    int data;
    struct node *link;
}*NODE;

int main(){

    NODE head,newnode;
    newnode=(NODE)malloc(sizeof(struct node));

    printf("enter data ");
    scanf("%d", &newnode->data);
    newnode->link=NULL;
    head=newnode;

    printf("node is created with the value of %d ", head->data);

    return 0;
}