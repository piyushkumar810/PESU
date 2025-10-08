/*
 ■ Objective: Write a program to demonstrate pointer arithmetic with a 1-dimensional array.
 ■ Instructions:
 □ Declare a 1-dimensional array of integers and initialize it with 5 values.
 □ Use a pointer to traverse the array and print each element using pointer arithmetic.
 ■ Sample Output:
 Array elements: 10 20 30 40 50
*/

#include <stdio.h>

int main() {
    int arr[]={10,20,30,40,50};
    int *ptr=arr;

    printf("arry elements are : ");
    for(int i=0;i<5;i++)
    {
        printf("%d ", *(ptr +i));
    }
    return 0;
}

// // just i want to check what is inside ptr and *ptr just befors traversing array
// #include <stdio.h>

// int main() {
//     int arr[5] = {10, 20, 30, 40, 50};
//     int *ptr;
//     ptr = arr;

//     printf("ptr = %p\n", ptr);            //ptr = 0x7ffde7d8b6f0 -> this is address of arr[0]
//     printf("*ptr = %d\n", *ptr);         //*ptr = 10

//     return 0;
// }


// // then how *(ptr+i) working
/*
⚙️ What happens when you do ptr + 1?

Many people think it means:

0x7ffde7d8b6f0 + 1 → 0x7ffde7d8b6f1 ❌
(That would be wrong!)

In C, pointer arithmetic is scaled by the size of the data type the pointer points to.

Since ptr is an int *, and on most systems sizeof(int) = 4 bytes,
then:

ptr + 1  ➜  0x7ffde7d8b6f0 + (1 × 4 bytes)
          ➜  0x7ffde7d8b6f4 --> and this will the address of arr[1]
*/