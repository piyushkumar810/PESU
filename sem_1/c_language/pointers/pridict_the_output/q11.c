#include <stdio.h>
int main() {
    int x = 5;
    int *p = &x;
    printf("%d %d\n", *p, *(&x));
    return 0;
}
/*
Explanation:
Both *p and *(&x) give value of x.
So output = 5 5.
*/