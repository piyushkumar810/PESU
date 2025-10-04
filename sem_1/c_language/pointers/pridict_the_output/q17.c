#include <stdio.h>
int main() {
    int arr[3] = {10,20,30};
    int *p = arr;
    *(p+1) = *(p+1) + 5;
    printf("%d\n", arr[1]);
    return 0;
}
/*
Explanation:
arr[1] = 20 → 25.
Output = 25.
*/