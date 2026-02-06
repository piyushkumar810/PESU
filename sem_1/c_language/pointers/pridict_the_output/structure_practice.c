#include <stdio.h>
#include <string.h>

struct student {
    int roll_no;
    char name[25];
    float marks;
} s1;

int main() {

    s1.roll_no = 47;
    strcpy(s1.name, "Piyush Kumar");
    s1.marks = 47.50;

    printf("Roll No: %d\n", s1.roll_no);
    printf("Name: %s\n", s1.name);
    printf("Marks: %.2f\n", s1.marks);

    return 0;
}
