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