/*
Jagged Array — Small Note
-------------------------------------
A Jagged Array is a 2D array where each row can have a different number of columns.

Why did Jagged Array come?
A normal 2D array requires the same number of columns in every row:

10  20  30
40  50  60
70  80  90

But sometimes we don't need the same number of elements in every row. For example:

Student 1 → 2 subjects
Student 2 → 4 subjects
Student 3 → 3 subjects

A normal 2D array would waste space. Jagged Array solves this problem by allowing each row to have its own size.

What does it do?
It allows us to create:

Row 0 → 10 20
Row 1 → 30 40 50 60
Row 2 → 70 80 90

Each row has a different length.

Basic syntax
int[][] a = new int[3][];


a[0] = new int[2];
a[1] = new int[4];
a[2] = new int[3];
Remember ⭐

Normal 2D Array:
Same number of columns in every row.

Jagged Array:
Different number of columns in different rows.

Main purpose: Flexibility + avoiding unnecessary memory allocation.
*/




import java.util.Scanner;

public class ArraySum {

    // Method to calculate sum of two arrays
    static int[] sumArrays(int[] a, int[] b) {

        int[] sum = new int[a.length];

        for (int i = 0; i < a.length; i++) {
            sum[i] = a[i] + b[i];
        }

        return sum;
    }

    // Method to print array
    static void printArray(int[] arr) {

        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i] + " ");
        }
    }

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter size of arrays: ");
        int n = sc.nextInt();

        int[] a = new int[n];
        int[] b = new int[n];

        System.out.println("Enter elements of first array:");
        for (int i = 0; i < n; i++) {
            a[i] = sc.nextInt();
        }

        System.out.println("Enter elements of second array:");
        for (int i = 0; i < n; i++) {
            b[i] = sc.nextInt();
        }

        // Calling method
        int[] result = sumArrays(a, b);

        System.out.println("Sum of two arrays:");
        printArray(result);

        sc.close();
    }
}



// ----------------------------------Jagged Array — Code Snippet MCQs---------------------------
/*
MCQ 1 — Basic Access
int[][] a = new int[3][];


a[0] = new int[]{10, 20};
a[1] = new int[]{30, 40, 50};
a[2] = new int[]{60};


System.out.println(a[1][2]);

What is the output?

A) 20
B) 30
C) 50
D) 60

✅ Answer: C) 50

Solution:
a[1] is the second row:

a[1] → 30 40 50

a[1][2] means second row, third element → 50.

MCQ 2 — Finding Length
int[][] a = {
    {10, 20},
    {30, 40, 50},
    {60, 70, 80, 90}
};


System.out.println(a[2].length);

What is the output?

A) 2
B) 3
C) 4
D) 9

✅ Answer: C) 4

Solution:

a[0] → 2 elements
a[1] → 3 elements
a[2] → 4 elements

Therefore:

a[2].length

is 4.

⭐ Remember: a.length = number of rows, while a[i].length = number of elements in row i.

MCQ 3 — Nested Loop
int[][] a = {
    {1, 2},
    {3, 4, 5},
    {6}
};


for (int i = 0; i < a.length; i++) {
    for (int j = 0; j < a[i].length; j++) {
        System.out.print(a[i][j] + " ");
    }
}

What is the output?

A) 1 2 3 4 5 6
B) 1 2 3 4 5
C) 1 2 3 4 5 6 0
D) Compilation error

✅ Answer: A) 1 2 3 4 5 6

Solution:

The inner loop uses:

j < a[i].length

So it automatically adjusts to the size of each row.

MCQ 4 — Find the Error
int[][] a = new int[3][];


a[0] = new int[2];
a[1] = new int[3];
a[2] = new int[1];


System.out.println(a[2][1]);

What happens?

A) Prints 0
B) Prints 1
C) Compilation error
D) Runtime error

✅ Answer: D) Runtime error

Solution:

a[2] has only 1 element:

a[2] → [0]
         ↑
       index 0

Valid index:

a[2][0]

But:

a[2][1]

does not exist.

➡️ It causes ArrayIndexOutOfBoundsException.

MCQ 5 — Important Output Question ⭐
int[][] a = {
    {1, 2, 3},
    {4, 5},
    {6, 7, 8, 9}
};


System.out.println(a.length);
System.out.println(a[0].length);
System.out.println(a[2].length);

What is the output?

A)

3
3
4

B)

3
2
4

C)

3
3
3

D)

2
3
4

✅ Answer: A

Solution:
a.length       → 3 rows


a[0].length    → 3 elements
                 {1,2,3}


a[2].length    → 4 elements
                 {6,7,8,9}

Therefore:

3
3
4
🔥 Exam Trick

Remember this simple rule:

a.length       → Number of ROWS


a[i].length    → Number of elements in ROW i


a[i][j]        → Actual element at row i, column j
 */