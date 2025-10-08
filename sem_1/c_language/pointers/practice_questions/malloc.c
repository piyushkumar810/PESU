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
    for(int i=0;i<5;arr[i++]=i+1);
    for(int i=0;i<5;i++)
    {
        printf("%d ",arr[i]);
    }
}