/*
===========================================================
                 CONSTRUCTOR IN JAVA
===========================================================

CONSTRUCTOR:
------------

A constructor is a special member of a class that is
automatically called when an object is created.

Its main purpose is to INITIALIZE an object.

Example:

    Student s1 = new Student();

Here:

    new Student()
          ↓
    Constructor is called
          ↓
    Object is initialized


===========================================================
             IMPORTANT PROPERTIES OF CONSTRUCTOR
===========================================================

1. Constructor name must be SAME as the class name.

2. Constructor does NOT have a return type.

3. Constructor is automatically called when an object
   is created using the new keyword.

4. Constructor is used to initialize instance variables.

5. Constructor can be overloaded.

6. Constructor is NOT inherited by child classes.

7. Constructor can have parameters.

8. A constructor can call another constructor.

9. A constructor cannot be abstract, static, final,
   or synchronized.

10. Constructor is executed only when an object is created.


===========================================================
             BASIC CONSTRUCTOR EXAMPLE
===========================================================
*/

class Student {

    String name;
    int age;

    Student() {
        name = "Piyush";
        age = 22;
    }

    public static void main(String[] args) {

        Student s1 = new Student();

        System.out.println(s1.name);
        System.out.println(s1.age);
    }
}


/*
===========================================================
                    TYPES OF CONSTRUCTOR
===========================================================

There are mainly TWO types:

1. No-Argument Constructor
2. Parameterized Constructor


===========================================================
              1. NO-ARGUMENT CONSTRUCTOR
===========================================================

A constructor that does not take any parameters is called
a no-argument constructor.

Example:

    Student() {
        name = "Piyush";
    }

IMPORTANT:
----------
No-argument constructor and default constructor are not
exactly the same concept.

A default constructor is automatically provided by the
compiler ONLY when the programmer does not write ANY
constructor.


===========================================================
             2. PARAMETERIZED CONSTRUCTOR
===========================================================

A constructor that accepts parameters is called a
parameterized constructor.

It is used when we want to initialize an object with
specific values.

Example:

    Student(String name, int age)


===========================================================
                PARAMETERIZED EXAMPLE
===========================================================
*/

class Student2 {

    String name;
    int age;

    Student2(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public static void main(String[] args) {

        Student2 s1 = new Student2("Piyush", 22);
        Student2 s2 = new Student2("Rahul", 21);

        System.out.println(s1.name);
        System.out.println(s1.age);

        System.out.println(s2.name);
        System.out.println(s2.age);
    }
}


/*
===========================================================
                  CONSTRUCTOR OVERLOADING
===========================================================

Constructor overloading means having multiple constructors
in the same class with different parameter lists.

Example:

    Student()
    Student(String name)
    Student(String name, int age)

Java decides which constructor to call based on the
arguments passed during object creation.

Example:

    new Student();
         ↓
    Student()

    new Student("Piyush");
         ↓
    Student(String)

    new Student("Piyush", 22);
         ↓
    Student(String, int)


===========================================================
             CONSTRUCTOR OVERLOADING EXAMPLE
===========================================================
*/

class Student3 {

    String name;
    int age;

    Student3() {
        name = "Unknown";
        age = 0;
    }

    Student3(String name) {
        this.name = name;
        age = 0;
    }

    Student3(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public static void main(String[] args) {

        Student3 s1 = new Student3();
        Student3 s2 = new Student3("Piyush");
        Student3 s3 = new Student3("Piyush", 22);

        System.out.println(s1.name + " " + s1.age);
        System.out.println(s2.name + " " + s2.age);
        System.out.println(s3.name + " " + s3.age);
    }
}


/*
===========================================================
        CONSTRUCTOR CALLING ANOTHER CONSTRUCTOR
===========================================================

A constructor can call another constructor of the SAME
class.

This is called CONSTRUCTOR CHAINING.

Java provides:

                this()

to call another constructor of the SAME class.


===========================================================
                    this()
===========================================================

this() is used to call another constructor in the same
class.

Example:

    Student() {
        this("Piyush");
    }

    Student(String name) {
        this.name = name;
    }

Here:

    Student()
       |
       | this("Piyush")
       ↓
    Student(String name)


IMPORTANT:
----------
this() must be the FIRST statement inside a constructor.

Correct:

    Student() {
        this("Piyush");
        age = 22;
    }

Wrong:

    Student() {
        age = 22;
        this("Piyush");
    }

Because this() must always be the first statement.


===========================================================
           SIMPLE this() CONSTRUCTOR CHAINING
===========================================================
*/

class Student4 {

    String name;
    int age;

    Student4() {
        this("Piyush");
    }

    Student4(String name) {
        this(name, 22);
    }

    Student4(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public static void main(String[] args) {

        Student4 s1 = new Student4();

        System.out.println(s1.name);
        System.out.println(s1.age);
    }
}


/*
===========================================================
              UNDERSTANDING THE ABOVE CODE
===========================================================

When we write:

    Student4 s1 = new Student4();

Java first calls:

    Student4()


Inside Student4():

    this("Piyush");

So it calls:

    Student4(String name)


Inside Student4(String name):

    this(name, 22);

So it calls:

    Student4(String name, int age)


Finally:

    this.name = name;
    this.age = age;

Execution flow:

    new Student4()
          ↓
    Student4()
          ↓
    this("Piyush")
          ↓
    Student4(String name)
          ↓
    this(name, 22)
          ↓
    Student4(String name, int age)
          ↓
    this.name = name
    this.age = age


This is called:

        CONSTRUCTOR CHAINING


===========================================================
             WHY USE CONSTRUCTOR CHAINING?
===========================================================

Constructor chaining helps us:

1. Avoid duplicate code.

2. Reuse initialization logic.

3. Keep constructors clean.

4. Initialize objects in a controlled way.

Example without constructor chaining:

    Student() {
        name = "Unknown";
        age = 0;
    }

    Student(String name) {
        this.name = name;
        age = 0;
    }

    Student(String name, int age) {
        this.name = name;
        this.age = age;
    }

There is repeated code.

Using constructor chaining:

    Student() {
        this("Unknown", 0);
    }

    Student(String name) {
        this(name, 0);
    }

    Student(String name, int age) {
        this.name = name;
        this.age = age;
    }

Now initialization logic exists mainly in one place.


===========================================================
         ANOTHER IMPORTANT CONCEPT: super()
===========================================================

super() is used to call the constructor of the PARENT
class.

this()
------
Calls constructor of SAME class.

super()
-------
Calls constructor of PARENT class.

Example:

    Parent()
    Child()

When Child object is created:

    new Child()
         ↓
    Child constructor
         ↓
    super()
         ↓
    Parent constructor


===========================================================
                 super() EXAMPLE
===========================================================
*/

class Parent {

    Parent() {
        System.out.println("Parent constructor");
    }
}

class Child extends Parent {

    Child() {
        super();
        System.out.println("Child constructor");
    }

    public static void main(String[] args) {

        // Child c = new Child();
    }
}


/*
Output:

Parent constructor
Child constructor


Why?

When we create:

    Child c = new Child();

Java first executes the parent constructor.

Execution:

    new Child()
        ↓
    super()
        ↓
    Parent()
        ↓
    Child()


===========================================================
             this() vs super()
===========================================================

this()
-------
Calls another constructor of the SAME class.

super()
--------
Calls constructor of the PARENT class.


Example:

    class Child extends Parent {

        Child() {
            this(10);
        }

        Child(int x) {
            super();
        }
    }

Here:

    this(10)
        ↓
    Calls Child(int)

    super()
        ↓
    Calls Parent()


===========================================================
          VERY IMPORTANT RULES OF this()
===========================================================

1. this() calls another constructor in the SAME class.

2. this() must be the FIRST statement in the constructor.

3. this() can call a parameterized constructor.

4. this() can call a no-argument constructor.

5. A constructor can call another constructor using this().

6. Constructors can form a chain.

7. Constructor chaining should eventually end at a
   constructor that does not call another constructor.

8. A constructor cannot directly or indirectly call itself
   forever.

Example of invalid circular chaining:

    A() {
        this(10);
    }

    A(int x) {
        this();
    }

This creates circular constructor invocation.


===========================================================
          VERY IMPORTANT RULES OF super()
===========================================================

1. super() calls the constructor of the PARENT class.

2. super() must be the FIRST statement in a constructor.

3. If we do not explicitly write super(), Java generally
   inserts super() automatically.

4. The automatically inserted super() calls the no-argument
   constructor of the parent class.

5. If the parent class has no accessible no-argument
   constructor, the child constructor must explicitly call
   an appropriate parent constructor using super(arguments).


===========================================================
             AUTOMATIC super() EXAMPLE
===========================================================
*/

class Parent2 {

    Parent2() {
        System.out.println("Parent");
    }
}

class Child2 extends Parent2 {

    Child2() {
        System.out.println("Child");
    }

    public static void main(String[] args) {

        // Child2 c = new Child2();
    }
}


/*
Java effectively treats the Child constructor as:

    Child2() {
        super();
        System.out.println("Child");
    }

Therefore output is:

Parent
Child


===========================================================
        CAN WE USE this() AND super() TOGETHER?
===========================================================

A constructor cannot directly contain both:

    this()
    super()

because BOTH must be the FIRST statement.

Example:

    Child() {
        this(10);
        super();
    }

This is INVALID.

However, constructor chaining can eventually reach
a parent constructor.

Example:

    Child() {
        this(10);
    }

    Child(int x) {
        super();
    }

Execution:

    Child()
       ↓
    this(10)
       ↓
    Child(int)
       ↓
    super()
       ↓
    Parent()


===========================================================
             COMPLETE CONSTRUCTOR EXAMPLE
===========================================================
*/

class Person {

    String name;
    int age;
    String city;

    Person() {
        this("Unknown");
    }

    Person(String name) {
        this(name, 0);
    }

    Person(String name, int age) {
        this(name, age, "Bangalore");
    }

    Person(String name, int age, String city) {
        this.name = name;
        this.age = age;
        this.city = city;
    }

    public static void main(String[] args) {

        Person p1 = new Person();

        Person p2 = new Person("Piyush");

        Person p3 = new Person("Piyush", 22);

        Person p4 = new Person("Piyush", 22, "Bangalore");

        System.out.println(p1.name + " " + p1.age + " " + p1.city);
        System.out.println(p2.name + " " + p2.age + " " + p2.city);
        System.out.println(p3.name + " " + p3.age + " " + p3.city);
        System.out.println(p4.name + " " + p4.age + " " + p4.city);
    }
}


/*
===========================================================
                    EXAM POINTS
===========================================================

🔥 1. Constructor has the SAME NAME as the class.

🔥 2. Constructor does NOT have a return type.

🔥 3. Constructor is called automatically when an object
      is created.

🔥 4. Constructor is mainly used to initialize objects.

🔥 5. Constructors can be overloaded.

🔥 6. this() calls another constructor of the SAME class.

🔥 7. super() calls a constructor of the PARENT class.

🔥 8. this() must be the FIRST statement.

🔥 9. super() must be the FIRST statement.

🔥 10. We cannot directly use both this() and super()
       in the same constructor.

🔥 11. If no constructor is written, compiler provides a
       default constructor.

🔥 12. If we write any constructor ourselves, Java does NOT
       automatically provide the no-argument constructor.

🔥 13. Constructor is NOT inherited.

🔥 14. Constructor cannot be overridden.

🔥 15. Constructor chaining using this() avoids duplicate
       initialization code.

🔥 16. super() is used for parent constructor invocation.

🔥 17. this() is used for same-class constructor invocation.


===========================================================
                 QUICK MEMORY TRICK
===========================================================

Remember:

        this()  → THIS CLASS

        super() → PARENT CLASS


Example:

    this(10)
       ↓
    Same class constructor

    super(10)
       ↓
    Parent class constructor


===========================================================
               CONSTRUCTOR FLOW
===========================================================

SAME CLASS:

    Constructor A
         |
         | this()
         ↓
    Constructor B
         |
         | this()
         ↓
    Constructor C


INHERITANCE:

    Child Constructor
          |
          | super()
          ↓
    Parent Constructor


===========================================================
              MOST IMPORTANT MCQ TABLE
===========================================================

Feature                 Constructor
-------                 -----------

Purpose                 Initialize object

Name                    Same as class

Return type             No return type

Called                  Automatically during object creation

Overloading             YES

Overriding              NO

Inherited                NO

Can use this()           YES

Can use super()          YES

this()                  Same class constructor

super()                 Parent class constructor

this()/super() position First statement

===========================================================
*/