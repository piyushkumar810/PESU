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

#include<stdalign.h>

int addressOf1D(int arr1D[5],int baseAddress, int position)
{
    int address = baseAddress+(position*(sizeof(int)));
    return address;
}

int main()
{
    int arr[5]={1,2,3,4,5};
    
}