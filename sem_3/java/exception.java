/*
===========================================================
                    EXCEPTION IN JAVA
===========================================================

Exception:
-----------
An exception is an unwanted or unexpected event that occurs
during program execution and interrupts the normal flow
of the program.

Example:
    int a = 10 / 0;
This causes ArithmeticException.

Java exception hierarchy:
-------------------------

                    Throwable
                    /       \
              Exception     Error
                 |
        -------------------
        |                 |
 Checked Exception   Unchecked Exception
                     (RuntimeException)

There are mainly TWO TYPES of exceptions:

1. Checked Exception
2. Unchecked Exception


===========================================================
              1. CHECKED EXCEPTION
===========================================================

Definition:
-----------
Checked exceptions are exceptions that are checked by the
compiler at COMPILE TIME.

If a checked exception can occur, Java forces the programmer
to either:

1. Handle it using try-catch
OR
2. Declare it using throws.

Checked exceptions are generally subclasses of Exception
but NOT subclasses of RuntimeException.

Examples:
---------
1. IOException
2. FileNotFoundException
3. SQLException
4. ClassNotFoundException
5. InterruptedException

Important:
----------
Checked exceptions are also called compile-time exceptions.

The compiler checks whether the exception is handled or
declared.

Common hierarchy:

Exception
   |
   +-- IOException
   |      |
   |      +-- FileNotFoundException
   |
   +-- SQLException
   |
   +-- ClassNotFoundException
   |
   +-- InterruptedException


-----------------------------------------------------------
Example of Checked Exception: IOException
-----------------------------------------------------------
*/

import java.io.*;

class CheckedExample {
    public static void main(String[] args) {

        try {
            FileReader file = new FileReader("abc.txt");
            System.out.println("File opened");
        } catch (IOException e) {
            System.out.println("File not found or cannot be read");
        }
    }
}


/*
===========================================================
          IMPORTANT TYPES OF CHECKED EXCEPTIONS
===========================================================

1. IOException
---------------
Occurs when an input/output operation fails.

Example:
    Reading a file
    Writing to a file
    Network input/output

2. FileNotFoundException
------------------------
Occurs when a specified file cannot be found or opened.

It is a subclass of IOException.

Hierarchy:
    IOException
         |
    FileNotFoundException

3. SQLException
---------------
Occurs when an error happens while working with a
database.

Example:
    Database connection failure
    Invalid SQL query

4. ClassNotFoundException
-------------------------
Occurs when Java cannot find a class at runtime when using
methods such as Class.forName().

5. InterruptedException
-----------------------
Occurs when a thread is interrupted while it is sleeping,
waiting, or performing certain blocking operations.


===========================================================
              2. UNCHECKED EXCEPTION
===========================================================

Definition:
-----------
Unchecked exceptions are exceptions that are NOT checked
by the compiler at compile time.

The compiler does NOT force the programmer to handle or
declare them.

Unchecked exceptions occur mainly because of programming
mistakes or invalid operations.

Unchecked exceptions are subclasses of RuntimeException.

Hierarchy:

Throwable
   |
Exception
   |
RuntimeException
   |
   +-- ArithmeticException
   +-- NullPointerException
   +-- ArrayIndexOutOfBoundsException
   +-- ArrayStoreException
   +-- NumberFormatException
   +-- ClassCastException
   +-- IllegalArgumentException
   +-- IllegalStateException

Important:
----------
Unchecked exceptions are also called runtime exceptions.

They occur during program execution.

===========================================================
          IMPORTANT TYPES OF UNCHECKED EXCEPTIONS
===========================================================

1. ArithmeticException
----------------------
Occurs when an illegal arithmetic operation is performed.

Most common example:
    Division by zero.

2. NullPointerException
-----------------------
Occurs when we try to use an object reference that contains
null.

Example:
    String s = null;
    s.length();

3. ArrayIndexOutOfBoundsException
---------------------------------
Occurs when we access an array using an invalid index.

Example:
    int[] a = {10, 20};
    a[5];

4. ArrayStoreException
----------------------
Occurs when an incompatible object is stored in an array
of objects.

5. NumberFormatException
------------------------
Occurs when a String cannot be converted into a numeric
value.

Example:
    Integer.parseInt("abc");

6. ClassCastException
---------------------
Occurs when an object is incorrectly cast to an incompatible
class.

7. IllegalArgumentException
---------------------------
Occurs when a method receives an inappropriate or invalid
argument.

8. IllegalStateException
------------------------
Occurs when a method is called at an inappropriate time
because the object is not in the required state.


===========================================================
                EXAMPLES OF UNCHECKED
===========================================================
*/

class UncheckedExample {
    public static void main(String[] args) {

        // ArithmeticException
        int a = 10;
        int b = 0;

        // System.out.println(a / b);


        // NullPointerException
        String name = null;

        // System.out.println(name.length());


        // ArrayIndexOutOfBoundsException
        int[] numbers = {10, 20, 30};

        // System.out.println(numbers[5]);


        // NumberFormatException
        // int num = Integer.parseInt("abc");


        // ClassCastException
        Object obj = "Hello";

        // Integer value = (Integer) obj;
    }
}


/*
===========================================================
        CHECKED vs UNCHECKED EXCEPTION
===========================================================

                    CHECKED              UNCHECKED
                    -------              ---------

Checked by          Compiler             Not checked by
                    compiler              compiler

Time                Compile time         Runtime

Parent              Exception            RuntimeException

Handling            Must handle or       Not compulsory
                    declare

try-catch           Required when        Not compulsory
                    exception can occur

throws              Can be used          Not compulsory

Examples            IOException          ArithmeticException
                    SQLException         NullPointerException
                    ClassNotFoundException NumberFormatException
                    InterruptedException ClassCastException


===========================================================
                    VERY IMPORTANT
===========================================================

Exception:
    An abnormal condition that interrupts normal execution.

Checked Exception:
    Compiler checks it.
    Must be handled or declared.
    Example: IOException

Unchecked Exception:
    Compiler does not check it.
    Handling is not compulsory.
    Example: ArithmeticException

RuntimeException:
    Parent class of most unchecked exceptions.

Exception vs Error:
-------------------

Exception:
    Usually conditions that a program can handle/recover
    from.

Error:
    Serious problems generally outside normal application
    handling.

Examples of Error:
    OutOfMemoryError
    StackOverflowError

IMPORTANT MCQ POINTS:
---------------------

1. Checked exceptions are checked at compile time.

2. Unchecked exceptions are checked at runtime.

3. RuntimeException is the superclass of unchecked
   exceptions.

4. IOException is a checked exception.

5. SQLException is a checked exception.

6. ClassNotFoundException is a checked exception.

7. ArithmeticException is an unchecked exception.

8. NullPointerException is an unchecked exception.

9. NumberFormatException is an unchecked exception.

10. ArrayIndexOutOfBoundsException is an unchecked
    exception.

11. The compiler does not force handling of unchecked
    exceptions.

12. The compiler forces handling or declaration of checked
    exceptions.

13. try-catch can be used for BOTH checked and unchecked
    exceptions.

14. throws can be used to declare exceptions.

15. RuntimeException and its subclasses are unchecked
    exceptions.

16. All exceptions are not necessarily checked exceptions.

17. Error is different from Exception.

===========================================================
                    QUICK REVISION
===========================================================

                    EXCEPTION
                        |
              -------------------
              |                 |
           CHECKED          UNCHECKED
              |                 |
       Compile-time          Runtime
       checking             checking
              |                 |
       Exception            RuntimeException
       subclasses           subclasses
              |                 |
       IOException          ArithmeticException
       SQLException         NullPointerException
       FileNotFoundException NumberFormatException
       ClassNotFoundException ClassCastException
       InterruptedException ArrayIndexOutOfBoundsException

===========================================================
*/