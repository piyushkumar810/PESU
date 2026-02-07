#include<stdio.h>
#include<stdlib.h>

typedef struct node{
    int data;
    struct node *next;
}*NODE;

NODE create_node(int data){
    NODE temp=(NODE)malloc(sizeof(struct node));
    if(temp==NULL){
        printf("memory allocation failed .\n");
        exit(1);    
    }
    temp->data=data;
    temp->next=NULL;
    return temp;
}

void display(NODE head){
    if(head==NULL){
        printf("list is empty \n");
        return;
    }
    printf("Head -> ");
    while(head!=NULL){
        printf(" %d ",head->data);
        head=head->next;
    }
    printf(" -> NULL \n");
}

NODE insert_front(NODE head,int data){
    NODE new_node=create_node(data);
    new_node->next=head;
    return new_node;

}

NODE insert_end(NODE head,int data){
    NODE new_node=create_node(data);

    if(head==NULL){
        return new_node;
    }
    else{
        NODE temp=head;

        while(temp->next!=NULL){
            temp=temp->next;
        }
        temp->next=new_node;
        return head;
    }
}

NODE insert_at_position(NODE head, int data, int pos){
    if(pos<0){
        printf("invalid position.\n");
        return head;
    }

    if(pos==0 || head==NULL){
        return insert_front(head,data);
    }

    NODE temp=head;
    for(int i=0; i<pos-1 && temp !=NULL; i++)
    {
        temp=temp->next;
    }

    if(temp==NULL){
        printf("position out of range.\n");
        return head;
    }

    NODE newnode=create_node(data);
    newnode->next=temp->next;
    temp->next=newnode;
    return head;
}

NODE delet_first(NODE head){
    if(head==NULL){
        printf("list is empty ");
        return 0;
    }
    else{
        NODE temp = head;
        head=head->next;
        printf("Delete :%d\n", temp->data);
        free(temp);
        return head;
    }
}

NODE delete_last(NODE head){
    if(head==NULL){
        printf("list is empty ");
        return 0;
    }

    if(head->next==NULL){
        printf("deleted :%d\n", head->data);
        free(head);
        return NULL;
    }

    NODE temp=head;
    while(temp->next->next!=NULL){
        temp=temp->next;
    }
    printf("deleted :%d\n", temp->next->data);
    free(temp->next);
    temp->next=NULL;
    return head;
}


int main(){
    NODE head=NULL;

    int pos,choice,data;

    while(1){
        printf("\n=========== LINKED LIST MENU ===========\n");
        printf("1. Insert at front\n");
        printf("2. Insert at end\n");
        printf("3. Insert at position\n");
        printf("4. Display list\n");
        printf("5. Delete first\n");
        printf("0. Exit\n");


        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch(choice){
            case 1: 
            printf("insert data :");
            scanf("%d",&data);
            head=insert_front(head,data);
            break;

            case 2:
            printf("insert data :");
            scanf("%d",&data);
            head=insert_end(head,data);
            break;

            case 3:
            printf("Enter data: ");
            scanf("%d", &data);
            printf("Enter position: ");
            scanf("%d", &pos);
            head = insert_at_position(head, data, pos);
            break;

            case 4:
            printf("list is \n:");
            display(head);
            break;

            case 5:
            printf("after 1st element deletion \n:");
            head=delet_first(head);
            break;

            case 0:
                printf("Exiting program...\n");
                exit(0);

            default :
            printf("Invalid choice! Please try again.\n");

        }
    }

    return 0;
}