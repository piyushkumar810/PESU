#include <stdio.h>
int main() {
    int x = 100;
    int *ptr = &x;
    *ptr = *ptr + 50;
    printf("%d\n", x);
    return 0;
}
// *ptr accesses x. Updating *ptr updates x. So x = 150.