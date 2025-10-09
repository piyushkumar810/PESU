/*
6. LEVEL- 2 : Structures and Arrays of Structures
 ■ Objective: Create a program that demonstrates the use of structures and passing them as parameters.
 ■ Instructions:
    □ Define a structure called Student with fields for name, age, and marks.
    □ Create an array of Student structures and initialize it with sample data.
    □ Write a function that takes the array of Student structures and the size of the array as parameters
    to calculate the average marks.
    □ Print the average marks.
 ■ Sample Output:
 Average marks of students: 78.5
 Academic Year 2024- 25
 Dept. of Computer Application
*/

#include <stdio.h>

// Define structure
struct Student {
    char name[50];
    int age;
    float marks;
};

// Function to calculate average marks
float calculateAverage(struct Student s[], int size) {
    float total = 0;
    for (int i = 0; i < size; i++) {
        total += s[i].marks;
    }
    return total / size;
}

int main() {
    // Array of structures initialized with sample data
    struct Student students[] = {
        {"Piyush", 19, 80.0},
        {"Riya", 20, 75.0},
        {"Aman", 18, 78.5},
        {"Sneha", 19, 80.5}
    };

    int size = sizeof(students) / sizeof(students[0]);

    // Function call to calculate average marks
    float avg = calculateAverage(students, size);

    // Display results
    printf("Average marks of students: %.1f\n", avg);
    printf("Academic Year 2024-25\n");
    printf("Dept. of Computer Application\n");

    return 0;
}
