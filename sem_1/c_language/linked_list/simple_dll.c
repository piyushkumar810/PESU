#include<stdio.h>
#include<stdlib.h>


// structure of dll
typedef struct node
{
    struct node *prev;
    int data;
    struct node *next;
}*NODE;


void display(NODE head)
{
    if(head==NULL){
        printf("your list ia empty\n");
        return;
    }
    else{
        while(head!=NULL){
            printf("%d -> ", head->data);
            head=head->next;
        }
        printf("NULL\n");
    }
}

void display_opposit(NODE third){
    printf("diplay list opposit\n");
    while(third!=NULL){
        printf("%d -> ",third->data);
        third=third->prev;
    }
    printf("NULL\n");
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

    third->prev=second;
    second->prev=head;
    head->prev=NULL;

    display_opposit(third);


    return 0;
}