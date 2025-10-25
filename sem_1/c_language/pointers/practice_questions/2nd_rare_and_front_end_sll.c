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
        printf("\nlist is empty");
    }
    else{
        printf("\nHead -> ");
        for(NODE temp=head; temp!=NULL; temp=temp->link){
            printf("%d -> ", temp->data);
        }
        printf("NULL");
    }
}

NODE ins_front(NODE head, int data)
{
    NODE new_node=create_node(data);
    if(new_node!=NULL){
        new_node->link=head;
        head=new_node;
    }
    return head;
}