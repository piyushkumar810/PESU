public class about_var {

    public static void main(String[] args) {

        // ============================================================
        // 1. WHAT IS A VARIABLE?
        // ============================================================

        // A variable is a named memory location used to store data.
        //
        // Syntax:
        //     dataType variableName = value;
        //
        // Example:
        int age = 21;
        System.out.println(age);
        //
        // int      -> data type
        // age      -> variable name
        // 21       -> value
        // =        -> assignment operator


        // ============================================================
        // 2. DECLARATION vs INITIALIZATION
        // ============================================================

        // DECLARATION:
        // Creating a variable without giving it a value.

        int marks;
        // INITIALIZATION:
        // Giving a value to a variable for the first time.

        marks = 90;
        System.out.println(marks);


        // DECLARATION + INITIALIZATION together:

        int score = 95;
        System.out.println(score);

        // ============================================================
        // 3. REASSIGNMENT
        // ============================================================

        // A normal variable can change its value after initialization.

        int x = 10;

        x = 20;

        // Now x contains 20, not 10.
        System.out.println(x);


        // ============================================================
        // 4. VARIABLE MUST BE DECLARED BEFORE USE
        // ============================================================

        int number = 100;

        System.out.println(number);

        // This is invalid:
        //
        // System.out.println(value);
        // int value = 10;
        //
        // Because value is used before declaration.


        // ============================================================
        // 5. JAVA IS STATISTICALLY TYPED
        // ============================================================

        // Java is a statically typed language.
        //
        // The data type of a variable is known at compile time.

        int a = 10;
        System.out.println(a);

        // a = "Hello";  // ERROR
        //
        // Because a is an int and cannot store a String.


        // ============================================================
        // 6. TYPES OF VARIABLES IN JAVA
        // ============================================================

        // There are mainly 3 types of variables:
        //
        // 1. Local variable
        // 2. Instance variable
        // 3. Static/Class variable


        // ---------------- LOCAL VARIABLE ----------------

        // A variable declared inside a method, constructor,
        // or block is called a local variable.

        int localVariable = 50;
        System.out.println(localVariable);

        // localVariable exists only inside this method/block.


        // ---------------- INSTANCE VARIABLE ----------------

        // An instance variable is declared inside a class
        // but outside methods, constructors, and blocks.
        //
        // It belongs to an OBJECT.

        // Example:
        //
        // class Student {
        //     int age;       // instance variable
        // }


        // ---------------- STATIC VARIABLE ----------------

        // A static variable is declared using the 'static' keyword.
        //
        // It belongs to the CLASS rather than individual objects.

        // Example:
        //
        // class Student {
        //     static String college = "ABC";
        // }


        // ============================================================
        // 7. LOCAL VARIABLE DEFAULT VALUE
        // ============================================================

        // IMPORTANT MCQ:
        //
        // Local variables DO NOT get default values automatically.
        //
        // You must initialize them before using them.

        // int value;

        // System.out.println(value);
        // ERROR: variable value might not have been initialized.


        // ============================================================
        // 8. INSTANCE AND STATIC VARIABLE DEFAULT VALUES
        // ============================================================

        // Instance and static variables DO get default values.

        // Default values:
        //
        // byte      -> 0
        // short     -> 0
        // int       -> 0
        // long      -> 0L
        // float     -> 0.0f
        // double    -> 0.0d
        // char      -> '\u0000'
        // boolean   -> false
        // reference -> null


        // ============================================================
        // 9. PRIMITIVE DATA TYPES
        // ============================================================

        // Java has 8 primitive data types:
        //
        // byte
        // short
        // int
        // long
        // float
        // double
        // char
        // boolean


        // ---------------- byte ----------------

        // Size: 8 bits
        // Range: -128 to 127

        byte b = 100;
        System.out.println(b);


        // ---------------- short ----------------

        // Size: 16 bits
        // Range: -32,768 to 32,767

        short sh = 30000;
        System.out.println(sh);


        // ---------------- int ----------------

        // Size: 32 bits
        // Range:
        // -2^31 to 2^31 - 1
        //
        // int is the default type for integer literals.

        int i = 100;
        System.out.println(i);

        // ---------------- long ----------------

        // Size: 64 bits
        //
        // For large integer literals, use L.

        long population = 8000000000L;
        System.out.println(population);

        // 8000000000 without L may cause an integer literal error
        // because Java treats integer literals as int by default.


        // ---------------- float ----------------

        // Size: 32 bits
        //
        // Decimal literals are double by default.
        // Therefore, use 'f' or 'F' for float.

        float price = 10.5f;
        System.out.println(price);

        // float price = 10.5;  // ERROR
        //
        // Because 10.5 is a double by default.


        // ---------------- double ----------------

        // Size: 64 bits
        // Decimal literals are double by default.

        double salary = 50000.50;
        System.out.println(salary);


        // ---------------- char ----------------

        // Size: 16 bits
        // Stores a single Unicode character.
        //
        // char uses SINGLE quotes.

        char grade = 'A';
        System.out.println(grade);

        // char grade = "A";  // ERROR
        //
        // "A" is a String.
        // 'A' is a char.


        // ---------------- boolean ----------------

        // Can store only:
        //
        // true
        // false

        boolean passed = true;
        System.out.println(passed);

        // boolean x = 1;  // ERROR
        //
        // Java does NOT treat 1 as true.


        // ============================================================
        // 10. REFERENCE VARIABLES
        // ============================================================

        // Reference variables store a reference to an object,
        // rather than directly storing the object itself.

        String name = "Piyush";
        System.out.println(name);

        // String is NOT a primitive data type.
        // String is a class.


        // Example:
        //
        // Student s = new Student();
        //
        // s is a reference variable.
        // new Student() creates an object.


        // ============================================================
        // 11. null
        // ============================================================

        // Reference variables can contain null.

        String city = null;
        System.out.println(city);

        // null means the reference does not currently refer
        // to any object.


        // Primitive variables cannot store null.

        // int n = null;       // ERROR
        // boolean b = null;   // ERROR


        // ============================================================
        // 12. var KEYWORD
        // ============================================================

        // Java 10 introduced local variable type inference using 'var'.

        // var num = 100;

        // Java automatically determines:
        //
        // num -> int
        //
        // IMPORTANT:
        // 'var' does NOT mean dynamically typed.
        //
        // The type is still fixed after compilation.

        // num = "Hello";  // ERROR


        // ============================================================
        // 13. RULES FOR 'var'
        // ============================================================

        // 'var' can be used for LOCAL VARIABLES.

        // var name2 = "Java";


        // 'var' MUST be initialized when declared.

        // var x;  // ERROR


        // 'var' cannot be initialized with null alone.

        // var x = null;  // ERROR
        //
        // Java cannot determine the type.


        // 'var' cannot be used for fields/instance variables.

        // class Test {
        //     var x = 10;  // ERROR
        // }


        // 'var' cannot be used for method parameters.

        // void test(var x) { }  // ERROR


        // 'var' cannot be used as a method return type.

        // var test() { }  // ERROR


        // ============================================================
        // 14. IDENTIFIERS
        // ============================================================

        // The name of a variable is called an identifier.
        //
        // Example:
        //
        // int marks = 90;
        //     ↑
        //  identifier


        // Rules for identifiers:
        //
        // 1. Can contain letters.
        // 2. Can contain digits.
        // 3. Can contain underscore (_).
        // 4. Can contain dollar sign ($).
        // 5. Cannot start with a digit.
        // 6. Cannot contain spaces.
        // 7. Cannot be a Java keyword.
        // 8. Java identifiers are case-sensitive.


        int marks1 = 90;       // VALID
        int _marks = 90;      // VALID
        int $marks = 90;      // VALID
        System.out.println(marks1);
        System.out.println(_marks);
        System.out.println($marks);

        // int 1marks = 90;   // INVALID
        // int my marks = 90; // INVALID
        // int class = 10;    // INVALID because class is a keyword


        // ============================================================
        // 15. CASE SENSITIVITY
        // ============================================================

        int age1 = 20;
        int Age1 = 30;
        System.out.println(age1);
        System.out.println(Age1);

        // age1 and Age1 are TWO DIFFERENT variables.


        // ============================================================
        // 16. KEYWORDS CANNOT BE VARIABLE NAMES
        // ============================================================

        // Java has reserved keywords.
        //
        // Examples:
        //
        // int
        // class
        // public
        // static
        // void
        // if
        // else
        // for
        // while
        // return
        // new
        // final
        // this
        // super
        //
        // These cannot be used as identifiers.


        // ============================================================
        // 17. CONSTANT VARIABLES - final
        // ============================================================

        // Use 'final' when a variable should not be reassigned.

        final int MAX_AGE = 100;

        // MAX_AGE = 200;  // ERROR
        System.out.println(MAX_AGE);


        // By convention, constants are written in:
        // UPPER_CASE_WITH_UNDERSCORES.


        // ============================================================
        // 18. FINAL VARIABLE MUST BE INITIALIZED BEFORE USE
        // ============================================================

        final int value2;

        value2 = 50;

        // This is valid because value2 is assigned exactly once.
        System.out.println(value2);


        // value2 = 100;  // ERROR
        //
        // A final variable cannot be assigned again.


        // ============================================================
        // 19. TYPE CASTING
        // ============================================================

        // Converting one data type into another is called type casting.


        // ---------------- WIDENING ----------------

        // Smaller type -> larger compatible type.
        //
        // This is generally automatic.

        int small = 100;

        long large = small;
        System.out.println(large);

        // int -> long
        //
        // No explicit casting required.


        // Common widening:
        //
        // byte -> short -> int -> long -> float -> double
        //
        // char -> int -> long -> float -> double


        // ---------------- NARROWING ----------------

        // Larger type -> smaller type.
        //
        // Requires explicit casting.

        double d = 10.99;

        int integer = (int) d;
        System.out.println(integer);

        // Result:
        // 10
        //
        // Decimal part is removed.


        // ============================================================
        // 20. INTEGER LITERAL DEFAULT TYPE
        // ============================================================

        // Integer literals are int by default.

        int n1 = 10;
        System.out.println(n1);

        // long n2 = 10; is also valid because int can widen to long.

        long n2 = 10;
        System.out.println(n2);

        // ============================================================
        // 21. DECIMAL LITERAL DEFAULT TYPE
        // ============================================================

        // Decimal literals are double by default.

        double d1 = 10.5;
        System.out.println(d1);

        // float d2 = 10.5;  // ERROR

        float d2 = 10.5f;
        System.out.println((d2));

        // ============================================================
        // 22. CHAR + INT
        // ============================================================

        // char is internally represented using a numeric Unicode value.

        char c = 'A';

        int ascii = c;
        System.out.println(ascii);

        // 'A' has Unicode value 65.
        //
        // Therefore:
        // ascii = 65


        // ============================================================
        // 23. CHAR + CHAR
        // ============================================================

        char c1 = 'A';
        char c2 = 'B';

        int result = c1 + c2;
        System.out.println(result);

        // c1 + c2 results in int.
        //
        // 65 + 66 = 131


        // ============================================================
        // 24. INTEGER OPERATIONS
        // ============================================================

        byte x1 = 10;
        byte x2 = 20;

        // byte result2 = x1 + x2;  // ERROR
        //
        // Arithmetic operations on byte/short/char are promoted to int.

        int result2 = x1 + x2;
        System.out.println((result2));


        // ============================================================
        // 25. INTEGER PROMOTION
        // ============================================================

        // byte, short and char are generally promoted to int
        // during arithmetic operations.

        byte p = 10;
        byte q = 20;

        int r = p + q;
        System.out.println((r));


        // ============================================================
        // 26. VARIABLE SCOPE
        // ============================================================

        // Scope means the region where a variable can be accessed.

        {
            int blockVariable = 100;

            System.out.println(blockVariable);
        }

        // blockVariable cannot be accessed here.
        //
        // System.out.println(blockVariable); // ERROR


        // ============================================================
        // 27. LOCAL VARIABLE SHADOWING
        // ============================================================

        // A local variable can have the same name as an instance
        // variable. The local variable takes priority.

        // Example:
        //
        // class Student {
        //
        //     int age = 20;
        //
        //     void display() {
        //         int age = 30;
        //
        //         System.out.println(age);
        //         // Prints 30
        //     }
        // }


        // ============================================================
        // 28. 'this' FOR INSTANCE VARIABLE
        // ============================================================

        // When local and instance variables have the same name,
        // 'this' refers to the current object's instance variable.
        //
        // Example:
        //
        // class Student {
        //
        //     int age;
        //
        //     Student(int age) {
        //         this.age = age;
        //     }
        // }


        // ============================================================
        // 29. STATIC VARIABLE
        // ============================================================

        // A static variable is shared among all objects of a class.
        //
        // Example:
        //
        // class Student {
        //
        //     static String college = "ABC";
        // }
        //
        // Only ONE copy of college is associated with the class.


        // ============================================================
        // 30. INSTANCE VARIABLE
        // ============================================================

        // Every object gets its own copy of an instance variable.
        //
        // Example:
        //
        // class Student {
        //     int age;
        // }
        //
        // Student s1 = new Student();
        // Student s2 = new Student();
        //
        // s1.age and s2.age are separate variables.


        // ============================================================
        // 31. VARIABLE NAMING CONVENTION
        // ============================================================

        // Java convention:
        //
        // Variables -> camelCase
        //
        // Examples:
        //
        // firstName
        // totalMarks
        // studentAge
        //
        // Constants -> UPPER_CASE
        //
        // MAX_VALUE
        // PI_VALUE


        // ============================================================
        // 32. MULTIPLE VARIABLES
        // ============================================================

        // You can declare multiple variables of the same type.

        // int a1 = 10, a2 = 20, a3 = 30;
        // System.out.println(a1,a2,a3);


        // ============================================================
        // 33. SAME VARIABLE NAME IN SAME SCOPE
        // ============================================================

        // You cannot declare two local variables with the same name
        // in the same scope.

        int test = 10;
        System.out.println(test);

        // int test = 20;  // ERROR


        // ============================================================
        // 34. VARIABLE VS VALUE
        // ============================================================

        // Variable:
        // A named storage location.
        //
        // Value:
        // Data stored inside that variable.

        int studentAge = 21;
        System.out.println(studentAge);

        // studentAge -> variable
        // 21         -> value


        // ============================================================
        // 35. IMPORTANT MCQ: int x = 10;
        // ============================================================

        // In:
        //
        // int x = 10;
        //
        // int -> data type
        // x   -> identifier / variable name
        // =   -> assignment operator
        // 10  -> integer literal
        //
        // 10 is normally an int literal.


        // ============================================================
        // 36. IMPORTANT MCQ: final
        // ============================================================

        final int DAYS_IN_WEEK = 7;
        System.out.println(DAYS_IN_WEEK);

        // final means the variable cannot be reassigned.
        //
        // It does NOT necessarily mean the object itself is immutable
        // when the variable is a reference.
    }
}