#include <stdio.h>
int main() {
    int arr[4] = {1,2,3,4};
    int *p = arr;
    printf("%d\n", *(p++) + *p);
    return 0;
}
/*
Explanation:
*(p++) → take value 1, then increment pointer.
Now *p = 2.
So sum = 1+2 = 3.
*/