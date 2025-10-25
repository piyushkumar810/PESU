#include<stdio.h>
#include<stdlib.h>

typedef struct node{
    int data;
    struct node *link;
}*NODE;

NODE create_node(int data)
{
    NODE newnode=(NODE) malloc(sizeof(struct node));
    if(newnode!=NULL){
        newnode->data=data;
        newnode->link=NULL;
    }
    else{
        printf("\nunable to create a node ");
    }
    return newnode;
}

void display(NODE head)
{
    if(head==NULL){
        printf("\nyour list is empty");
    }
    else{
        printf("\nHead -> ");
        for(NODE temp=head; temp!=NULL; temp=temp->link){
            printf("%d ", temp->data);
        }
        printf(" -> NULL");
    }
}

int main()
{
    NODE head=NULL;
    NODE n1=create_node(10);
    NODE n2=create_node(20);

    head=n1;
    n1->link=n2;

    display(head);

    return 0;
}