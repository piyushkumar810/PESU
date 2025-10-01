#include <stdio.h>
int main() {
    int a = 7;
    int *p = &a;
    int **q = &p;
    printf("%d\n", **q);
    return 0;
}
// q is pointer to pointer. **q = value of a. So output = 7.