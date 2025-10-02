#include <stdio.h>
int main() {
    int arr[3] = {5,10,15};
    int *p = arr;
    printf("%d\n", *++p);
    return 0;
}
/*
Explanation:
++p → pointer moves from arr[0] to arr[1].
So *p = 10.
*/