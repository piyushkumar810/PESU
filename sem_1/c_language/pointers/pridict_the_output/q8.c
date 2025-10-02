#include <stdio.h>
int main() {
    char str[] = "Hello";
    char *p = str;
    printf("%c \n %c\n", *p, *(p+4));
    return 0;
}
