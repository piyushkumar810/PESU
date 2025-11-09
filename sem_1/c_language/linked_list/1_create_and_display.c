#include<stdio.h>
#include<stdlib.h>

// struct node{
//     int data;
//     struct node *next;
// };

// void diaplay(struct node* head){
//     while(head!=NULL){
//         printf("%d -> ",head->data);
//         head=head->next;
//     }
//     printf("NULL\n");
// }

// int main(){

//     struct node* head=NULL, *second=NULL, *third=NULL;

//     head=(struct node*)malloc(sizeof(struct node));
//     second=(struct node*)malloc(sizeof(struct node));
//     third=(struct node*)malloc(sizeof(struct node));

//     head->data=10;
//     head->next=second;

//     head->next->data=20;
//     head->next->next=third;

//     head->next->next->data=30;
//     head->next->next->next=NULL;

//     diaplay(head);


//     return 0;
// }


// ------------------------------------------ or-------------------------------------
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