#include<stdio.h>
#include<stdlib.h>

typedef struct node{
    int data;
    struct node *next;
}*NODE;

NODE create_node(int value){
    NODE newnode=(NODE)malloc(sizeof(struct node));

    if(newnode==NULL){
        printf("memory allocation failed \n");
        exit(1);
    }
    newnode->data=value;
    newnode->next=NULL;
    return newnode;
}

void display(NODE head){
    if(head==NULL){
        printf("your list is empty");
        return;
    }
    else{
        while(head!=NULL){
            printf("%d ", head->data);
            head=head->next;
        }
    }
}


NODE insert_front(NODE head, int value){
    NODE newnode=create_node(value);
    newnode->next=head;
    return newnode;
}

NODE insert_last(NODE head, int value){

    NODE newnode=create_node(value);
    if(head==NULL){
        return newnode;
    }
    else{
        NODE temp=head;
        while(temp->next!=NULL){
            temp=temp->next;
        }

        temp->next=newnode;
        return head;
    }
}

NODE delete_front(NODE head){
    if(head==NULL){
        printf("there is n element to be deleted ");
        return NULL;
    }
    else{
        NODE temp=head;
        head=head->next;
        printf("ypur deleted element is :%d", temp->data);
        free(temp);
        return head;
    }
}

NODE delete_last(NODE head){
    if(head==NULL){
        printf("ll is empty\n");
        return NULL;
    }

    else if(head->next==NULL){
        printf("deleted element is :%d", head->data);
        free(head);
        return NULL;
    }

    else{
        NODE temp=head;
        while(temp->next->next!=NULL){
            temp=temp->next;
        }
        printf("delete %d", temp->next->data);
        free(temp->next);
        temp->next=NULL;
        return head;
    }
}