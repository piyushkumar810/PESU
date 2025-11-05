#include<stdio.h>
#define N 5
int stack[N];
int top=-1;

void push()
{
    int n;
    printf("enter the element : ");
    scanf("%d",&n);
    if(top==N-1){
    printf("stack overflow");
    } 
    else{
    top++;
    stack[top]=n;
   }
}

void display() {
    if(top == -1) {
        printf("No value is there in your stack\n");
    } else {
        printf("Elements inside the stack are: ");
        for(int i = top; i >= 0; i--) {
            printf("%d ", stack[i]);  // <-- added a space here
        }
        printf("\n");  // newline after printing all elements
    }
}


void pop(){
    int items;
    
    if(top==-1){
        printf("stack underflow");
    }
    else{
        items=stack[top];
        top--;
        printf("your poped item is %d ",items);
    }
}

int main(){
    while(1){
    printf("enter \n1 for push  \n2 for pop  \n3 for display  \n4 for exit \n ");
    int ch;
    scanf("%d",&ch);

    switch(ch){
        case 1: 
        push();
        break;

        case 2:
        pop();
        break;

        case 3:
        display();
        break;

        case 4:
        return 0;

        default:
        printf("Wrong choice!\n");

    }
}
}