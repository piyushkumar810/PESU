#include<stdio.h>
#include<stdlib.h>
int main()
{
    // using malloc
    int *arr=(int *)malloc(5 * sizeof(int));
    if(arr==NULL)
    {
        printf("memory allocation falied using malloc \n");
        return 1;
    }
    // initiallize and print the malloc
    for(int i=0;i<5;i++)
    arr[i]=(i+1)*2;
    printf("array allocated using malloc ");
    for(int i=0;i<5;i++)
    {
        printf("%d ", arr[i]);
    }
    printf("\n");

    // using calloc
    int *arr2=(int *)malloc(5 * sizeof(int));
    if(arr2==NULL)
    {
        printf("memory allocation falied using calloc \n");
        free(arr);
        return 1;
    }
    // // initiallize and print the malloc
    // for(int i=0;i<5;i++)
    // arr[i]=(i+1)*2;
    // printf("array allocated using malloc ");
    // for(int i=0;i<5;i++)
    // {
    //     printf("%d ", arr[i]);
    // }
    printf("\n");
    return 0;
}