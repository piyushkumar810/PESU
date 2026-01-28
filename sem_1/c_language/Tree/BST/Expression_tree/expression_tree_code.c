#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

// Structure of expression tree node
struct Node {
    char data;
    struct Node *left, *right;
};

// Stack structure to store tree nodes
struct Stack {
    int top;
    struct Node* arr[50];
};

// Create a new tree node
struct Node* createNode(char value) {
    struct Node* node = (struct Node*)malloc(sizeof(struct Node));
    node->data = value;
    node->left = NULL;
    node->right = NULL;
    return node;
}

// Initialize stack
struct Stack* createStack() {
    struct Stack* s = (struct Stack*)malloc(sizeof(struct Stack));
    s->top = -1;
    return s;
}

// Push node into stack
void push(struct Stack* s, struct Node* node) {
    s->arr[++s->top] = node;
}

// Pop node from stack
struct Node* pop(struct Stack* s) {
    return s->arr[s->top--];
}

// Construct expression tree from postfix
struct Node* constructTree(char postfix[]) {
    struct Stack* s = createStack();
    struct Node *node, *right, *left;

    for (int i = 0; postfix[i] != '\0'; i++) {

        // If operand, push to stack
        if (isalnum(postfix[i])) {
            node = createNode(postfix[i]);
            push(s, node);
        }
        // If operator
        else {
            node = createNode(postfix[i]);

            right = pop(s);
            left = pop(s);

            node->left = left;
            node->right = right;

            push(s, node);
        }
    }

    return pop(s); // root of expression tree
}

// Inorder Traversal
void inorder(struct Node* root) {
    if (root != NULL) {
        inorder(root->left);
        printf("%c ", root->data);
        inorder(root->right);
    }
}

// Preorder Traversal
void preorder(struct Node* root) {
    if (root != NULL) {
        printf("%c ", root->data);
        preorder(root->left);
        preorder(root->right);
    }
}

// Postorder Traversal
void postorder(struct Node* root) {
    if (root != NULL) {
        postorder(root->left);
        postorder(root->right);
        printf("%c ", root->data);
    }
}

// Main function
int main() {
    char postfix[] = "ABC*+";
    struct Node* root = constructTree(postfix);

    printf("Inorder Traversal: ");
    inorder(root);

    printf("\nPreorder Traversal: ");
    preorder(root);

    printf("\nPostorder Traversal: ");
    postorder(root);

    return 0;
}
