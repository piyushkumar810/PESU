// ------------------------ malloc practice

#include<stdio.h>
#include<stdlib.h>

int main(){

    int n;
    printf("enter total number of values ");
    scanf("%d", &n);

    int *ptr=(int *)malloc(n* sizeof(int));

    printf("enter the values: ");
    for(int i=0; i<n; i++)
    {
        scanf("%d", (ptr+i));
    }

    printf("the entered values are : ");
    for(int i=0; i<n; i++)
    {
        printf("%d ", *(ptr+i));
    }

    free(ptr);
    return 0;
}
























