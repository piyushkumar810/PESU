#include<stdio.h>
#include<conio.h>

typedef struct node{
    int data;
    struct node *next;
}*NODE;

void display(NODE head){
    while(head!=NULL){
        printf("%d -> ", head->data);
        head=head->next;
    }
    printf("NULL\n");
}

// -----------insertion
// 1.at bignning
// 2.at end
// 3.at specific position


// ----------1. at bignning
// NODE insert_at_bignning(NODE head, int newdata){
//     NODE newnode=(NODE)malloc(sizeof(struct node));
//     newnode->data=newdata;
//     newnode->next=head;
//     return newnode;
// }

void insertion_at_end(NODE head, int newdata){
    NODE newnode=(NODE)malloc(sizeof(struct node));
    newnode->data=newdata;
    newnode->next=NULL;
     
    NODE temp=head;
    while(temp->next!=NULL){
        temp=temp->next;
    }
    temp->next=newnode;
}

int main(){

    NODE head=NULL, second=NULL, third=NULL;

    head=(NODE)malloc(sizeof(struct node));
    second=(NODE)malloc(sizeof(struct node));
    third=(NODE)malloc(sizeof(struct node));

    head->data=10;
    head->next=second;

    second->data=20;
    second->next=third;

    third->data=30;
    third->next=NULL;

    insert_at_bignning(head,40);
    insertion_at_end(head,50);

    display(head);
    
    return 0;
}