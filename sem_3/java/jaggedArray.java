import java.util.*;

class JaggedArray1 {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("No of Rows = ");
        int r = sc.nextInt();

        // Jagged Array
        int[][] a = new int[r][];

        for (int i = 0; i < a.length; i++) {   // Row wise Loop

            System.out.print("No of Col (Row " + i + "): ");
            int c = sc.nextInt();

            a[i] = new int[c];

            // Column wise Loop
            System.out.print("Enter " + c + " items: ");

            for (int j = 0; j < c; j++) {
                a[i][j] = sc.nextInt();
            }
        }

        // Display Jagged Array
        System.out.println("\nJagged Array:");

        for (int i = 0; i < a.length; i++) {

            for (int j = 0; j < a[i].length; j++) {
                System.out.print(a[i][j] + " ");
            }

            System.out.println();
        }

        sc.close();
    }
}