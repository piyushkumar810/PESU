#include<stdio.h>
#include<stdlib.h>

// creating the structure of dll
typedef struct node{
    struct node *prev;
    int data;
    struct node *next;
}*NODE;

// creating node
void create_node(int data){
    NODE newnode=(NODE)malloc(sizeof(struct node));
    
}