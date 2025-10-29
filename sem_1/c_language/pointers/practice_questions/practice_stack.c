// stack implementation
#include<stdio.h>
#define N 5
int stack[N];
int top=-1;

void push(){
    int n;
    printf("\nenter the value in stack : ");
    scanf("%d",&n);
    if(top==N-1){
        printf("\nstack overflow\n");
        return;
    }
    else{
        top++;
        stack[top]=n;
    }
}

void pop(){
    int item;
    if(top==-1){
        printf("\nstack underflow\n");
    }
    else{
        item=stack[top];
        top--;
        prinf("\nyour pop element is : %d",item);
    }
}

void display(){
    int i;
    if(top==-1){
        printf("\nempty stack\n");
    }
    else{
        printf("\nelement in stack are: ");
        for(i=top; i>=0;i--){
            printf("%d ", stack[i]);
        }
    }
}