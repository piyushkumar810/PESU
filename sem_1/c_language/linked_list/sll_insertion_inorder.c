#include<stdio.h>
#include<stdlib.h>


typedef struct node{
    int data;
    struct node *next;
}*NODE;

NODE create_node(int data){
    NODE new_node=(NODE)malloc(sizeof(struct node));
    if(new_node==NULL){
        printf("memory allocation failed .\n");
        exit(1);    
    }
    new_node->data=data;
    new_node->next=NULL;
    return new_node;
}

NODE insert_in_order(NODE head,int data){
    NODE new_node=create_node(data);

    if(head==NULL){
        printf("list is empty");
        return;
    }
    else{
        NODE temp=head;
        while(temp->data<new_node->data){
            temp=temp->next;
        }
        temp->next=new_node;
    }
}

int main(){

    NODE head=NULL;
    


    return 0;
}