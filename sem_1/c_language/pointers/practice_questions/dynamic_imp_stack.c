#include <stdio.h>
#include <stdlib.h>

typedef struct stackADT {
    int *stk;      // pointer to dynamically allocated array
    int top;
    int capacity;  // current size of allocated array
} *stack;

// int is_full(stack mystack);
// int is_empty(stack mystack);
// void push(stack mystack);
// void pop(stack mystack);
// void peek(stack mystack);
// void display(stack mystack);

// check if stack is full
int is_full(stack mystack){
    return mystack->top == mystack->capacity - 1;
}

// check if stack is empty
int is_empty(stack mystack){
    return mystack->top == -1;
}

// push function
void push(stack mystack){
    int element;
    printf("\nEnter element to push: ");
    scanf("%d", &element);

    if(is_full(mystack)){
        // double the capacity using realloc
        mystack->capacity *= 2;
        mystack->stk = realloc(mystack->stk, mystack->capacity * sizeof(int));
        if(mystack->stk == NULL){
            printf("\nMemory reallocation failed!");
            exit(1);
        }
        printf("\nStack resized to %d\n", mystack->capacity);
    }
    mystack->stk[++(mystack->top)] = element;
}

// pop function
void pop(stack mystack){
    if(is_empty(mystack)){
        printf("\nStack empty.\n");
    } else {
        printf("\nPopped element: %d\n", mystack->stk[mystack->top--]);
    }
}

// peek function
void peek(stack mystack){
    if(is_empty(mystack)){
        printf("\nStack empty.\n");
    } else {
        printf("\nTop element: %d\n", mystack->stk[mystack->top]);
    }
}

// display function
void display(stack mystack){
    if(is_empty(mystack)){
        printf("\nStack empty.\n");
    } else {
        printf("\nStack elements (top to bottom): ");
        for(int i = mystack->top; i >= 0; i--){
            printf("%d ", mystack->stk[i]);
        }
        printf("\n");
    }
}

int main(){
    struct stackADT s;
    int choice;

    // initial setup
    s.capacity = 2; // start with capacity 2
    s.top = -1;
    s.stk = (int *)malloc(s.capacity * sizeof(int));
    if(s.stk == NULL){
        printf("Memory allocation failed\n");
        return 1;
    }

    printf("\n--- Dynamic Stack Implementation ---\n");

    while(1){
        printf("\n1. Push");
        printf("\n2. Pop");
        printf("\n3. Peek");
        printf("\n4. Display");
        printf("\n5. Exit");
        printf("\nEnter your choice: ");
        scanf("%d", &choice);

        if(choice == 1){
            push(&s);
        }
        else if(choice == 2){
            pop(&s);
        }
        else if(choice == 3){
            peek(&s);
        }
        else if(choice == 4){
            display(&s);
        }
        else if(choice == 5){
            free(s.stk);
            printf("\nExiting program.\n");
            return 0;
        }
        else{
            printf("\nInvalid choice.\n");
        }
    }
}
