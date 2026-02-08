#include <stdio.h>
#include <stdlib.h>

/*
    Each node of the polynomial contains:
    coeff  -> coefficient of the term
    power  -> power (exponent) of x
    next   -> link to next term
*/
typedef struct node {
    int coeff;
    int power;
    struct node *next;
} *POLY;

/*
    Function: create_node
    Purpose : Dynamically creates a polynomial node
*/
POLY create_node(int coeff, int power) {
    POLY new_node = (POLY)malloc(sizeof(struct node));

    // Check whether memory is allocated successfully
    if (new_node == NULL) {
        printf("Memory allocation failed\n");
        exit(1);
    }

    // Initialize node data
    new_node->coeff = coeff;
    new_node->power = power;
    new_node->next = NULL;

    return new_node;
}

/*
    Function: insert_poly
    Purpose : Inserts a term into polynomial list
              in descending order of power.
              If same power exists, coefficients are added.
*/
POLY insert_poly(POLY head, int coeff, int power) {

    // Create new polynomial term
    POLY new_node = create_node(coeff, power);

    /*
        Case 1:
        If list is empty OR power is greater than head power,
        insert node at the beginning.
    */
    if (head == NULL || power > head->power) {
        new_node->next = head;
        return new_node;
    }

    POLY temp = head;

    /*
        Case 2:
        If head node has the same power,
        add coefficients and discard new node.
    */
    if (temp->power == power) {
        temp->coeff += coeff;
        free(new_node);
        return head;
    }

    /*
        Case 3:
        Traverse to find correct position
        (keep list sorted by power)
    */
    while (temp->next != NULL && temp->next->power > power) {
        temp = temp->next;
    }

    /*
        If a node with same power is found,
        add coefficients.
    */
    if (temp->next != NULL && temp->next->power == power) {
        temp->next->coeff += coeff;
        free(new_node);
    }
    /*
        Otherwise, insert node in proper position
    */
    else {
        new_node->next = temp->next;
        temp->next = new_node;
    }

    return head;
}

/*
    Function: display
    Purpose : Displays the polynomial in standard form
*/
void display(POLY head) {

    // If polynomial is empty
    if (head == NULL) {
        printf("0\n");
        return;
    }

    POLY temp = head;

    // Traverse and print polynomial terms
    while (temp != NULL) {
        printf("%dx^%d", temp->coeff, temp->power);

        if (temp->next != NULL)
            printf(" + ");

        temp = temp->next;
    }
    printf("\n");
}

/*
    Function: add_polynomials
    Purpose : Adds two polynomials and
              stores result in a new polynomial list
*/
POLY add_polynomials(POLY p1, POLY p2) {
    POLY result = NULL;

    // Insert all terms of first polynomial
    while (p1 != NULL) {
        result = insert_poly(result, p1->coeff, p1->power);
        p1 = p1->next;
    }

    // Insert all terms of second polynomial
    while (p2 != NULL) {
        result = insert_poly(result, p2->coeff, p2->power);
        p2 = p2->next;
    }

    return result;
}

/*
    Main Function
*/
int main() {
    POLY P1 = NULL, P2 = NULL, P3 = NULL;

    /*
        Polynomial 1:
        5x^3 + 4x^2 + 2
    */
    P1 = insert_poly(P1, 5, 3);
    P1 = insert_poly(P1, 4, 2);
    P1 = insert_poly(P1, 2, 0);

    /*
        Polynomial 2:
        3x^3 + 2x^1 + 1
    */
    P2 = insert_poly(P2, 3, 3);
    P2 = insert_poly(P2, 2, 1);
    P2 = insert_poly(P2, 1, 0);

    // Display polynomials
    printf("Polynomial 1: ");
    display(P1);

    printf("Polynomial 2: ");
    display(P2);

    // Add polynomials
    P3 = add_polynomials(P1, P2);

    // Display result
    printf("Sum Polynomial: ");
    display(P3);

    return 0;
}
