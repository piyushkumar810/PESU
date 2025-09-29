#include<stdio.h>
#include<conio.h>
int g;
void main()
{
    printf("enter the value of global var : ");
    scanf("%d", &g);
    printf("the value is %d", g);
    getch();
}