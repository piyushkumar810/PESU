#include <stdio.h>
int main() {
    int arr[3] = {1,2,3};
    int *p = arr;
    printf("%d %d\n", *p, *(p+2));
    return 0;
}
/*Explanation:
In arrays, arr is equivalent to &arr[0].
So *p = arr[0] = 1, and *(p+2) = arr[2] = 3.
Output: 1 3.
*/