#include<stdio.h>
#include<stdlib.h>
//define the Node structure

typedef struct Node{
    int data;
    struct Node* link; 
}*NODE;

NODE create_node(int data)
{
    NODE temp=(NODE) malloc(sizeof(struct Node));
    if(temp !=NULL)
    {
        temp->data=data;
        temp->link=NULL;
    }
    else{
        printf("\n\tUnable to create a Node");
}
        return temp;

}
void Display(NODE head)
{
    if(head == NULL)
    printf("Empty List");
    else{
        printf("\n HEAD->");
        for(NODE temp=head; temp !=NULL; temp=temp->link)
        printf("%d->",temp->data);
        printf("NULL \n");
    }
}

NODE ins_front(NODE head,int data)
{
    NODE new_Node=create_node(data);
    if(new_Node !=NULL)
    {
        new_Node->link=head;
        head=new_Node;
    }
    return new_Node;
}

NODE ins_last(NODE head, int data)
{
    NODE temp, new_Node=create_node(data);
    if(new_Node !=NULL)
    {
        if(head==NULL)
            return new_Node;
        for(temp=head; temp->link !=NULL; temp=temp->link);
        temp->link=new_Node;
    }
        return head;
}

//14-10-25 in class

NODE del_last(NODE Head)
    {
    if(Head==NULL){
        printf("\n\t\t Empty List");
        return NULL;
        }   
    if(Head ->link==NULL) {
        printf("\n\t Deleted NODE %d", Head->data);
        free(Head);
        return NULL;
    }
    NODE curr=Head;
    while(curr->link->link !=NULL)
        curr=curr->link;

    printf("\n\t Deleted NODE %d",curr->link->data);
    free(curr->link);
    curr->link=NULL;
    return Head;
}

NODE insert_position (NODE Head, int data, int pos)
{
    NODE curr=Head, new_Node;
    int i;

    new_Node = create_node(data);  //create Node first
    if(new_Node==NULL)
        return Head;

        //insert at the begining or into an empty list
    if(pos==0 || Head== NULL){
        new_Node->link=Head;
        return new_Node;
    }

    for(i=0;i<pos-1 && curr !=NULL;i++){
    curr=curr->link;
}
        if(curr == NULL){
            printf("out of Range. Not inserted.\n");
            free(new_Node);
            return Head;
        }
        //insert the node
            new_Node->link = curr->link;
            curr->link =new_Node;
    
        return Head;
}

//15-10-25

NODE insert_in_sorted_list(NODE Head, int data)
{
    NODE curr = Head,new_node= create_node(data);
    if(new_node ==NULL)
        return Head;

    if(Head==NULL || Head->data >=data)
    {
        new_node->link=Head;
        return new_node;
    }

    while(curr->link !=NULL && curr->link->data <data)
        curr=curr->link;

        new_node->link=curr->link;
        curr->link=new_node;
        return Head;
}

NODE delete_position(NODE Head, int pos)
{
    if(Head==NULL){
        printf("\n\t\tEmpty List. Cannot delete.");
        return NULL;
    }
    if(pos==0)
    {
        NODE temp=Head;
        Head=Head->link;
        printf("\n\tDeleted Node %d", temp->data);
        free(temp);
        return(Head);
    }
    NODE curr=Head;
    for(int i=0; curr->link !=NULL && i<pos-1;i++)
        curr=curr->link;

    if(curr->link==NULL)
    {
        printf("\n\tOut of range, Node not found.");
        return Head;
    }
    NODE temp=curr->link;
    curr->link=temp->link;
    printf("\n\tDeleted Node %d",temp->data);
    free(temp);
    return Head;
}

NODE search_and_return_previous(NODE Head, int key)
{
    if(Head==NULL || Head-> data== key)
        return NULL;

    NODE curr= Head;
    while(curr->link !=NULL && curr->link->data !=key);
    curr=curr->link;

    if(curr->link==NULL) 
        return NULL;
    else
        return curr;
}

NODE del_front(NODE Head)
{
    NODE temp;
    if(Head==NULL){
        printf("\n\t\t Empty list");
    }
    else{
        temp=Head;
        Head=Head->link;
        printf("\n deliting node %d", temp-> data);
        free(Head);
    }
    return NULL;
}

int main()
{
    NODE head=create_node(20);
    Display(head);

    head=ins_front(head,10);  // insert at front
    Display(head);

    head=ins_last(head,80);  //insert at front
    Display(head);

    head=del_last(head);  //del at last
    Display(head);

    // head=insert_position(head,60,2);
    // Display(head);

    head=insert_in_sorted_list(head,70);
    Display(head);

    head=delete_position(head,10);
    Display(head);

    return 0;
}