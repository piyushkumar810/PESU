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
    
    // if(head==NULL){
    //     newnode=head;
    //     return newnode;
    // }


    // 1st create newnode then you  will insert na
    NODE newnode=create_node(data);  // allocate a new node
    newnode->next=head;        // link new_node to the old head    //Works for both empty and non-empty list no need for creating if condition above
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
    return head;   //here you can think to (return newnode) but it is incorrect i have to return full head not only newnode
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
    if(head->next==NULL){
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

// delete at position
NODE delete_position(NODE head, int pos){
    if(head == NULL){
        printf("List is empty\n");
        return NULL;
    }

    if(pos == 0)
        return delete_first(head);

    NODE temp = head;
    for(int i = 0; i < pos - 1 && temp->next != NULL; i++)
        temp = temp->next;

    if(temp->next == NULL){
        printf("Position out of range\n");
        return head;
    }

    NODE del = temp->next;
    temp->next = del->next;
    free(del);
    return head;
}

// delete by value
NODE delete_value(NODE head, int value){
    if(head == NULL)
        return NULL;

    if(head->data == value)
        return delete_first(head);

    NODE temp = head;
    while(temp->next != NULL && temp->next->data != value)
        temp = temp->next;

    if(temp->next == NULL){
        printf("Value not found\n");
        return head;
    }

    NODE del = temp->next;
    temp->next = del->next;
    free(del);
    return head;
}

// count nodes
int count_nodes(NODE head){
    int count = 0;
    while(head != NULL){
        count++;
        head = head->next;
    }
    return count;
}

// search value
void search_value(NODE head, int value){
    int pos = 0;
    while(head != NULL){
        if(head->data == value){
            printf("Value found at position %d\n", pos);
            return;
        }
        pos++;
        head = head->next;
    }
    printf("Value not found\n");
}

// reverse linked list
NODE reverse_list(NODE head){
    NODE prev = NULL, curr = head, next = NULL;
    while(curr != NULL){
        next = curr->next;
        curr->next = prev;
        prev = curr;
        curr = next;
    }
    return prev;
}

// sort linked list (bubble sort)
NODE sort_list(NODE head){
    if(head == NULL)
        return NULL;

    for(NODE i = head; i->next != NULL; i = i->next){
        for(NODE j = i->next; j != NULL; j = j->next){
            if(i->data > j->data){
                int temp = i->data;
                i->data = j->data;
                j->data = temp;
            }
        }
    }
    return head;
}

// merge two linked lists
NODE merge_lists(NODE h1, NODE h2){
    if(h1 == NULL) return h2;
    if(h2 == NULL) return h1;

    NODE temp = h1;
    while(temp->next != NULL)
        temp = temp->next;

    temp->next = h2;
    return h1;
}

// detect loop using Floyd’s algorithm
void detect_loop(NODE head){
    NODE slow = head, fast = head;
    while(fast != NULL && fast->next != NULL){
        slow = slow->next;
        fast = fast->next->next;
        if(slow == fast){
            printf("Loop detected\n");
            return;
        }
    }
    printf("No loop detected\n");
}

// middle element using slow-fast pointer
void middle_element(NODE head){
    if(head == NULL)
        return;

    NODE slow = head, fast = head;
    while(fast != NULL && fast->next != NULL){
        slow = slow->next;
        fast = fast->next->next;
    }
    printf("Middle element: %d\n", slow->data);
}


int main(){
    NODE head = NULL;
    NODE head2 = NULL;   // for merge operation
    int choice, data, pos;

    while(1){

        printf("\n=========== LINKED LIST MENU ===========\n");
        printf("1. Insert at front\n");
        printf("2. Insert at end\n");
        printf("3. Insert at position\n");
        printf("4. Delete first node\n");
        printf("5. Delete last node\n");
        printf("6. Delete at position\n");
        printf("7. Delete by value\n");
        printf("8. Count nodes\n");
        printf("9. Search value\n");
        printf("10. Display list\n");
        printf("11. Reverse linked list\n");
        printf("12. Sort linked list\n");
        printf("13. Merge two linked lists\n");
        printf("14. Detect loop in list\n");
        printf("15. Find middle element\n");
        printf("0. Exit\n");

        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch(choice){

            case 1:
                printf("Enter data: ");
                scanf("%d", &data);
                head = insert_front(head, data);
                break;

            case 2:
                printf("Enter data: ");
                scanf("%d", &data);
                head = insert_end(head, data);
                break;

            case 3:
                printf("Enter data: ");
                scanf("%d", &data);
                printf("Enter position: ");
                scanf("%d", &pos);
                head = insert_position(head, data, pos);
                break;

            case 4:
                head = delete_first(head);
                break;

            case 5:
                head = delete_last(head);
                break;

            case 6:
                printf("Enter position: ");
                scanf("%d", &pos);
                head = delete_position(head, pos);
                break;

            case 7:
                printf("Enter value to delete: ");
                scanf("%d", &data);
                head = delete_value(head, data);
                break;

            case 8:
                printf("Total nodes = %d\n", count_nodes(head));
                break;

            case 9:
                printf("Enter value to search: ");
                scanf("%d", &data);
                search_value(head, data);
                break;

            case 10:
                diaplay(head);
                break;

            case 11:
                head = reverse_list(head);
                printf("Linked list reversed successfully.\n");
                break;

            case 12:
                head = sort_list(head);
                printf("Linked list sorted successfully.\n");
                break;

            case 13:
                printf("Enter elements for second list (-1 to stop):\n");
                while(1){
                    scanf("%d", &data);
                    if(data == -1)
                        break;
                    head2 = insert_end(head2, data);
                }
                head = merge_lists(head, head2);
                printf("Two linked lists merged successfully.\n");
                break;

            case 14:
                detect_loop(head);
                break;

            case 15:
                middle_element(head);
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