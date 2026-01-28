#include <stdio.h>
#include <stdlib.h>

// Definition of BST Node
struct Node {
    int data;
    struct Node* left;
    struct Node* right;
};

// 🔹 Create a new node
struct Node* createNode(int value) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = value;
    newNode->left = NULL;
    newNode->right = NULL;
    return newNode;
}

// 🔹 INSERTION in BST
struct Node* insert(struct Node* root, int value) {
    // Case 1: Empty tree or correct position found
    if (root == NULL) {
        return createNode(value);
    }

    // Case 2: Go left
    if (value < root->data) {
        root->left = insert(root->left, value);
    }
    // Case 3: Go right
    else if (value > root->data) {
        root->right = insert(root->right, value);
    }

    return root;
}

// 🔹 Find minimum value node (used in deletion)
struct Node* findMin(struct Node* root) {
    while (root->left != NULL)
        root = root->left;
    return root;
}

// 🔹 DELETION in BST
struct Node* deleteNode(struct Node* root, int value) {
    if (root == NULL)
        return root;

    // Step 1: Traverse to find the node
    if (value < root->data) {
        root->left = deleteNode(root->left, value);
    }
    else if (value > root->data) {
        root->right = deleteNode(root->right, value);
    }
    else {
        // Case 1: Node with NO child
        if (root->left == NULL && root->right == NULL) {
            free(root);
            return NULL;
        }

        // Case 2: Node with ONE child
        else if (root->left == NULL) {
            struct Node* temp = root->right;
            free(root);
            return temp;
        }
        else if (root->right == NULL) {
            struct Node* temp = root->left;
            free(root);
            return temp;
        }

        // Case 3: Node with TWO children
        struct Node* temp = findMin(root->right);
        root->data = temp->data;
        root->right = deleteNode(root->right, temp->data);
    }
    return root;
}

// 🔹 Inorder Traversal
void inorder(struct Node* root) {
    if (root != NULL) {
        inorder(root->left);
        printf("%d ", root->data);
        inorder(root->right);
    }
}

// 🔹 Main Function
int main() {
    struct Node* root = NULL;

    root = insert(root, 50);
    insert(root, 30);
    insert(root, 70);
    insert(root, 20);
    insert(root, 40);
    insert(root, 60);
    insert(root, 80);

    printf("Inorder Traversal: ");
    inorder(root);

    root = deleteNode(root, 20);
    root = deleteNode(root, 30);
    root = deleteNode(root, 50);

    printf("\nAfter Deletion: ");
    inorder(root);

    return 0;
}
