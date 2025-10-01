#include <stdio.h>
int main() {
    int a = 5, b = 6;
    int *p = &a;
    p = &b;
    printf("%d\n", *p);
    return 0;
}

/* Initially p points to a, then it is reassigned to &b.
    So *p = b = 6.
*/