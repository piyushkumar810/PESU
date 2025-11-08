#include<stdio.h>
int main(){
    typedef struct 
    {
        int *p1,
        *p2;
        char *p3;
    }pointers;
    pointers ptr;
    /*remember that ptr itself is not a pointer, but a structure variable that has three pointer as as it member*/

    int a=125,b;
    char ch[]="my name os piyush";

    ptr.p1=&a;
    ptr.p2=&b;
    ptr.p3=ch;
    *ptr.p2=70;
    
    printf("\n %d %d %s",a,b,ch);/* 125    70    my name os piyush*/
    printf("\n %d %d %s",*ptr.p1,*ptr.p2,ptr.p3);/* 125     70     my name os piyush */


    return 0;
}