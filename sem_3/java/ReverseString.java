import java.util.Scanner;

public class ReverseString {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        // Take input from user
        System.out.print("Enter a string: ");
        String str = sc.nextLine();

        // Variable to store reversed string
        String reverse = "";

        // Reverse the string
        for (int i = str.length() - 1; i >= 0; i--) {
            reverse = reverse + str.charAt(i);
        }

        // Display result
        System.out.println("Original String: " + str);
        System.out.println("Reversed String: " + reverse);

        sc.close();
    }
}