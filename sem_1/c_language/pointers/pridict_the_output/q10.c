#include <stdio.h>
int main() {
    int arr[5] = {1,2,3,4,5};
    int *p = arr+2;
    printf("%d\n", p[-1]);
    return 0;
}
/*
Explanation:
This is literally how the C language defines array indexing!
That means:

p[0] = *(p+0) = *p
p[1] = *(p+1)
p[2] = *(p+2)

in negative indexing
p[-1] = *(p + (-1)) = *(p - 1)

so
*(p - 1) = arr[1] = 2

*/