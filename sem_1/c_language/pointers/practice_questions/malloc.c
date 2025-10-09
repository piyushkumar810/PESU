#include <stdio.h>
#include <stdlib.h>

int main() {
    int *arr = (int *) malloc(5 * sizeof(int)); // allocate memory for 5 integers

    if (arr == NULL) {
        printf("Memory allocation failed using malloc\n");
        return 1;
    }

    // assigning values
    for (int i = 0; i < 5; i++) {
        arr[i] = i + 1;
    }

    // printing values
    for (int i = 0; i < 5; i++) {
        printf("%d ", arr[i]);
    }

    // free allocated memory
    free(arr);

    return 0;
}
