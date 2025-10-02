#include <stdio.h>
int main() {
    int arr[5] = {10,20,30,40,50};
    int *p = arr;
    printf("%d\n", *(p++));
    printf("%d\n", *p);
    return 0;
}
/*
Explanation:

*(p++) → prints current value 10, then increments pointer.

Now p points to 20.
So second print is 20.
*/