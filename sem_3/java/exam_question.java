
// Suppose two lists are given, each having 4 names, and 2 names are common.

// Example:

// List 1 = [Amit, Rahul, Priya, Neha]
// List 2 = [Rahul, Priya, Karan, Ankit]

// We need to find:

// Common names → present in both lists
// Unique names → present in only one list

// ⭐ Best Exam Code
import java.util.*;

public class exam_question {
    public static void main(String[] args) {

        List<String> list1 = new ArrayList<>(
            Arrays.asList("Amit", "Rahul", "Priya", "Neha")
        );

        List<String> list2 = new ArrayList<>(
            Arrays.asList("Rahul", "Priya", "Karan", "Ankit")
        );

        // Common names
        List<String> common = new ArrayList<>(list1);
        common.retainAll(list2);

        // Unique names
        List<String> unique = new ArrayList<>(list1);
        unique.addAll(list2);
        unique.removeAll(common);

        System.out.println("Common names: " + common);
        System.out.println("Unique names: " + unique);
    }
}

// Output
// Common names: [Rahul, Priya]
// Unique names: [Amit, Neha, Karan, Ankit]