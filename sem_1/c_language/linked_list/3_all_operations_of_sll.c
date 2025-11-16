// ------------- lets do it sll all operation
// 1. create node
// 2. display
// 3. insert front
// 4. insert end
// 5. insert_position
// 6. delete last
// 7. delete position
// 8. delete value
// 9. count node
// 10. search value
// ----------- advance-----------
// 11. reverse the linked list
// 12. sort the linked list
// 13. merge two linked list
// 14. detect loop in the linked list
// 15. middle element using slow fast pointer

#include<stdio.h>
#include<stdlib.h>

// creating structure of the node
typedef struct node{
    int data;
    struct node *next;
}*NODE;
/*
Q) Why struct node *next instead of int *next?

    int *next would mean: "next is a pointer to an integer." That’s not what we want in a linked list. If you wrote int *next, each node would only know the address of some integer, not the address of another node.
    struct node *next means: "next is a pointer to another struct node." This is exactly what we need: each node in a linked list points to the next node in the chain.
*/


// creating a new node :-here we will simply create a new node that will consist of data and address
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
/*
Q) Why check (temp == NULL) after malloc?

    malloc tries to reserve a block of memory from the heap.
    If the system cannot provide memory (for example, if the heap is exhausted or fragmented), malloc returns NULL.
    If you don’t check and immediately use temp->data, you’ll be dereferencing a NULL pointer → segmentation fault / crash.

Q) What does exit(1) mean?

    exit(n) terminates the program immediately and returns the code n to the operating system.

    By convention:
    exit(0) → success (program ended normally).
    exit(1) (or any non‑zero value) → failure (program ended due to an error).
    
    So here, exit(1) signals: “Stop the program, something went wrong (memory allocation failed).”
*/


// displaying the linked list
void diaplay(NODE head){
    if(head==NULL){
        printf("list is empty. \n");
        return;
    }
    printf("HEAD -> ");
    // agar yaha tum (head->next!=NULL) karega tho ander head->data kaisa print kar payaga
    while(head!=NULL){
        printf("%d", head->data);
        head=head->next;
    }
    printf(" -> NULL \n");
}
/*
Q) why we are checking while(head!=NULL) because head cannot be NULL head ka next can be NULL
    beacuse inside while loop head is auto incremented by head->next and it is checking that only is (head->next is != NULL )  
*/


// insert at front
NODE insert_front(NODE head, int data){
    // 1st create newnode then you  will insert na
    NODE newnode=create_node(data);  // allocate a new node
    newnode->next=head;        // link new_node to the old head
    return newnode;            // return new_node as the new head
}


// insertion at end
NODE insert_end(NODE head,int data){
    NODE newnode=create_node(data);
    if(head==NULL){
        return newnode;
    }

    NODE temp=head;
    // here we done(temp->next!=NULL) beacuse here we dont want data here so we took temp->next!=NULL
    while(temp->next!=NULL){
        temp=temp->next;
    }
    temp->next=newnode;
    return head;
}


// insert at position
NODE insert_position(NODE head, int data, int pos){
    // If the user gives a negative position, that doesn’t make sense → just return the original list unchanged.
    if(pos<0){
        printf("invalid position.\n");
        return head;
    }

    // If pos == 0, we want to insert at the beginning → call insert_front.
    // If the list is empty (head == NULL), then inserting at any position is effectively inserting at the front.
    if(pos==0 || head==NULL){
        return insert_front(head,data);
    }

    // We move temp forward until it points to the node just before the position where we want to insert.
    NODE temp=head;
    for(int i=0; i<pos-1 && temp !=NULL; i++)
    {
        temp=temp->next;
    }

    // If we reached NULL before finding the right spot, it means the position is beyond the current list length → insertion not possible.
    if(temp==NULL){
        printf("position out of range.\n");
        return head;
    }

    // Create a new node with the given data.
    // Link it into the list:
    // new_node->next points to what temp was previously pointing to.
    // temp->next now points to new_node.
    NODE newnode=create_node(data);
    newnode->next=temp->next;
    temp->next=newnode;
    return head;
}


//deletion at first
NODE delete_first(NODE head){
    if(head==NULL){
        printf("list is empty. \n");
        return NULL;
    }
    NODE temp = head;
    head=head->next;
    printf("Delete :%d\n", temp->data);
    free(temp);
    return head;

}


// delete last
NODE delete_last(NODE head){
    // if no element in the llist
    if(head == NULL){
        printf("list is empty.\n");
        return NULL;
    }

    // if there is only one element in the list
    if(head->next=NULL){
        printf("deleted :%d\n", head->data);
        free(head);
        return NULL;
    }

    // if there is more than one element in the list
    NODE temp=head;

    // why we are doing (temp->next->next) inside the while loop
    // because for the first node we are deleting above only. now we will start from 2nd node only
    while(temp->next->next!=NULL){
        temp=temp->next;
    }
    printf("Deleted: %d\n",temp->next->data);
    free(temp->next);
    temp->next=NULL;
    return head;
}


int main(){
    NODE head=NULL;
    int choice,data,pos;

    while(1){
        printf("\n======== LINKED LIST MENU =======");
        printf("\n1. Insert at front");
        printf("\n2. Insert at end");
        printf("\n3. Insert at position");
        printf("\n4. delete first node");
        printf("\n5. delete last node");

        printf("\n6. Display list");
        printf("\n7. Exit");

        printf("\nEnter your choice: ");
        scanf("%d",&choice);

        switch(choice){
            case 1:
                
        }

    }


    return 0;
}