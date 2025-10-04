#include <stdio.h>
int main() {
    int a = 10, b = 20;
    int *p = &a, *q = &b;
    p = q;
    printf("%d\n", *p);
    return 0;
}
/*
Explanation:
p = q → now both point to b.
So *p = 20.
*/