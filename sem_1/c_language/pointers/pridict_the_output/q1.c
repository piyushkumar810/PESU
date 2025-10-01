#include <stdio.h>
int main() {
    int a = 10;
    int *p = &a;
    printf("%d\n", *p);
    return 0;
}

// p stores the address of a, so *p means "value at that address". Hence output is 10.