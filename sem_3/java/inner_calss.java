// ============================================================
// INNER / NESTED CLASSES IN JAVA
// ============================================================

// A class defined inside another class is called a nested class.
//
// If it is non-static → Inner Class
// If it is static → Static Nested Class
//
// There are 4 commonly discussed types:
//
// 1. Member Inner Class
// 2. Static Nested Class
// 3. Local Inner Class
// 4. Anonymous Inner Class


class Outer {

    int x = 10;
    static int y = 20;


    // ========================================================
    // 1. MEMBER INNER CLASS
    // ========================================================

    // A non-static class declared directly inside another class
    // is called a Member Inner Class.
    
    class Inner {

        void display() {

            // Inner class can access instance members
            // of the outer class directly.

            System.out.println(x);

            // It can also access static members.

            System.out.println(y);
        }
    }


    // To create a Member Inner Class object:
    //
    // Outer obj = new Outer();
    // Outer.Inner inner = obj.new Inner();
    //
    // IMPORTANT:
    // A Member Inner Class object requires an object
    // of the Outer class.


    // ========================================================
    // 2. STATIC NESTED CLASS
    // ========================================================

    // A static class declared inside another class
    // is called a Static Nested Class.

    static class StaticInner {

        void display() {

            // Can directly access static members.

            System.out.println(y);

            // Cannot directly access non-static
            // instance variable x.
            
            // System.out.println(x); // ERROR
        }
    }


    // Creating Static Nested Class object:
    //
    // Outer.StaticInner obj = new Outer.StaticInner();
    //
    // IMPORTANT:
    // No Outer class object is required.


    // ========================================================
    // 3. LOCAL INNER CLASS
    // ========================================================

    void method() {

        // A class declared inside a method/block
        // is called a Local Inner Class.

        class LocalInner {

            void display() {
                System.out.println("Local Inner Class");
            }
        }

        // Object must be created inside the scope
        // where the class is declared.

        LocalInner obj = new LocalInner();

        obj.display();
    }


    // IMPORTANT:
    // Local Inner Class cannot normally be accessed
    // outside the method/block where it is declared.


    // ========================================================
    // 4. ANONYMOUS INNER CLASS
    // ========================================================

    // An Anonymous Inner Class is a class without a name.
    //
    // It is usually used when we need a class/object
    // only once.

    Runnable r = new Runnable() {

        @Override
        public void run() {
            System.out.println("Anonymous Inner Class");
        }
    };


    // The class has no name.
    //
    // new Runnable() {
    //     ...
    // };
    //
    // creates an object of an anonymous class.


    // ========================================================
    // MAIN METHOD
    // ========================================================

    public static void main(String[] args) {

        // -------- Member Inner Class --------

        Outer outer = new Outer();

        Outer.Inner inner = outer.new Inner();

        inner.display();


        // -------- Static Nested Class --------

        Outer.StaticInner staticObj =
                new Outer.StaticInner();

        staticObj.display();


        // -------- Local Inner Class --------

        outer.method();


        // -------- Anonymous Inner Class --------

        outer.r.run();
    }
}