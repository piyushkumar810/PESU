#include<stdio.h>
#include<stdlib.h>
int main()
{
    // using calloc
    int *ptr=(int *)calloc(5,sizeof(int));
    if(ptr==NULL){
        printf("Memory allocation failed!\n");
        return 1;
    }
    int i;
    // if you comment this value entering part then you will see by default initialized values calloc have is (0 0 0 0 0) 
    printf("enter the values : ");
    for(i=0; i<5; i++)
    {
        scanf("%d ",(ptr+i));
    }

    printf("the entered values are : ");
    for(i=0; i<5; i++)
    {
        printf("%d ",*(ptr+i));
    }
    free(ptr);
    return 0;
}