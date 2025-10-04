#include <stdio.h>
int main() {
    int x = 5;
    int *p1 = &x;
    int **p2 = &p1;
    int ***p3 = &p2;
    ***p3 = ***p3 + 50;
    printf("%d\n", x);
    return 0;
}
/*
Explanation:
***p3 → value of x.
So x = 5+50 = 55.
*/