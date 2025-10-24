// ----------------------------------- DLL(double linked list)--------------------------------

#include<stdio.h>
#include<stdlib.h>

typedef struct node{
    int data;
    struct Node *next, *prev;
}*NODE;

// create a new node
NODE creat_node(int data){
    NODE newnode=(NODE) malloc(sizeof(struct node));
    if(newnode==NULL)
    {
        print("\nout of memory");
    }
    else{
        newnode->data=data;
        newnode->prev=NULL;
        newnode->next=NULL;
    }
    return newnode;
}



// int main()
// {

//     return 0;
// }