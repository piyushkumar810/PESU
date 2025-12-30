#include<stdio.h>
#include<stdlib.h>

typedef struct node{
    int data;
    struct node *next;
}*NODE;

NODE node_creation(data){
    NODE newnode=(NODE)malloc(sizeof(struct node));
    if(newnode==NULL){
        printf("memory allocation failed\n");
        exit(0);
    }
    newnode->data=data;
    newnode->next=NULL;
    return newnode;
}

void Display_ll(NODE head){
    if(head==NULL){
        printf("list is empty\n");
        return;
    }
    else{
        printf(" HEAD->");
        while(head!=NULL){
            head=head->next;
        }
    }
}

NODE insert_front(NODE head,int data){
    NODE newnode=node_creation(data);  
    newnode->next=head;        
    return newnode; 
}

NODE insert_end(NODE head,int data){
    NODE newnode=node_creation(data);
    if(head==NULL){
        printf("list empty !");
        return newnode;
    }
    else{
        NODE temp=head;
        while(temp->next!=NULL){
            temp=temp->next;
        }
        temp->next=newnode;
    }
    return head;
}

int main(){
    NODE head=NULL;
    int choice,data;
    while(1){
        printf("============= LINKED LIST MENU =============\n");
        printf("1.insert at front\n");
        printf("2.insert at end\n");
        printf("3.Display list\n");
        printf("0.Exit program\n");

        printf("Enter your choice\n");
        scanf("%d",&choice);

        switch(choice){
            case 1:
               printf("enter the data\n");
               scanf("%d",&data);
               head=insert_front(head,data);
               break;

            case 2:
              printf("enter the data ");
              scanf("%d",&data);
              head=insert_end(head,data);
              break;

            case 3:
              Display_ll(head);
              break;

            case 0:
              printf("Exiting program...\n");
              exit(0);
            
            default:
                printf("Invalid choice! Please try again.\n");
        }
    }
    return 0;
}