// #include <stdio.h>
// #include <stdlib.h>

// #define MAX 10

// typedef struct StackADT {
//     int stk[MAX];
//     int TOP;
// } *Stack;

// int IsFull(Stack MyStack) {
//     return (MyStack->TOP == MAX - 1 ? 1 : 0);
// }

// int IsEmpty(Stack MyStack) {
//     return (MyStack->TOP == -1 ? 1 : 0);
// }

// void display(Stack MyStack) {
//     int i;
//     if (IsEmpty(MyStack))
//         printf("\n\t\tEmpty Stack");
//     else {
//         printf("\n\t TOP -> | ");
//         for (i = MyStack->TOP; i >= 0; i--)
//             printf("%d | ", MyStack->stk[i]);
//     }
// }

// void push(Stack MyStack) {
//     int element;
//     if (IsFull(MyStack))
//         printf("\n\t\tStack Overflow");
//     else {
//         printf("\n\t\tEnter the Element: ");
//         scanf("%d", &element);
//         MyStack->stk[++MyStack->TOP] = element;
//         display(MyStack);
//     }
// }

// void pop(Stack MyStack) {
//     if (IsEmpty(MyStack))
//         printf("\n\t\tStack Underflow !!!");
//     else {
//         printf("\n\t\t%d is Popped", MyStack->stk[MyStack->TOP--]);
//         display(MyStack);
//     }
// }

// int main() {
//     Stack MyStack = (Stack) malloc(sizeof(struct StackADT));
//     MyStack->TOP = -1;

//     int choice;

//     while (1) {
//         printf("\n\n1.Push\n2.Pop\n3.Display\n4.Exit\nEnter choice: ");
//         scanf("%d", &choice);

//         switch (choice) {
//             case 1: push(MyStack); break;
//             case 2: pop(MyStack); break;
//             case 3: display(MyStack); break;
//             case 4: exit(0);
//             default: printf("\nInvalid Choice");
//         }
//     }

//     return 0;
// }



//-------------------------------------- recap

#include<stdio.h>
#include<stdlib.h>

#define MAX 10

typedef struct stackADT{
    int stk[MAX];
    int top;
}*stack;

int isFULL(stack mystack){
    if(mystack->top==MAX-1){
        printf("your stack is full\n");
    }
    else{
        printf("\nyour stack have space\n");
    }
}

int isEMPTY(stack mystack)
{
    return (mystack->top==-1 ? 1:0);
}

void display(stack mystack){
    int i;
    if(isEMPTY(mystack))
    {
        printf("my stack is empty\n");
    }
    else{
        printf("\nmy stack is: ");
        for(i=mystack->top; i>=0;i--){
            printf("\t%d", mystack->stk[i]);
        }
    }
}

void push(stack mystack){
    int element;

    if(isFULL(mystack)){
        printf("stack overflow\n");
    }
    else{
        printf("\n emter the element : ");
        scanf("\t%d",&element);
        mystack->stk[++mystack->top]=element;
        display(mystack);
    }
}

void pop(stack mystack){
    if(isEMPTY(mystack)){
        printf("stack underflow\n");
    }

    else{
        printf("\nyour poped element is :%d", mystack->stk[mystack->top--]);
        // display(mystack);
    }
}

void peek(stack mystack){
    if(isEMPTY(mystack)){
        printf("my stack is empty\n");
    }
    else{
        printf("\nmy top element is %d", mystack->stk[mystack->top]);
    }
}

int main()
{

    stack mystack=(stack)malloc(sizeof(struct stackADT));
    mystack->top=-1;

    push(mystack);
    push(mystack);
    push(mystack);

    display(mystack);

    peek(mystack);

    pop(mystack);
    display(mystack);

    return 0;
}