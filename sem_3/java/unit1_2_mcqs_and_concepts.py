# =============================================================================
# JAVA WAF - GATE-LEVEL MCQ & OUTPUT PREDICTION BANK
# Units 1 & 2 | Exam Focus: 1M + 2M + 4M
# =============================================================================

"""
IMPORTANT:
-----------
This file intentionally does NOT teach basic concepts.
It focuses on:
- Deep conceptual MCQs
- Predict-the-output questions
- Scenario-based questions
- GATE-level traps
- Small "HARD CONCEPT" explanations only where students commonly get confused

Assumption:
Java 17+ style questions unless a question explicitly depends on a version detail.
For output questions, assume the code compiles unless the question asks about
compilation.
"""

# =============================================================================
# PART A - 1 MARK MCQs
# =============================================================================

"""
Q1. JVM / JDK / JRE
Which statement is MOST accurate?

A) JDK = JVM + JRE
B) JRE = JDK + JVM
C) JDK contains development tools and a runtime environment; JVM executes
   Java bytecode.
D) JVM compiles .java directly into machine code.

ANSWER: C

HARD CONCEPT:
JVM is the execution engine. javac is a compiler supplied by the JDK.
The JVM does NOT normally compile Java source code directly.
"""

"""
Q2. String Pool
What is the output?

String a = "java";
String b = "java";
System.out.println(a == b);

A) true
B) false
C) Compilation error
D) Runtime error

ANSWER: A

HARD CONCEPT:
String literals are interned in the String Pool, so identical literals can
refer to the same String object.
"""

"""
Q3. String + new
What is the output?

String a = new String("java");
String b = "java";
System.out.println(a == b);

A) true
B) false
C) Compilation error
D) Runtime error

ANSWER: B

HARD CONCEPT:
new String("java") creates a distinct String object, even though "java"
also exists in the pool.
"""

"""
Q4. final reference
Which statement is TRUE?

final ArrayList<Integer> x = new ArrayList<>();
x.add(10);

A) Compilation error because x is final
B) Runtime error
C) Valid; reference cannot change, object can change
D) Valid only if ArrayList is immutable

ANSWER: C

HARD CONCEPT:
final applies to the reference variable, not to the object's internal state.
"""

"""
Q5. Overloading
Which pair can be overloaded?

A) f(int) and f(int)
B) f(int) and f(Integer)
C) f(int) and f(int) with different return type only
D) f(int) and f(int...) only

ANSWER: B

HARD CONCEPT:
Method overloading requires a different parameter list. Return type alone
cannot distinguish overloaded methods.
"""

"""
Q6. Overriding
Which statement is TRUE?

A) A static method is dynamically dispatched like an instance method.
B) A private method can be overridden.
C) An instance method can be overridden with a covariant return type.
D) final methods must be overridden.

ANSWER: C

HARD CONCEPT:
Static/private/final methods are not overridden in the normal polymorphic
sense. A subclass can declare a method with the same name, but that is not
dynamic overriding for private/static methods.
"""

"""
Q7. Wrapper classes
What is printed?

Integer a = 127;
Integer b = 127;
System.out.println(a == b);

A) true
B) false
C) Compilation error
D) Depends only on heap size

ANSWER: A

HARD CONCEPT:
Integer.valueOf commonly caches Integer objects for values -128 to 127.
Do NOT generalize this rule to all Integer values.
"""

"""
Q8. Autoboxing
What happens?

Integer x = null;
int y = x;

A) y becomes 0
B) Compilation error
C) NullPointerException
D) NumberFormatException

ANSWER: C

HARD CONCEPT:
Unboxing null requires extracting an int from a null Integer, causing
NullPointerException.
"""

"""
Q9. Array covariance
Which statement is TRUE?

A) Object[] a = new String[3]; is illegal.
B) Object[] a = new String[3]; is legal but inserting Integer causes
   ArrayStoreException.
C) String[] is not a subtype of Object[].
D) It always causes ClassCastException.

ANSWER: B

HARD CONCEPT:
Java arrays are covariant. The JVM also knows the runtime array type and
can reject an incompatible store with ArrayStoreException.
"""

"""
Q10. Interface variables
An interface reference can refer to:

A) Only an interface object
B) An object of a class implementing that interface
C) Only an abstract class
D) Only a final class

ANSWER: B
"""

"""
Q11. Abstract class
Can an abstract class have a constructor?

A) No
B) Yes
C) Only if it has no abstract methods
D) Only if final

ANSWER: B

HARD CONCEPT:
Constructors of abstract classes run as part of constructing a concrete
subclass object.
"""

"""
Q12. Sealed classes
Which keyword restricts which classes may directly extend a class?

A) restricted
B) sealed
C) protected
D) final

ANSWER: B
"""

"""
Q13. var
Which declaration is valid?

A) var x;
B) var x = 10;
C) var x = null;
D) var x, y = 10;

ANSWER: B

HARD CONCEPT:
var is local variable type inference. It requires an initializer and cannot
be used for fields, method parameters, or return types.
"""

"""
Q14. try-catch-finally
If a try block returns a value and finally also returns a value:

A) try value always wins
B) finally value wins
C) Compilation error
D) Random value

ANSWER: B

HARD CONCEPT:
A return in finally can override a return from try/catch. This is valid but
strongly discouraged because it hides control flow.
"""

"""
Q15. Thread start
Which is correct?

A) run() creates a new thread automatically.
B) start() schedules a new thread and eventually invokes run().
C) start() can be called repeatedly on the same Thread object.
D) run() and start() are identical.

ANSWER: B

HARD CONCEPT:
Calling run() directly is just a normal method call in the current thread.
Calling start() creates a separate execution path.
"""

"""
Q16. List / Set / Map
Which statement is correct?

A) Set allows duplicate elements.
B) List is primarily key-value storage.
C) Map stores key-value associations.
D) Map is a subtype of Collection.

ANSWER: C

HARD CONCEPT:
Map belongs to the Collections Framework but does NOT extend Collection.
"""

# =============================================================================
# PART B - 2 MARK MCQs
# =============================================================================

"""
Q1. OUTPUT PREDICTION - STRING POOL

String s1 = "hello";
String s2 = new String("hello");
String s3 = s2.intern();

System.out.println(s1 == s2);
System.out.println(s1 == s3);

A) true true
B) false false
C) false true
D) true false

ANSWER: C

WHY:
s2 is a separate heap object.
intern() returns the canonical pooled String reference.
"""

"""
Q2. OUTPUT - OVERLOADING + WIDENING

static void f(long x) {
    System.out.println("long");
}

static void f(Integer x) {
    System.out.println("Integer");
}

public static void main(String[] args) {
    f(10);
}

A) long
B) Integer
C) Compilation error
D) Ambiguous

ANSWER: A

WHY:
For an int argument, primitive widening to long is considered before
boxing to Integer.
HARD TRAP:
Overload resolution generally prefers widening over boxing.
"""

"""
Q3. OUTPUT - OVERRIDING

class A {
    void show() { System.out.print("A"); }
}

class B extends A {
    @Override
    void show() { System.out.print("B"); }
}

A obj = new B();
obj.show();

A) A
B) B
C) Compilation error
D) Runtime error

ANSWER: B

WHY:
Instance methods are dynamically dispatched based on the runtime object.
Reference type = A; actual object = B.
"""

"""
Q4. OUTPUT - STATIC METHOD HIDING

class A {
    static void show() { System.out.print("A"); }
}

class B extends A {
    static void show() { System.out.print("B"); }
}

A obj = new B();
obj.show();

A) A
B) B
C) Compilation error
D) Runtime error

ANSWER: A

HARD CONCEPT:
Static methods are resolved using the reference/class type, not dynamic
runtime dispatch. This is method hiding, not overriding.
"""

"""
Q5. OUTPUT - FIELD HIDING

class A {
    int x = 10;
}

class B extends A {
    int x = 20;
}

A obj = new B();
System.out.println(obj.x);

A) 10
B) 20
C) Compilation error
D) 30

ANSWER: A

HARD CONCEPT:
Fields are not dynamically dispatched. Field access is resolved from the
reference type.
"""

"""
Q6. OUTPUT - CONSTRUCTOR ORDER

class A {
    A() { System.out.print("A"); }
}

class B extends A {
    B() { System.out.print("B"); }
}

new B();

A) BA
B) AB
C) B
D) A

ANSWER: B

HARD CONCEPT:
Before a subclass constructor body executes, the superclass constructor
must execute.
"""

"""
Q7. OUTPUT - FINALLY

static int test() {
    try {
        return 10;
    } finally {
        return 20;
    }
}

System.out.println(test());

A) 10
B) 20
C) Compilation error
D) Runtime error

ANSWER: B

WARNING:
Never normally put return inside finally.
"""

"""
Q8. OUTPUT - UNBOXING

Integer x = 10;
Integer y = 20;
System.out.println(x + y);

A) 1020
B) 30
C) Compilation error
D) "1020"

ANSWER: B

WHY:
Binary numeric operation causes unboxing of Integer values, then addition.
"""

"""
Q9. SCENARIO - EXCEPTION HIERARCHY

Which catch order is valid?

try {
    // code
}
A) catch (Exception e) {} catch (ArithmeticException e) {}
B) catch (ArithmeticException e) {} catch (Exception e) {}
C) catch (Throwable e) {} catch (Exception e) {}
D) Both A and C

ANSWER: B

WHY:
A broader catch before a narrower catch makes the narrower catch unreachable.
"""

"""
Q10. SCENARIO - THREAD

Thread t = new Thread(() -> System.out.println("Hello"));
t.run();

What is guaranteed?

A) A new thread is created.
B) "Hello" executes in the current thread.
C) Two threads execute Hello.
D) Compilation error.

ANSWER: B
"""

"""
Q11. COLLECTIONS

Which data structure is most appropriate when:
- duplicate values must be prevented
- membership testing is important
- order is not the primary requirement

A) HashSet
B) ArrayList
C) Queue
D) Stack

ANSWER: A

HARD CONCEPT:
HashSet uses hashing for average-case fast add/contains/remove.
"""

"""
Q12. ARRAYLIST VS LINKEDLIST

Which operation is generally efficient in ArrayList?

A) Random access by index
B) Insert at beginning always O(1)
C) Delete from middle always O(1)
D) Access by linked node reference

ANSWER: A

HARD CONCEPT:
ArrayList is array-backed, so indexed access is O(1) average.
Insert/delete in the middle may require shifting elements.
"""

# =============================================================================
# PART C - 4 MARK MCQs / MULTI-STATEMENT / GATE STYLE
# =============================================================================

"""
Q1. METHOD OVERLOAD RESOLUTION - DEEP

Consider:

static void f(Object x) {
    System.out.print("Object ");
}

static void f(String x) {
    System.out.print("String ");
}

static void f(StringBuilder x) {
    System.out.print("Builder ");
}

public static void main(String[] args) {
    f(null);
}

What happens?

A) Object
B) String
C) Builder
D) Compilation error due to ambiguity

ANSWER: D

WHY:
null can match all reference types.
String and StringBuilder are unrelated, and both are more specific than
Object. Neither String nor StringBuilder is more specific than the other.
Therefore overload resolution is ambiguous.

GATE TRAP:
null cannot be converted to primitive types, but can match reference types.
"""

"""
Q2. OVERLOADING - WIDENING VS BOXING

static void f(long x) { System.out.print("L"); }
static void f(Integer x) { System.out.print("I"); }

f(5);

A) L
B) I
C) Ambiguous
D) Compilation error

ANSWER: A

RULE:
For int -> long, primitive widening is available.
int -> Integer requires boxing.
The compiler prefers widening over boxing in overload resolution.
"""

"""
Q3. POLYMORPHISM - DYNAMIC DISPATCH

class A {
    void m() { System.out.print("A"); }
}

class B extends A {
    void m() { System.out.print("B"); }
}

class C extends B {
    void m() { System.out.print("C"); }
}

A x = new C();
x.m();

A) A
B) B
C) C
D) Compilation error

ANSWER: C

WHY:
For overridden instance methods, runtime type determines the selected
implementation.
Reference type A does not force A.m().
"""

"""
Q4. STATIC + INSTANCE MIX

class A {
    static void s() { System.out.print("A.s "); }
    void i() { System.out.print("A.i "); }
}

class B extends A {
    static void s() { System.out.print("B.s "); }
    @Override
    void i() { System.out.print("B.i "); }
}

A x = new B();
x.s();
x.i();

What is output?

A) A.s A.i
B) B.s B.i
C) A.s B.i
D) B.s A.i

ANSWER: C

KEY:
static -> reference type
instance override -> runtime type
"""

"""
Q5. FIELD + METHOD POLYMORPHISM

class A {
    int x = 10;
    int get() { return x; }
}

class B extends A {
    int x = 20;
    @Override
    int get() { return x; }
}

A obj = new B();

System.out.print(obj.x + " ");
System.out.print(obj.get());

A) 10 10
B) 20 20
C) 10 20
D) 20 10

ANSWER: C

HARD CONCEPT:
obj.x -> field resolved using reference type A.
obj.get() -> overridden method dynamically dispatched to B.
Inside B.get(), x refers to B.x.
"""

"""
Q6. ABSTRACT CLASS + INTERFACE

Which statement is FALSE?

A) An abstract class can contain concrete methods.
B) An interface can contain default methods.
C) An abstract class can have constructors.
D) An abstract class cannot contain instance variables.

ANSWER: D

WHY:
Abstract classes can contain instance variables, constructors, concrete
methods and abstract methods.
"""

"""
Q7. SEALED CLASSES

Given:

sealed class Shape permits Circle, Square {}

final class Circle extends Shape {}

non-sealed class Square extends Shape {}

class Triangle extends Shape {}

Which is correct?

A) All compile.
B) Triangle compiles because Shape is public.
C) Triangle fails because it is not permitted directly by Shape.
D) Square fails because every subclass of sealed class must be final.

ANSWER: C

HARD CONCEPT:
A direct subclass of a sealed class must be final, sealed, or non-sealed,
and it must be permitted by the sealed superclass.
"""

"""
Q8. EXCEPTION CONTROL FLOW

What is printed?

try {
    System.out.print("A");
    int x = 10 / 0;
    System.out.print("B");
}
catch (ArithmeticException e) {
    System.out.print("C");
}
finally {
    System.out.print("D");
}

A) ABCD
B) ACD
C) ABD
D) CD

ANSWER: B

FLOW:
A -> exception at 10/0 -> skip B -> catch C -> finally D
"""

"""
Q9. EXCEPTION - RETURN + FINALLY

static int f() {
    try {
        return 1;
    } catch (Exception e) {
        return 2;
    } finally {
        System.out.print("F");
    }
}

System.out.println(f());

A) F then 1
B) 1 then F
C) F then 2
D) F only

ANSWER: A

WHY:
No exception occurs. try prepares return value 1; finally executes before
control actually leaves the method.
"""

"""
Q10. COLLECTIONS - MAP AND COLLECTION

Which statements are TRUE?

I. Map stores key-value associations.
II. Map extends Collection.
III. HashSet permits duplicate elements.
IV. ArrayList preserves insertion order.

A) I only
B) I and IV
C) II and III
D) I, II and IV

ANSWER: B
"""

"""
Q11. HASHMAP KEY BEHAVIOR

Suppose:

Map<String, Integer> m = new HashMap<>();
m.put("A", 10);
m.put("A", 50);

What is m.get("A")?

A) 10
B) 50
C) 60
D) Undefined because duplicate keys are allowed

ANSWER: B

HARD CONCEPT:
A Map key is unique. Putting an existing key replaces its associated value.
"""

"""
Q12. THREAD STATE / start

Thread t = new Thread(() -> {});
t.start();
t.start();

What happens?

A) Runs twice.
B) Runs once.
C) IllegalThreadStateException on the second start().
D) Compilation error.

ANSWER: C

HARD CONCEPT:
A Thread instance can be started only once.
Create a new Thread object for another execution.
"""

# =============================================================================
# PART D - TOUGH OUTPUT PREDICTION
# =============================================================================

"""
OUTPUT 1 - INTEGER CACHE

Integer a = 100;
Integer b = 100;

System.out.println(a == b);

ANSWER:
true

Now:

Integer a = 1000;
Integer b = 1000;

System.out.println(a == b);

ANSWER:
Usually false for ordinary Integer.valueOf behavior.

IMPORTANT:
Do NOT use == to compare wrapper values. Use equals() when value equality
is intended.
"""

"""
OUTPUT 2 - STRING CONCATENATION

String s = "A";
s += "B";
s += 10;

System.out.println(s);

ANSWER:
AB10

WHY:
String concatenation converts the operands into a String representation.
"""

"""
OUTPUT 3 - STRING ==

String a = "Ja" + "va";
String b = "Java";

System.out.println(a == b);

ANSWER:
true

HARD CONCEPT:
Constant string expressions can be resolved at compile time and refer to
the same interned literal.
"""

"""
OUTPUT 4 - NEW STRING

String a = new String("Java");
String b = "Java";

System.out.println(a.equals(b));
System.out.println(a == b);

ANSWER:
true
false

equals() -> content equality
==      -> reference identity for objects
"""

"""
OUTPUT 5 - POST INCREMENT

int x = 5;
System.out.println(x++ + ++x);

ANSWER:
12

STEP:
x++ -> uses 5, then x becomes 6
++x -> x becomes 7, uses 7
5 + 7 = 12
"""

"""
OUTPUT 6 - FINAL REFERENCE

final List<Integer> list = new ArrayList<>();
list.add(1);
list.add(2);

System.out.println(list);

ANSWER:
[1, 2]

The reference cannot point to another List, but the mutable object can change.
"""

"""
OUTPUT 7 - PASS BY VALUE

static void change(int x) {
    x = 100;
}

int a = 10;
change(a);
System.out.println(a);

ANSWER:
10

HARD CONCEPT:
Java is pass-by-value. For object references, the VALUE of the reference is
passed; Java does not pass the caller's variable itself by reference.
"""

"""
OUTPUT 8 - OBJECT REFERENCE PASSING

class Box {
    int value = 10;
}

static void change(Box b) {
    b.value = 50;
}

Box x = new Box();
change(x);
System.out.println(x.value);

ANSWER:
50

WHY:
A copy of the reference is passed, but both references point to the same
object, so mutation of the object is visible to the caller.
"""

"""
OUTPUT 9 - REASSIGNMENT VS MUTATION

class Box {
    int value = 10;
}

static void change(Box b) {
    b = new Box();
    b.value = 50;
}

Box x = new Box();
change(x);
System.out.println(x.value);

ANSWER:
10

HARD CONCEPT:
Reassigning the local copy of the reference does not change x in the caller.
"""

"""
OUTPUT 10 - CONSTRUCTOR ORDER

class A {
    A() {
        System.out.print("A ");
    }
}

class B extends A {
    B() {
        System.out.print("B ");
    }
}

class C extends B {
    C() {
        System.out.print("C ");
    }
}

new C();

ANSWER:
A B C
"""

# =============================================================================
# PART E - SCENARIO-BASED MCQs
# =============================================================================

"""
SCENARIO 1 - BANKING APPLICATION
--------------------------------
A banking application has:
- account balance
- deposit()
- withdraw()

The balance must not be directly modified by arbitrary external classes.

Which design is MOST appropriate?

A) public balance + public methods
B) private balance + controlled public methods
C) protected balance + no methods
D) static balance only

ANSWER: B

HARD CONCEPT:
This is encapsulation/data hiding: restrict direct access and expose a
controlled interface.
"""

"""
SCENARIO 2 - PAYMENT SYSTEM
----------------------------
Payment types: UPI, Card, Cash.

All should provide pay(), but implementation differs.

Which Java feature best models this?

A) Encapsulation only
B) Polymorphism using interface/abstract type
C) Array only
D) Static variables

ANSWER: B

EXAM IDEA:
Reference can be Payment p while actual object can be UPI/Card/Cash.
Calling p.pay() can invoke the runtime object's implementation.
"""

"""
SCENARIO 3 - RESTRICTED VEHICLE HIERARCHY
-----------------------------------------
A company wants Vehicle to have ONLY Car and Bike as direct subclasses.

Which Java feature is designed for this?

A) final
B) sealed
C) private
D) synchronized

ANSWER: B

WHY:
sealed + permits restricts direct inheritance.
"""

"""
SCENARIO 4 - THREAD SAFETY
---------------------------
Two threads update a shared counter. The expected result is 2000 but sometimes
the result is lower.

Most likely reason?

A) Compilation error
B) Race condition
C) Method overloading
D) String interning

ANSWER: B

HARD CONCEPT:
Read-modify-write operations are not automatically atomic. Interleaving
between threads can cause lost updates.
"""

"""
SCENARIO 5 - COLLECTION CHOICE
------------------------------
Requirement:
- preserve insertion order
- allow duplicates
- frequent indexed access

Best choice among:
A) HashSet
B) ArrayList
C) HashMap
D) TreeSet

ANSWER: B

WHY:
ArrayList preserves insertion order, permits duplicates and supports O(1)
average indexed access.
"""

"""
SCENARIO 6 - UNIQUE USERNAMES
-----------------------------
Requirement:
- usernames must be unique
- fast membership check

Best choice:
A) HashSet
B) ArrayList
C) LinkedList
D) Stack

ANSWER: A
"""

"""
SCENARIO 7 - FIFO TICKETING
---------------------------
A ticket system must process requests in first-in-first-out order.

Best abstraction:
A) Queue
B) Set
C) Map
D) Stack

ANSWER: A
"""

"""
SCENARIO 8 - LIFO UNDO
----------------------
An editor's undo operation should reverse the most recent action first.

Best abstraction:
A) Queue
B) Stack
C) Map
D) Set

ANSWER: B
"""

# =============================================================================
# PART F - DEEP GATE-STYLE MIXED MCQs
# =============================================================================

"""
Q1. Which statements are TRUE?

I. Overloading is generally resolved at compile time.
II. Overriding of instance methods participates in runtime dispatch.
III. Static methods are dynamically dispatched.
IV. Fields participate in runtime method dispatch.

A) I and II
B) II and III
C) I, II and IV
D) All

ANSWER: A
"""

"""
Q2. Which can cause NullPointerException?

A) int x = Integer.parseInt("null");
B) Integer x = null; int y = x;
C) int x = 10 / 0;
D) String x = null; System.out.println(x == null);

ANSWER: B

TRAPS:
A -> NumberFormatException
C -> ArithmeticException
D -> valid and prints true
"""

"""
Q3. Which is NOT true about constructors?

A) They have no return type.
B) They can be overloaded.
C) They are inherited by subclasses.
D) A superclass constructor is involved when constructing a subclass object.

ANSWER: C

HARD CONCEPT:
Constructors are not inherited.
"""

"""
Q4. Which statement about final is TRUE?

A) final class can be extended.
B) final method must be overridden.
C) final variable cannot be reassigned after initialization.
D) final reference makes referenced object immutable.

ANSWER: C
"""

"""
Q5. Which statement about interfaces is TRUE?

A) An interface can be instantiated directly.
B) A class can implement multiple interfaces.
C) A class can extend multiple classes.
D) Interfaces cannot have methods.

ANSWER: B
"""

"""
Q6. Which access level is MOST restrictive?

A) public
B) protected
C) default/package-private
D) private

ANSWER: D
"""

"""
Q7. Which collection generally maintains sorted order naturally?

A) HashSet
B) TreeSet
C) ArrayList
D) LinkedList

ANSWER: B

HARD CONCEPT:
TreeSet is based on sorted-tree semantics and provides ordered set behavior.
"""

"""
Q8. Which collection maps keys to values?

A) List
B) Set
C) Map
D) Queue

ANSWER: C
"""

"""
Q9. What happens if a HashMap key's equals() and hashCode() contract is
implemented inconsistently?

A) Nothing can go wrong.
B) Hash-based lookup behavior can become incorrect/unreliable.
C) Java automatically fixes it.
D) It becomes a TreeMap.

ANSWER: B

HARD CONCEPT:
Equal objects MUST have equal hash codes. Violating this contract can break
expected hash-based collection behavior.
"""

"""
Q10. Which is a checked exception?

A) NullPointerException
B) ArithmeticException
C) IOException
D) ArrayIndexOutOfBoundsException

ANSWER: C

HARD CONCEPT:
Checked exceptions are generally enforced by the compiler through catch or
throws requirements. RuntimeException subclasses are unchecked.
"""

# =============================================================================
# PART G - MULTI-CORRECT / GATE-STYLE
# =============================================================================

"""
Q1. Select ALL TRUE statements.

A) String is immutable.
B) StringBuilder is mutable.
C) String literals may be interned.
D) String == always compares textual contents.

ANSWER: A, B, C

TRAP:
== compares references for objects; equals() is used for logical equality.
"""

"""
Q2. Select ALL TRUE statements about ArrayList.

A) Allows duplicates.
B) Preserves insertion order.
C) Provides indexed access.
D) Implements Map.

ANSWER: A, B, C
"""

"""
Q3. Select ALL TRUE statements about inheritance.

A) Java classes support single class inheritance.
B) A class can implement multiple interfaces.
C) Constructors are inherited.
D) private members are not directly accessible in subclasses.

ANSWER: A, B, D
"""

"""
Q4. Select ALL TRUE statements about threads.

A) Calling run() directly guarantees a new thread.
B) Calling start() is used to begin independent thread execution.
C) A Thread object cannot normally be started twice.
D) Multiple threads can create race conditions on shared mutable state.

ANSWER: B, C, D
"""

# =============================================================================
# PART H - HARD CONCEPTS YOU SHOULD KNOW BEFORE THE EXAM
# =============================================================================

"""
1. WIDENING VS BOXING IN OVERLOADING
------------------------------------
Example:
f(long)
f(Integer)

f(10) -> f(long)

Why?
The compiler can widen int -> long without boxing.
This is a common overload-resolution trap.

Remember:
primitive widening is preferred over boxing in this situation.
"""

"""
2. STATIC METHOD HIDING VS OVERRIDING
-------------------------------------
Instance method:
A ref = new B();
ref.show(); -> B.show() if overridden.

Static method:
A ref = new B();
ref.show(); -> A.show() when show() is static in A/B.

Remember:
INSTANCE -> runtime object
STATIC   -> reference/class context
"""

"""
3. FIELD HIDING
---------------
Fields do NOT use dynamic dispatch.

A ref = new B();
ref.x -> A.x

But:
ref.get() -> B.get() if get() is overridden.

This difference is one of the highest-value output traps.
"""

"""
4. == VS equals()
-----------------
For primitives:
== compares values.

For objects:
== compares whether references identify the same object.

equals():
normally checks logical/content equality when the class overrides it.

Example:
new String("A") == new String("A")       -> false
new String("A").equals(new String("A"))  -> true
"""

"""
5. INTEGER CACHE
----------------
Do not assume:
Integer a = 1000;
Integer b = 1000;
a == b -> always false

The exact behavior of boxing/caching can depend on implementation and the
specified caching guarantees. For exam-safe value comparison, use equals()
for wrappers and == for primitives.
"""

"""
6. PASS-BY-VALUE
----------------
Java is ALWAYS pass-by-value.

Primitive:
copy of value

Object:
copy of reference value

Therefore:
- object mutation -> visible
- local reference reassignment -> not visible to caller
"""

"""
7. EXCEPTION CATCH ORDER
------------------------
Narrow exception FIRST
Broad exception LAST

Correct:
catch (ArithmeticException e) {}
catch (Exception e) {}

Wrong:
catch (Exception e) {}
catch (ArithmeticException e) {}

Reason:
ArithmeticException would already be caught by Exception, making the later
catch unreachable.
"""

"""
8. FINALLY
----------
finally normally executes whether the try/catch completes normally or via
an exception/return, subject to abrupt termination such as JVM shutdown.

A return in finally can override an earlier return.
This is a classic output question.
"""

"""
9. HASHCODE + EQUALS CONTRACT
-----------------------------
If:
a.equals(b) == true

then:
a.hashCode() == b.hashCode()

The reverse is NOT guaranteed:
same hash code does not necessarily mean objects are equal.

This is extremely important for HashMap/HashSet.
"""

"""
10. MAP IS NOT A COLLECTION
---------------------------
Collection hierarchy:
Iterable
   |
Collection
   |-- List
   |-- Set
   |-- Queue

Map is separate:
Map
 |-- HashMap
 |-- TreeMap
 |-- LinkedHashMap

Map still belongs to the Java Collections Framework conceptually, but it does
not implement Collection.
"""

"""
11. ARRAYLIST VS LINKEDLIST
---------------------------
ArrayList:
- array-backed
- fast indexed access
- middle insertion/deletion can require shifting

LinkedList:
- linked-node structure
- indexed access requires traversal
- can be useful when working through iterators/end operations, but do not
  blindly assume every insertion is O(1)

EXAM TRAP:
"LinkedList insertion is always O(1)" is FALSE when locating the insertion
position itself requires traversal.
"""

"""
12. SEALED CLASS RULE
---------------------
A direct subclass of a sealed class must be declared:
- final
OR
- sealed
OR
- non-sealed

and must be permitted by the sealed parent.

This is a favorite conceptual MCQ.
"""

# =============================================================================
# FINAL RAPID REVISION - 30 FACTS
# =============================================================================

"""
1. JDK -> development kit.
2. JRE -> runtime environment.
3. JVM -> executes bytecode.
4. javac -> Java compiler.
5. String -> immutable.
6. StringBuilder -> mutable.
7. == on objects -> reference identity.
8. equals() -> logical equality when overridden.
9. final reference -> cannot be reassigned.
10. final object -> NOT automatically immutable.
11. Overloading -> compile-time selection.
12. Overriding -> runtime dispatch for instance methods.
13. Static methods -> hidden, not dynamically overridden.
14. Fields -> not dynamically dispatched.
15. Constructors -> not inherited.
16. Abstract class -> can have constructors.
17. Interface -> class can implement multiple interfaces.
18. sealed -> restricts direct inheritance.
19. var -> local variable type inference.
20. var requires initializer.
21. null unboxing -> NullPointerException.
22. Array covariance -> can cause ArrayStoreException.
23. Java -> pass-by-value.
24. finally can execute before return completes.
25. return in finally can override previous return.
26. HashMap -> key-value mapping.
27. HashSet -> unique elements.
28. ArrayList -> indexed, ordered, duplicates allowed.
29. Queue -> FIFO abstraction.
30. Stack/LIFO -> most recent item first.

# TOP 10 TRAPS
1. run() != start()
2. == != equals()
3. static hiding != overriding
4. field access != method dispatch
5. final reference != immutable object
6. Java pass-by-value
7. constructors are not inherited
8. Map != Collection
9. catch broad exception after narrow exception
10. widening vs boxing in overload resolution
"""

# =============================================================================
# EXAM TARGET
# =============================================================================

"""
If the exam contains:
4 x 4 marks:
    Prioritize:
    - polymorphism + output
    - SSR-like? NO: Java syllabus -> OOP/polymorphism
    - exception flow
    - collections + complexity
    - threads
    - sealed classes

4 x 2 marks:
    Prioritize:
    - output prediction
    - overload/override
    - exception hierarchy
    - collection selection

16 x 1 marks:
    Prioritize:
    - definitions
    - keywords
    - output traps
    - JDK/JRE/JVM
    - String pool
    - wrapper caching
    - var
    - sealed
    - collection properties

BEST LAST-MINUTE ORDER:
1. Polymorphism traps
2. String pool + ==/equals
3. Exceptions + finally
4. Collections
5. Threads
6. Sealed classes
7. JDK/JRE/JVM
8. var/wrappers/autoboxing
"""

# =============================================================================
# END
# =============================================================================
