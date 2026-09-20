// 2. Find the TRACE of a square matrix

// Trace = sum of the main diagonal elements.

// For example:

// 1  2  3
// 4  5  6
// 7  8  9

// Trace = 1 + 5 + 9 = 15

import java.util.Scanner;

class MatrixTraces {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // Input matrix size
        System.out.print("Enter size of square matrix: ");
        int n = sc.nextInt();

        int[][] matrix = new int[n][n];

        // Input matrix elements
        System.out.println("Enter matrix elements:");
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                matrix[i][j] = sc.nextInt();
            }
        }

        // Calculate trace
        int trace = 0;

        for (int i = 0; i < n; i++) {
            trace += matrix[i][i];
        }

        System.out.println("Trace of matrix = " + trace);

        sc.close();
    }
}