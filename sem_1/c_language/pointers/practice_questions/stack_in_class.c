#include<stdio.h>
#define max 5

typedef struct stackADT{
    int stk[max];
    int top;
}*stack;

// int is_full(stack mystack);
// int is_empty(stack mystack);

int is_full(stack mystack){
    return (mystack->top==max-1) ? 1:0;
}

int is_empty(stack mystack){
    return (mystack->top== -1) ? 1:0;
}

void push(stack mystack){
    int element;
    if(is_full(mystack)){
        printf("\nstack full\n");
    }
    else{
        printf("\nenter the element: ");
        scanf("%d", &element);
        mystack->stk[++(mystack->top)]=element;
    }
}

void pop(stack mystack){
    if(is_empty(mystack)){
        printf("\n\tstack empty: ");
    }
    else{
        printf("\n\tpopped element is: %d",mystack->stk[(mystack->top)--]);
    }
}

void peek(stack mystack){
    if(is_empty(mystack)){
        printf("\n\tstack empty: ");
    }
    else{
        printf("\n\ttop element is: %d", mystack->stk[mystack->top]);
    }
}

void display(stack mystack){
    if(is_empty(mystack)){
        printf("\n\tstack empty: ");
    }
    else{
        printf("\nStack elements (top to bottom): ");
        for(int i = mystack->top; i >= 0; i--){
            printf("%d ", mystack->stk[i]);
        }
    }
}

int main(){
    struct stackADT s;
    s.top = -1;
    int choice;

    while(1){
        printf("\n\n1. Push\n2. Pop\n3. Peek\n4. Display\n5. Exit");
        printf("\nEnter your choice: ");
        scanf("%d", &choice);

        switch(choice){
            case 1: push(&s); break;
            case 2: pop(&s); break;
            case 3: peek(&s); break;
            case 4: display(&s); break;
            case 5: return 0;
            default: printf("\nInvalid choice");
        }
    }
}

