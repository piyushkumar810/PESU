#include <stdio.h>
#include <ctype.h>
#include <string.h>

#define MAX 20

char stack[MAX];
int Top = -1;

// safe push
void push(char elem) {
    if (Top < MAX - 1)
        stack[++Top] = elem;
}

// safe pop
char pop() {
    if (Top >= 0)
        return stack[Top--];
    return '#';    // fallback
}

int precd(char elem) {
    switch (elem) {
        case '+':
        case '-': return 1;
        case '*':
        case '/': return 2;
        case '^': return 3;   // highest (right associative)
        case '(':
        case '#': return 0;
    }
    return -1;
}

int main() {
    char infix[MAX], postfix[MAX], ch;
    int i = 0, j = 0;

    printf("Enter the Infix Expression: ");
    scanf("%19s", infix);   // prevent overflow

    push('#');

    for (i = 0; i < strlen(infix); i++) {
        ch = infix[i];

        if (isalnum(ch)) {
            postfix[j++] = ch;
        }
        else if (ch == '(') {
            push(ch);
        }
        else if (ch == ')') {
            while (stack[Top] != '(')
                postfix[j++] = pop();
            pop();  // remove '('
        }
        else { // operator
            while ((precd(stack[Top]) > precd(ch)) ||
                  (precd(stack[Top]) == precd(ch) && ch != '^')) {
                postfix[j++] = pop();
            }
            push(ch);
        }
    }

    while (stack[Top] != '#')
        postfix[j++] = pop();

    postfix[j] = '\0';

    printf("Postfix: %s\n", postfix);

    return 0;
}