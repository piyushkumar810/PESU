/*
 ■ Objective: Create a program that manipulates a 2-dimensional array.
 ■ Instructions:
 □ Declare and initialize a 2-dimensional array (e.g., a 3x3 matrix).
 □ Write a function to calculate the sum of the elements of the matrix and return the result.
 □ Print the sum.
 ■ Sample Output:
 Sum of the matrix elements: 45
*/

#include <stdio.h>

// Function to calculate the sum of all elements in a 3x3 matrix
int calculateSum(int arr[3][3]) {
    int sum = 0;
    int i, j;

    for (i = 0; i < 3; i++) {
        for (j = 0; j < 3; j++) {
            sum += arr[i][j];   // same as sum = sum + arr[i][j];
        }
    }
    return sum; // return the total sum to main()
}

int main() {
    int arr[3][3] = {
        {7, 3, 5},
        {8, 6, 1},
        {4, 4, 7}
    };

    int total = calculateSum(arr);  // call the function
    printf("Sum of the matrix elements: %d\n", total);

    return 0;
}
