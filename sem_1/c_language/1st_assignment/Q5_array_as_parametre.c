/*
. LEVEL- 1 : Arrays as Parameters
 ■ Objective: Write a program that uses arrays as function parameters.
 ■ Instructions:
 □ Create a function that takes an array of integers and its size as parameters.
 □ The function should calculate and return the average of the elements in the array.
 □ In the main function, declare an array, initialize it, and call the average function.
 ■ Sample Output:
 Average of the array: 25.
*/

#include<stdio.h>
int findAverage(int arr[],int size)
{
    int avg;
    int sum=0;
    for(int i=0;i<size;i++)
    {
        sum=sum+arr[i];
    }
    avg=sum/size;
    return avg;
}

int main()
{
    int arr[]={10,20,30,40,50};
    int size=(sizeof(arr)/sizeof(arr[0]));
    float avg=findAverage(arr,size);
    printf("Average of the array: %.2f\n", avg); 

    return 0;
}
