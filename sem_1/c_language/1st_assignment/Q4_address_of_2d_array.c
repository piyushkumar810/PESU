/*
 4. LEVEL- 1 : Calculating Address in Arrays
 ■ Objective: Create a program that calculates the address of a specific element in both 1-dimensional
 and 2-dimensional arrays using their respective formulas

 ■ Instructions:
    □ 1-Dimensional Array:
        ■ Declare and initialize a 1-dimensional array with 5 elements.
        ■ Write a function to calculate the address of an element using the formula:
        Address = Base Address+(i×Size of element)
        where i is the index of the element.
        ■ Print the address of a specified element.

    □ 2-Dimensional Array:
        ■ Declare and initialize a 2-dimensional array with 3 rows and 3 columns.
        ■ Write a function to calculate the address of an element using the formula for row-major order:
        Address = Base Address+[(i×Total Columns)+j]×Size of element
        where i and j represent the row and column indices of the element.
        ■ Print the address of a specified element.

 ■ Sample Output:
 Address of element at index 2 in 1D Array: 2012
 Address of element at (1, 2) in 2D Array: 3056
*/

#include <stdio.h>

// Function to calculate address in 1D array
void address_1D(int baseAddress, int index, int sizeOfElement) {
    int address = baseAddress + (index * sizeOfElement);
    printf("Address of element at index %d in 1D Array: %d\n", index, address);
}

// Function to calculate address in 2D array (Row-major order)
void address_2D(int baseAddress, int i, int j, int totalColumns, int sizeOfElement) {
    int address = baseAddress + ((i * totalColumns) + j) * sizeOfElement;
    printf("Address of element at (%d, %d) in 2D Array: %d\n", i, j, address);
}

int main() {
    // 1-Dimensional Array
    int arr1D[5] = {10, 20, 30, 40, 50};
    int baseAddress1D = 2000;           // Assume base address = 2000
    int size1D = sizeof(arr1D[0]);      // size of each element (int)
    int index1D;

    printf("Enter the index of element in 1D array (0-4): ");
    scanf("%d", &index1D);

    address_1D(baseAddress1D, index1D, size1D);

    // 2-Dimensional Array
    int arr2D[3][3] = {
        {1, 2, 3},
        {4, 5, 6},
        {7, 8, 9}
    };
    int baseAddress2D = 3000;           // Assume base address = 3000
    int totalColumns = 3;               // number of columns in the matrix
    int size2D = sizeof(arr2D[0][0]);   // size of each element (int)
    int row, col;

    printf("Enter the row and column of element in 2D array (0-2 0-2): ");
    scanf("%d %d", &row, &col);

    address_2D(baseAddress2D, row, col, totalColumns, size2D);

    return 0;
}
