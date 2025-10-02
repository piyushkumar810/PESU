#include <stdio.h>
int main() {
    int arr[] = {10,20,30,40};
    int *p = arr;
    printf("%d\n", *p + *(p+3));
    return 0;
}
/*
Explanation:
*p = arr[0] = 10,
*(p+3) = arr[3] = 40.
Sum = 50.
*/