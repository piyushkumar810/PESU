#include<stdio.h>
#include<conio.h>

// define node as pointer to struct node
typedef struct Node{
    int coeff;
    int pow;
    struct Node* next;
}*Node;

Node create_node(int c, int p)
{
    Node newNode=(Node)malloc(sizeof(struct Node));
    if(!newNode){
        printf("memory allocation failed \n");
        exit(1);
    }
    newNode->coeff=c;
    newNode->pow=p;
    newNode->next=NULL;
    return newNode;
}

int main(){
// 1st polynomial: 5x^2+4x^1+2x^0
Node head1=create_node(5,2);
head1->next=create_node(4,1);
head1->next->next=create_node(2,0);

// 2st polynomial: 5x^1+5x^0
Node head2=create_node(-5,1);
head2->next=create_node(-5,0);

Node head=addPolynomial(head1,head2);

return 0;
}