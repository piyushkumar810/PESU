#include <stdio.h>
int main() {
    int a = 5, b = 10;
    int *p = &a, *q = &b;
    printf("%d\n", *p + *q);
    return 0;
}
// 15