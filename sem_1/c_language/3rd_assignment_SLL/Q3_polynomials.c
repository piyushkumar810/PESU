/*
Write a C Program to do the following 

Addition of Polynomials: Implement a function that adds two polynomials represented as linked lists, where each node contains a coefficient and a degree.
□ Hint: Traverse both lists simultaneously, summing the coefficients of terms with the same degree. Add the resulting terms to a new polynomial linked list.

typedef struct mynode {
      int data; 
      structure dynode *link;
} *NODE;
*/

#include <stdio.h>
#include <stdlib.h>

// Define node structure
typedef struct mynode {
    int coeff;
    int degree;
    struct mynode *link;
} *NODE;

// Function to create a new node
NODE create_node(int coeff, int degree) {
    NODE temp = (NODE)malloc(sizeof(struct mynode));
    if (temp == NULL) {
        printf("Memory allocation failed!\n");
        exit(1);
    }
    temp->coeff = coeff;
    temp->degree = degree;
    temp->link = NULL;
    return temp;
}

// Function to add two polynomials
NODE add_polynomials(NODE p1, NODE p2) {
    NODE result = NULL, tail = NULL;

    while (p1 != NULL && p2 != NULL) {
        NODE temp;
        if (p1->degree == p2->degree) {
            temp = create_node(p1->coeff + p2->coeff, p1->degree);
            p1 = p1->link;
            p2 = p2->link;
        } else if (p1->degree > p2->degree) {
            temp = create_node(p1->coeff, p1->degree);
            p1 = p1->link;
        } else {
            temp = create_node(p2->coeff, p2->degree);
            p2 = p2->link;
        }

        if (result == NULL)
            result = tail = temp;
        else {
            tail->link = temp;
            tail = temp;
        }
    }

    // Add remaining terms
    while (p1 != NULL) {
        NODE temp = create_node(p1->coeff, p1->degree);
        tail->link = temp;
        tail = temp;
        p1 = p1->link;
    }

    while (p2 != NULL) {
        NODE temp = create_node(p2->coeff, p2->degree);
        tail->link = temp;
        tail = temp;
        p2 = p2->link;
    }

    return result;
}

// Function to display a polynomial
void display_polynomial(NODE head) {
    if (head == NULL) {
        printf("0");
        return;
    }

    NODE temp = head;
    while (temp != NULL) {
        printf("%dx^%d", temp->coeff, temp->degree);
        if (temp->link != NULL && temp->link->coeff >= 0)
            printf(" + ");
        temp = temp->link;
    }
    printf("\n");
}

// Main function
int main() {
    NODE p1 = NULL, p2 = NULL, sum = NULL;

    // Create first polynomial: 5x^3 + 4x^2 + 2x + 1
    p1 = create_node(5, 3);
    p1->link = create_node(4, 2);
    p1->link->link = create_node(2, 1);
    p1->link->link->link = create_node(1, 0);

    // Create second polynomial: 3x^3 + x^2 + 9
    p2 = create_node(3, 3);
    p2->link = create_node(1, 2);
    p2->link->link = create_node(9, 0);

    printf("Polynomial 1: ");
    display_polynomial(p1);

    printf("Polynomial 2: ");
    display_polynomial(p2);

    // Add both polynomials
    sum = add_polynomials(p1, p2);

    printf("Sum: ");
    display_polynomial(sum);

    return 0;
}
