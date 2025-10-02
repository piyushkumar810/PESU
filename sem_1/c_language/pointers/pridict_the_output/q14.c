#include <stdio.h>
int main() {
    int arr[] = {1,2,3,4};
    int *p = arr;
    printf("%d\n", *p);
    ++*p;
    printf("%d\n", arr[0]);
    return 0;
}
/*
Explanation:
++*p → increment value at pointer.
So arr[0] = 2.
Output = 2.
*/