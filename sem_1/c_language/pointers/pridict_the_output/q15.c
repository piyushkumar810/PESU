#include <stdio.h>
int main() {
    int a = 5;
    int *p = &a;
    int **q = &p;
    **q = **q + 10;
    printf("%d\n", a);
    return 0;
}
// **q modifies a. So a = 5+10 = 15.