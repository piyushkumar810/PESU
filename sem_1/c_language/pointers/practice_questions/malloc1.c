// ------------------------ malloc practice

#include <stdio.h>
#include <stdlib.h>

int main() {
    int n;
    printf("Enter total number of values: ");
    scanf("%d", &n);  // removed space

    int *ptr = (int *)malloc(n * sizeof(int));
    if (ptr == NULL) {
        printf("Memory allocation failed!\n");
        return 1;
    }

    printf("Enter the values: ");
    for (int i = 0; i < n; i++) {
        scanf("%d", (ptr + i));  // removed space
    }

    printf("The entered values are: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", *(ptr + i));
    }

    free(ptr);
    return 0;
}
