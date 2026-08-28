public class multiline_string {

    // main() is the starting point of a Java program.
    // Program execution starts from here.
    public static void main(String[] args) {

        // =========================================================
        // 1. STRING
        // =========================================================

        // String is used to store text/sequence of characters.
        //
        // "sdfghijn" is a String literal.
        // String literals are written inside double quotes (" ").
        //
        // \n is an escape sequence.
        // \n means "new line".
        //
        // + is the concatenation operator.
        // It joins two Strings together.
        //
        // So:
        // "sdfghijn\n" + "dfuhifd"
        //
        // becomes:
        // sdfghijn
        // dfuhifd

        String s = "sdfghijn\n" + "dfuhifd";

        // System.out.println() prints the value on the console
        // and then moves the cursor to the next line.
        System.out.println(s);


        // =========================================================
        // 2. ESCAPE SEQUENCE - DOUBLE QUOTES
        // =========================================================

        // Normally, double quotes are used to start and end a String.
        //
        // Example:
        // String name = "ABC";
        //
        // If we want to PRINT double quotes as part of the String,
        // we cannot directly write:
        //
        // System.out.println(""ABC"");  // ERROR
        //
        // Because Java will think the String ends at the second quote.
        //
        // \" is an escape sequence used to represent
        // a double quote (") inside a String.
        //
        // Therefore:
        // "\"ABC\""
        //
        // produces:
        // "ABC"

        System.out.println("\"ABC\"");


        // =========================================================
        // 3. JSON STRING
        // =========================================================

        // JSON stands for:
        // JavaScript Object Notation.
        //
        // JSON is commonly used to exchange/store data.
        //
        // Example JSON:
        //
        // {"srn" : "abc101"}
        //
        // Here:
        // "srn"     -> key
        // "abc101"  -> value
        //
        // The problem is that JSON itself uses double quotes,
        // and Java Strings also use double quotes.
        //
        // Therefore, we need to escape the JSON double quotes
        // using \".

        String json = "{\"srn\" : \"abc101\"}";

        // Let's understand the above line:
        //
        // \"srn\"
        //      ↓
        // "srn"
        //
        // \"abc101\"
        //      ↓
        // "abc101"
        //
        // The final String stored in the variable 'json' is:
        //
        // {"srn" : "abc101"}

        System.out.println(json);


        // =========================================================
        // IMPORTANT ESCAPE SEQUENCES IN JAVA
        // =========================================================

        // \n  -> New line
        // \t  -> Tab space
        // \"  -> Double quote
        // \'  -> Single quote
        // \\  -> Backslash
        // \b  -> Backspace
        // \r  -> Carriage return


        // =========================================================
        // IMPORTANT STRING CONCEPTS
        // =========================================================

        // String variable:
        // String name = "Piyush";
        //
        // String value:
        // "Piyush"
        //
        // String concatenation:
        // "Hello " + "World"
        // Result:
        // "Hello World"
        //
        // New line:
        // "Hello\nWorld"
        // Result:
        // Hello
        // World


        // =========================================================
        // SEMICOLON (;)
        // =========================================================

        // Most Java statements end with a semicolon (;).
        //
        // Example:
        // String s = "Hello";
        // System.out.println(s);
        //
        // Missing the semicolon will generally cause
        // a compilation error.

    }
}