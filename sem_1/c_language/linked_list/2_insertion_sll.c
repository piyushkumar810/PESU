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
NODE insert_at_bignning(NODE head, int newdata){
    
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

    display(head);
    
    return 0;
}