#include <stdio.h>
int main() {
    int a = 5;
    int *p = &a;
    int **q = &p;
    **q = **q + 10;
    printf("%d\n", a);
    return 0;
}
