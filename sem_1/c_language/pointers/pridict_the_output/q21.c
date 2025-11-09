#include <stdio.h>
int main() {
    int arr[3] = {10, 20, 30};
    int *p = arr;

    // printf("Address before increment: %p\n", p); 
    // p++;  // Move to next integer (next element in array)
    // printf("Address after increment: %p\n", p);
    // printf("Value at new address: %d\n", *p);

    printf("%d\n", p);
    printf("%d\n",*p);

    p++;

    printf("%d\n", p);
    printf("%d\n",*p);

    --p;
    printf("%d",*p);

    return 0;
}