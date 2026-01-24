#include <stdio.h>
#include <stdlib.h>

/* ---------- Structure of a Tree Node ---------- */
struct Node {
    int data;                  // value stored in node
    struct Node *left;          // pointer to left child
    struct Node *right;         // pointer to right child
};

/* ---------- Create a New Node ---------- */
struct Node* createNode(int value) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = value;
    newNode->left = NULL;
    newNode->right = NULL;
    return newNode;
}

/* ---------- Inorder Traversal (L → Root → R) ---------- */
void inorder(struct Node* root) {
    if (root == NULL)
        return;

    inorder(root->left);
    printf("%d ", root->data);
    inorder(root->right);
}

/* ---------- Preorder Traversal (Root → L → R) ---------- */
void preorder(struct Node* root) {
    if (root == NULL)
        return;

    printf("%d ", root->data);
    preorder(root->left);
    preorder(root->right);
}

/* ---------- Postorder Traversal (L → R → Root) ---------- */
void postorder(struct Node* root) {
    if (root == NULL)
        return;

    postorder(root->left);
    postorder(root->right);
    printf("%d ", root->data);
}

/* ---------- Main Function ---------- */
int main() {

    /*
           1
         /   \
        2     3
       / \   /
      4   5 6
    */

    struct Node* root = createNode(1);
    root->left = createNode(2);
    root->right = createNode(3);
    root->left->left = createNode(4);
    root->left->right = createNode(5);
    root->right->left = createNode(6);

    printf("Inorder Traversal: ");
    inorder(root);

    printf("\nPreorder Traversal: ");
    preorder(root);

    printf("\nPostorder Traversal: ");
    postorder(root);

    return 0;
}


/*
✅ PART 2: NOW LET’S UNDERSTAND EVERYTHING PROPERLY

We’ll go step by step, picturizing in your brain 🧠

🌳 What is a Binary Tree?

A binary tree is a hierarchical structure where:

Each node has at most 2 children

Called left child and right child

🔹 Tree used in the code (VERY IMPORTANT)
           1
         /   \
        2     3
       / \   /
      4   5 6


Keep this picture in your mind.
All traversals depend on how we visit nodes.

🔁 What is Tree Traversal?

Traversal = visiting every node exactly once in some order

There are 3 main ways:

Traversal	Order
Preorder	Root → Left → Right
Inorder	Left → Root → Right
Postorder	Left → Right → Root
🔹 1️⃣ INORDER TRAVERSAL
(Left → Root → Right)
Rule (say it loudly):

LEFT first → then ROOT → then RIGHT

Code logic:
inorder(root->left);
print root;
inorder(root->right);

Picturize:

Go to leftmost node

Print while coming back

Output:
4 2 5 1 6 3


📌 Important use:

In BST, inorder traversal gives sorted order

🔹 2️⃣ PREORDER TRAVERSAL
(Root → Left → Right)
Rule:

ROOT first → LEFT → RIGHT

Code logic:
print root;
preorder(root->left);
preorder(root->right);

Picturize:

Visit node as soon as you see it

Then go left, then right

Output:
1 2 4 5 3 6


📌 Used for:

Copying a tree

Expression trees (prefix)

🔹 3️⃣ POSTORDER TRAVERSAL
(Left → Right → Root)
Rule:

LEFT → RIGHT → ROOT

Code logic:
postorder(root->left);
postorder(root->right);
print root;

Picturize:

Visit children first

Visit parent last

Output:
4 5 2 6 3 1


📌 Used for:

Deleting a tree

Expression evaluation (postfix)

🧠 ONE-LINE MEMORY TRICK (EXAM GOLD)
Traversal	Trick
Preorder	Root First
Inorder	Root in Middle
Postorder	Root Last
⚠️ VERY IMPORTANT CONCEPT (RECURSION)
if (root == NULL)
    return;


Why needed?

Prevents infinite recursion

Means: no node → stop
*/