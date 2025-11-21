#include<stdio.h>
#include<stdlib.h>

typedef struct node{
    int data;
    struct node *next;
}*NODE;

NODE create_node(int data){
    NODE temp=(NODE)malloc(sizeof(struct node));
    if(temp==NULL){
        printf("there is no space\n");
        exit(1);
    }
    temp->data=data;
    temp->next=NULL;
    return temp;
}

void display(NODE head){
    if(head==NULL){
        printf("ll is empty\n");
        return;
    }
    else{
        printf("HEAD -> ");

        while(head!=NULL){
            printf("%d -> ",head->data);
            head=head->next;
        }
        printf(" NULL");
    }
}

NODE insert_front(NODE head, int data){
    NODE newnode=create_node(data);
    newnode->next=head;
    return newnode;
}

NODE insert_last(NODE head, int data){
    NODE newnode=create_node(data);
    if(head==NULL){
        return newnode;
    }

    else{
        NODE temp=head;

        while(temp->next!=NULL){
            temp=temp->next;
        }
        temp->next=newnode;
        // newnode->next=NULL;   we will not do this because in create_node i am already assigning node->next=NULL 
        return head;
    }
}

NODE delete_front(NODE head){
    if(head==NULL){
        printf("your list is empty\n");
        return NULL;
    }
    else{
        NODE temp=head;
        head=head->next;
        printf("delete %d\n",temp->data);
        free(temp);
        return head;
    }
}

NODE delete_last(NODE head){
    if(head==NULL){
        printf("your list is empty\n");
        return NULL;
    }

    // if there is only one element
    if(head->next==NULL){
        printf("deleted %d\n",head->data);
        free(head);
        return NULL;
    }

    else{
        NODE temp=head;
        while(temp->next->next!=NULL){
            temp=temp->next;
        }
        
    printf("Deleted: %d\n",temp->next->data);
    free(temp->next);
    temp->next=NULL;
    return head;
    }
} 