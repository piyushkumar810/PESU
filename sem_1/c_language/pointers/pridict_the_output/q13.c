#include <stdio.h>
int main() {
    int a = 100, b = 200;
    int *p = &a;
    *p = b;
    printf("%d %d\n", a, b);
    return 0;
}
/*
Explanation:
*p = b means a = 200.
So output: 200 200.
*/