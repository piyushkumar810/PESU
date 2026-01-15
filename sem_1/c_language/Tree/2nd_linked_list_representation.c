// 2️⃣ LINKED LIST REPRESENTATION OF TREE

/*
🧠 IDEA
Each node is a structure

Contains:
Data
Pointer(s) to children

🌳 Binary Tree Node Structure
struct Node {
    int data;
    struct Node *left;
    struct Node *right;
};

🧠 Picture:
[data | left | right]
*/

// ✅ LINKED LIST REPRESENTATION – FULL C CODE
#include <stdio.h>
#include <stdlib.h>

// Define tree node
struct Node {
    int data;
    struct Node *left;
    struct Node *right;
};

// Create a new node
struct Node* createNode(int value)
{
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = value;
    newNode->left = NULL;
    newNode->right = NULL;
    return newNode;
}

int main()
{
    // Creating tree manually
    struct Node* root = createNode(1);
    root->left = createNode(2);
    root->right = createNode(3);
    root->left->left = createNode(4);
    root->left->right = createNode(5);

    printf("Root = %d\n", root->data);
    printf("Left child of root = %d\n", root->left->data);
    printf("Right child of root = %d\n", root->right->data);

    return 0;
}

/*
🧠 VISUAL MAPPING
        1
       / \
      2   3
     / \
    4   5


Each arrow = pointer

✔ Advantages
No memory wastage
Dynamic size
Best for all tree types

❌ Disadvantages
Extra memory for pointers
Slightly complex
*/