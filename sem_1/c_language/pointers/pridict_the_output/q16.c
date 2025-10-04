#include <stdio.h>
int main() {
    char *str = "World";
    printf("%c %c\n", *str, *(str+2));
    return 0;
}
/*
Explanation:
*str = 'W',
*(str+2) = 'r'.
Output: W r.
*/