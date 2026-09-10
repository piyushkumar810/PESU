/*
============================================================
              JAVA COLLECTION FRAMEWORK
============================================================

WHAT IS A COLLECTION?
---------------------

A collection is an object that is used to store and
manipulate a group of objects/elements.

Example:

    10
    20
    30
    40

Instead of creating separate variables:

    int a = 10;
    int b = 20;
    int c = 30;
    int d = 40;

We can use a collection to store them together.


============================================================
           WHY DO WE NEED COLLECTIONS?
============================================================

Suppose we have to store 100 student names.

Using an array:

    String[] students = new String[100];

The size is fixed.

If later we need 150 students, we need a new array.

Collections solve this problem because many collection
classes can grow or shrink dynamically.

Advantages of Collections:

1. Dynamic size
2. Easy insertion and deletion
3. Searching is easier
4. Sorting utilities are available
5. Ready-made data structures
6. Can store objects
7. Provides many useful methods


============================================================
             COLLECTION FRAMEWORK
============================================================

Java Collection Framework is a set of interfaces,
classes, and algorithms used to store and manipulate
groups of objects.

Main interfaces:

                    Collection
                       |
        --------------------------------
        |              |               |
       List            Set            Queue
        |
   ArrayList
   LinkedList
   Vector
   Stack


Map is also part of the Collection Framework, but
Map does NOT extend the Collection interface.

                    Map
                     |
        ---------------------------
        |            |            |
     HashMap     LinkedHashMap   TreeMap


============================================================
              COLLECTION HIERARCHY
============================================================

                         Iterable
                            |
                       Collection
                            |
             ----------------------------
             |            |             |
            List         Set          Queue
             |            |             |
       ArrayList       HashSet    PriorityQueue
       LinkedList      LinkedHashSet
       Vector           TreeSet
       Stack


Map is separate:

                         Map
                          |
          ------------------------------
          |             |              |
       HashMap     LinkedHashMap     TreeMap


============================================================
          COLLECTION vs COLLECTIONS
============================================================

Collection:
-----------

Collection is an INTERFACE.

It is the root interface of the main collection hierarchy.

Examples:

    List
    Set
    Queue

are subinterfaces of Collection.


Collections:
------------

Collections is a UTILITY CLASS.

It contains static methods for operating on collections.

Examples:

    Collections.sort()
    Collections.reverse()
    Collections.max()
    Collections.min()


IMPORTANT MCQ:

Collection  → Interface
Collections → Utility class


============================================================
                    LIST
============================================================

List is an interface.

It represents an ORDERED collection.

Main characteristics of List:

1. Maintains insertion order.
2. Allows duplicate elements.
3. Allows null values.
4. Elements can be accessed using index.
5. Index starts from 0.

Example:

    [10, 20, 30, 20]

20 can appear multiple times.

Index:

    10    20    30    20
     0     1     2     3


Main List implementations:

1. ArrayList
2. LinkedList
3. Vector
4. Stack


============================================================
                  ARRAYLIST
============================================================

ArrayList is a class in Java that implements the List
interface.

Package:

    java.util.ArrayList

ArrayList is based on a DYNAMIC ARRAY.

Unlike a normal array, an ArrayList can automatically
grow when more elements are added.


Syntax:

    ArrayList<DataType> variableName = new ArrayList<>();


Example:

    ArrayList<Integer> numbers =
        new ArrayList<>();


============================================================
             ARRAYLIST BASIC EXAMPLE
============================================================
*/

import java.util.ArrayList;

class ArrayListExample {

    public static void main(String[] args) {

        ArrayList<Integer> numbers = new ArrayList<>();

        numbers.add(10);
        numbers.add(20);
        numbers.add(30);

        System.out.println(numbers);
    }
}


/*
Output:

[10, 20, 30]


============================================================
              IMPORTANT ARRAYLIST FEATURES
============================================================

1. Dynamic size

ArrayList automatically grows when elements are added.


2. Maintains insertion order

Example:

    add(30)
    add(10)
    add(20)

Output:

    [30, 10, 20]


3. Allows duplicates

Example:

    [10, 20, 10, 30]


4. Allows null

Example:

    [10, null, 20]


5. Index-based access

Example:

    numbers.get(0)


6. Stores objects

ArrayList uses GENERICS.

Example:

    ArrayList<Integer>

NOT:

    ArrayList<int>

Because Java Collections work with objects, not primitive
types.


============================================================
             ARRAYLIST AND PRIMITIVE TYPES
============================================================

Collections cannot directly store primitive data types.

Primitive:

    int
    char
    double
    float
    boolean

Use wrapper classes instead:

    int     → Integer
    char    → Character
    double  → Double
    float   → Float
    boolean → Boolean
    long    → Long
    short   → Short
    byte    → Byte


Example:

    ArrayList<Integer>

NOT:

    ArrayList<int>


============================================================
                   ADD ELEMENT
============================================================

add() is used to add an element.

Syntax:

    list.add(element);


Example:
*/

import java.util.ArrayList;

class AddExample {

    public static void main(String[] args) {

        ArrayList<String> names = new ArrayList<>();

        names.add("Piyush");
        names.add("Rahul");
        names.add("Aman");

        System.out.println(names);
    }
}


/*
Output:

[Piyush, Rahul, Aman]


============================================================
             ADD ELEMENT AT SPECIFIC INDEX
============================================================

We can also specify the index.

Syntax:

    list.add(index, element);


Example:
*/

import java.util.ArrayList;

class AddIndexExample {

    public static void main(String[] args) {

        ArrayList<String> names = new ArrayList<>();

        names.add("Piyush");
        names.add("Rahul");

        names.add(1, "Aman");

        System.out.println(names);
    }
}


/*
Output:

[Piyush, Aman, Rahul]

Existing elements are shifted to the right.


============================================================
                  ACCESS ELEMENT
============================================================

get() is used to access an element.

Syntax:

    list.get(index);


Example:
*/

import java.util.ArrayList;

class GetExample {

    public static void main(String[] args) {

        ArrayList<String> names = new ArrayList<>();

        names.add("Piyush");
        names.add("Rahul");
        names.add("Aman");

        System.out.println(names.get(0));
        System.out.println(names.get(1));
    }
}


/*
Output:

Piyush
Rahul


IMPORTANT:

Index starts from 0.

If size = 3:

    index 0
    index 1
    index 2

There is NO index 3.


============================================================
                 UPDATE ELEMENT
============================================================

set() is used to replace an existing element.

Syntax:

    list.set(index, newValue);


Example:
*/

import java.util.ArrayList;

class SetExample {

    public static void main(String[] args) {

        ArrayList<String> names = new ArrayList<>();

        names.add("Piyush");
        names.add("Rahul");
        names.add("Aman");

        names.set(1, "Rohit");

        System.out.println(names);
    }
}


/*
Output:

[Piyush, Rohit, Aman]

IMPORTANT:

set() replaces an element.

It does NOT add a new element.


============================================================
                   REMOVE ELEMENT
============================================================

There are two commonly used remove() forms:

1. remove(index)
2. remove(object)


------------------------------------------------------------
1. remove(index)
------------------------------------------------------------

Removes the element at the specified index.

Example:

    list.remove(1);


------------------------------------------------------------
2. remove(object)
------------------------------------------------------------

Removes the specified object.

Example:

    list.remove("Piyush");


============================================================
              IMPORTANT INTEGER PROBLEM
============================================================

This is a very important interview/MCQ concept.

Suppose:

    ArrayList<Integer> numbers

Then:

    numbers.remove(1);

means:

    REMOVE ELEMENT AT INDEX 1

NOT:

    remove the value 1


To remove the INTEGER value 1:

    numbers.remove(Integer.valueOf(1));


Reason:

remove() has overloaded methods:

    remove(int index)

    remove(Object object)


============================================================
                  SIZE OF ARRAYLIST
============================================================

size() returns the number of elements.

Syntax:

    list.size();


Example:
*/

import java.util.ArrayList;

class SizeExample {

    public static void main(String[] args) {

        ArrayList<Integer> numbers = new ArrayList<>();

        numbers.add(10);
        numbers.add(20);
        numbers.add(30);

        System.out.println(numbers.size());
    }
}


/*
Output:

3


IMPORTANT:

Array:

    array.length

ArrayList:

    arrayList.size()


============================================================
                 CHECK EMPTY
============================================================

isEmpty() checks whether the ArrayList contains
zero elements.

Returns:

    true  → empty
    false → not empty

Example:
*/

import java.util.ArrayList;

class EmptyExample {

    public static void main(String[] args) {

        ArrayList<Integer> numbers = new ArrayList<>();

        System.out.println(numbers.isEmpty());

        numbers.add(10);

        System.out.println(numbers.isEmpty());
    }
}


/*
Output:

true
false


============================================================
                  SEARCH ELEMENT
============================================================

contains() checks whether an element exists.

Returns:

    true
    false


Example:
*/

import java.util.ArrayList;

class ContainsExample {

    public static void main(String[] args) {

        ArrayList<String> names = new ArrayList<>();

        names.add("Piyush");
        names.add("Rahul");

        System.out.println(names.contains("Piyush"));
        System.out.println(names.contains("Aman"));
    }
}


/*
Output:

true
false


============================================================
                    indexOf()
============================================================

indexOf() returns the index of the FIRST occurrence
of an element.

Example:

    [10, 20, 30, 20]

indexOf(20)

returns:

    1


============================================================
                   lastIndexOf()
============================================================

lastIndexOf() returns the index of the LAST occurrence
of an element.

Example:

    [10, 20, 30, 20]

lastIndexOf(20)

returns:

    3


============================================================
                     clear()
============================================================

clear() removes ALL elements from the ArrayList.

Example:

    [10, 20, 30]

after:

    clear()

result:

    []


IMPORTANT:

clear() does not delete the ArrayList object itself.

It removes its elements.


============================================================
                   ITERATING
============================================================

There are several ways to iterate through an ArrayList.

1. Normal for loop
2. Enhanced for loop
3. Iterator
4. ListIterator
5. forEach()


============================================================
              1. NORMAL FOR LOOP
============================================================
*/

import java.util.ArrayList;

class LoopExample {

    public static void main(String[] args) {

        ArrayList<String> names = new ArrayList<>();

        names.add("Piyush");
        names.add("Rahul");
        names.add("Aman");

        for (int i = 0; i < names.size(); i++) {

            System.out.println(names.get(i));
        }
    }
}


/*
============================================================
             2. ENHANCED FOR LOOP
============================================================
*/

import java.util.ArrayList;

class EnhancedLoopExample {

    public static void main(String[] args) {

        ArrayList<String> names = new ArrayList<>();

        names.add("Piyush");
        names.add("Rahul");
        names.add("Aman");

        for (String name : names) {

            System.out.println(name);
        }
    }
}


/*
============================================================
                    ITERATOR
============================================================

Iterator is used to traverse elements of a collection.

Important methods:

    hasNext()
    next()
    remove()


hasNext()
----------
Checks whether another element exists.

next()
------
Returns the next element.

Example:
*/

import java.util.ArrayList;
import java.util.Iterator;

class IteratorExample {

    public static void main(String[] args) {

        ArrayList<String> names = new ArrayList<>();

        names.add("Piyush");
        names.add("Rahul");
        names.add("Aman");

        Iterator<String> it = names.iterator();

        while (it.hasNext()) {

            System.out.println(it.next());
        }
    }
}


/*
============================================================
                  GENERICS
============================================================

Generics allow us to specify what type of data an
ArrayList can store.

Example:

    ArrayList<String>

can store only Strings.

    ArrayList<Integer>

can store only Integers.

Advantages:

1. Type safety
2. No unnecessary casting
3. Errors are detected at compile time
4. Cleaner code


Example:
*/

import java.util.ArrayList;

class GenericExample {

    public static void main(String[] args) {

        ArrayList<String> names = new ArrayList<>();

        names.add("Piyush");
        names.add("Rahul");

        // names.add(10);   // Compile-time error
    }
}


/*
============================================================
            ARRAYLIST CONSTRUCTORS
============================================================

ArrayList provides constructors to create an ArrayList.


1. No-argument constructor:

    ArrayList<Integer> list =
        new ArrayList<>();


2. Initial capacity:

    ArrayList<Integer> list =
        new ArrayList<>(20);


3. Collection constructor:

    ArrayList<Integer> list =
        new ArrayList<>(anotherCollection);


============================================================
             SIZE vs CAPACITY
============================================================

This is an important concept.

SIZE:
------
Number of elements currently stored.

CAPACITY:
---------
Amount of space available internally before the internal
storage needs to grow.

Example:

    ArrayList<Integer> list =
        new ArrayList<>(10);

Here:

    initial capacity = 10
    current size = 0


After adding 3 elements:

    size = 3
    capacity is still at least enough for those elements.


IMPORTANT:

size and capacity are NOT the same thing.


============================================================
             INTERNAL WORKING OF ARRAYLIST
============================================================

ArrayList internally uses a dynamic array.

Conceptually:

    ArrayList
       |
       ↓
   internal array
       |
    ----------------
    | 10 | 20 | 30 |
    ----------------

When the internal array becomes full and we add another
element:

    old array
       ↓
    [10][20][30]
          |
          | resize
          ↓
    larger array
    [10][20][30][40][...]


The ArrayList creates a larger internal array and copies
the old elements into it.

Therefore, ArrayList can grow dynamically.


IMPORTANT:
----------
The exact resizing policy is an implementation detail and
should not be relied upon as a fixed percentage for all
Java versions.


============================================================
             ARRAYLIST TIME COMPLEXITY
============================================================

Access by index:

    get(index)

Average:
    O(1)


Update by index:

    set(index, value)

    O(1)


Add at end:

    add(value)

Usually:
    O(1) amortized


Add at specific index:

    add(index, value)

    O(n)

because elements may need to be shifted.


Remove by index:

    remove(index)

    O(n)

because elements may need to be shifted.


Search:

    contains()
    indexOf()

    O(n)

because ArrayList generally searches sequentially.


============================================================
            ARRAYLIST VS NORMAL ARRAY
============================================================

Array:
------

1. Fixed size.
2. Can store primitives directly.
3. Uses [] syntax.
4. length gives size.
5. Fewer built-in methods.


ArrayList:
----------

1. Dynamic size.
2. Stores objects, not primitives directly.
3. Uses methods such as add(), remove(), get().
4. size() gives number of elements.
5. Many built-in methods.
6. Part of Collection Framework.


Example:

Array:

    int[] numbers = new int[5];


ArrayList:

    ArrayList<Integer> numbers =
        new ArrayList<>();


============================================================
          ARRAYLIST VS LINKEDLIST
============================================================

ArrayList:
----------

Uses dynamic array internally.

Good for:
    Random access
    get(index)

Access:
    Fast


LinkedList:
-----------

Uses linked nodes internally.

Good for:
    Frequent insertions/deletions at appropriate
    positions when node references are available.


Basic comparison:

                    ArrayList       LinkedList
                    ---------       ----------
Internal structure  Dynamic array   Linked nodes

get(index)          Fast            Slower

Random access       Better          Worse

Memory               Generally       Generally
                     less overhead   more overhead

Insertion/deletion   Can require     Can be efficient
                     shifting        after locating node


For most general-purpose List usage, ArrayList is often
the first choice.


============================================================
              ARRAYLIST AND NULL
============================================================

ArrayList allows null values.

Example:
*/

import java.util.ArrayList;

class NullExample {

    public static void main(String[] args) {

        ArrayList<String> names = new ArrayList<>();

        names.add("Piyush");
        names.add(null);
        names.add("Rahul");

        System.out.println(names);
    }
}


/*
Output:

[Piyush, null, Rahul]


============================================================
              ARRAYLIST AND DUPLICATES
============================================================

ArrayList allows duplicate elements.

Example:
*/

import java.util.ArrayList;

class DuplicateExample {

    public static void main(String[] args) {

        ArrayList<Integer> numbers = new ArrayList<>();

        numbers.add(10);
        numbers.add(20);
        numbers.add(10);
        numbers.add(20);

        System.out.println(numbers);
    }
}


/*
Output:

[10, 20, 10, 20]


============================================================
             SORTING AN ARRAYLIST
============================================================

Collections.sort() can be used to sort a List.

Example:
*/

import java.util.ArrayList;
import java.util.Collections;

class SortExample {

    public static void main(String[] args) {

        ArrayList<Integer> numbers = new ArrayList<>();

        numbers.add(50);
        numbers.add(10);
        numbers.add(30);
        numbers.add(20);

        Collections.sort(numbers);

        System.out.println(numbers);
    }
}


/*
Output:

[10, 20, 30, 50]


============================================================
                  REVERSE
============================================================

Collections.reverse() reverses the order.

Example:
*/

import java.util.ArrayList;
import java.util.Collections;

class ReverseExample {

    public static void main(String[] args) {

        ArrayList<Integer> numbers = new ArrayList<>();

        numbers.add(10);
        numbers.add(20);
        numbers.add(30);

        Collections.reverse(numbers);

        System.out.println(numbers);
    }
}


/*
Output:

[30, 20, 10]


============================================================
            ARRAYLIST TO ARRAY
============================================================

An ArrayList can be converted to an array.

Example:

    list.toArray()

For a typed array:

    list.toArray(new String[0])


============================================================
            ARRAY TO ARRAYLIST
============================================================

Arrays.asList() can be used to create a List view from
an array.

Example:

    Arrays.asList(array)

IMPORTANT:
----------
The list returned by Arrays.asList() has a fixed size.

It supports replacing elements using set(), but adding
or removing elements causes UnsupportedOperationException.

If a fully modifiable ArrayList is needed:

    new ArrayList<>(Arrays.asList(array))


============================================================
              ARRAYLIST IS NOT THREAD-SAFE
============================================================

ArrayList is NOT synchronized by default.

Therefore, it is not inherently thread-safe for concurrent
modification by multiple threads.

If synchronized access is required, one option is:

    Collections.synchronizedList(list)

For modern concurrent programming, the appropriate
concurrent collection should be chosen based on the
specific requirement.


============================================================
            ARRAYLIST IMPORTANT METHODS
============================================================

add(element)
    → Adds element at the end.

add(index, element)
    → Adds element at specified index.

get(index)
    → Returns element at index.

set(index, element)
    → Replaces element.

remove(index)
    → Removes element at index.

remove(object)
    → Removes specified object.

size()
    → Returns number of elements.

isEmpty()
    → Checks whether list is empty.

contains(object)
    → Checks whether object exists.

indexOf(object)
    → Returns first occurrence index.

lastIndexOf(object)
    → Returns last occurrence index.

clear()
    → Removes all elements.

iterator()
    → Returns Iterator.

toArray()
    → Converts list to array.


============================================================
              ARRAYLIST COMPLETE EXAMPLE
============================================================
*/

import java.util.ArrayList;
import java.util.Collections;

class CompleteArrayListExample {

    public static void main(String[] args) {

        ArrayList<Integer> numbers = new ArrayList<>();

        // ADD
        numbers.add(30);
        numbers.add(10);
        numbers.add(20);
        numbers.add(10);

        // ADD AT INDEX
        numbers.add(1, 50);

        System.out.println(numbers);

        // GET
        System.out.println(numbers.get(0));

        // UPDATE
        numbers.set(0, 100);

        // SIZE
        System.out.println(numbers.size());

        // SEARCH
        System.out.println(numbers.contains(20));

        // FIRST INDEX
        System.out.println(numbers.indexOf(10));

        // LAST INDEX
        System.out.println(numbers.lastIndexOf(10));

        // SORT
        Collections.sort(numbers);

        System.out.println(numbers);

        // REVERSE
        Collections.reverse(numbers);

        System.out.println(numbers);

        // REMOVE BY INDEX
        numbers.remove(0);

        // CLEAR
        // numbers.clear();

        System.out.println(numbers);
    }
}


/*
============================================================
             IMPORTANT EXAM / MCQ POINTS
============================================================

1. ArrayList belongs to:

       java.util

2. ArrayList implements:

       List

3. ArrayList internally uses a dynamic array.

4. ArrayList maintains insertion order.

5. ArrayList allows duplicate elements.

6. ArrayList allows null values.

7. ArrayList supports index-based access.

8. Index starts from 0.

9. ArrayList size is dynamic.

10. ArrayList does NOT store primitive types directly.

11. Use wrapper classes:

       Integer
       Double
       Character
       Boolean
       etc.

12. ArrayList<Integer> is valid.

13. ArrayList<int> is invalid.

14. get() is used to access an element.

15. set() is used to replace an element.

16. add() is used to add an element.

17. remove() is used to remove an element.

18. size() returns the number of elements.

19. isEmpty() returns true if there are no elements.

20. contains() checks whether an element exists.

21. indexOf() returns the first matching index.

22. lastIndexOf() returns the last matching index.

23. clear() removes all elements.

24. ArrayList is not synchronized by default.

25. ArrayList is generally good for random access.

26. get(index) is O(1) average.

27. Searching is O(n).

28. Insertion/removal in the middle can be O(n).

29. Adding at the end is O(1) amortized.

30. ArrayList allows duplicate values.

31. ArrayList maintains insertion order.

32. Collection is an interface.

33. Collections is a utility class.

34. List is an interface.

35. ArrayList is a class.

36. ArrayList is a List implementation.

37. List allows duplicates.

38. List maintains order.

39. Map does NOT extend Collection.

40. ArrayList can be sorted using Collections.sort().


============================================================
          MOST IMPORTANT TRICK QUESTIONS
============================================================

QUESTION 1:

    ArrayList<Integer> list =
        new ArrayList<>();

    list.add(10);
    list.add(20);
    list.add(30);

    list.remove(1);

What happens?

ANSWER:

    Element at index 1 is removed.

Before:

    [10, 20, 30]
        ↑
      index 1

After:

    [10, 30]


------------------------------------------------------------

QUESTION 2:

How do we remove the VALUE 1 from:

    ArrayList<Integer> list

Use:

    list.remove(Integer.valueOf(1));


------------------------------------------------------------

QUESTION 3:

Does ArrayList allow duplicates?

YES.


------------------------------------------------------------

QUESTION 4:

Does ArrayList maintain insertion order?

YES.


------------------------------------------------------------

QUESTION 5:

Does ArrayList allow null?

YES.


------------------------------------------------------------

QUESTION 6:

Can we write:

    ArrayList<int>

NO.

Use:

    ArrayList<Integer>


------------------------------------------------------------

QUESTION 7:

What is the difference?

    array.length

and

    arrayList.size()

Answer:

    array.length
        → array property

    arrayList.size()
        → ArrayList method


------------------------------------------------------------

QUESTION 8:

Which is faster?

    arrayList.get(index)

or searching with contains()?

Random access using get(index) is generally O(1).

contains() is generally O(n).


============================================================
                    QUICK REVISION
============================================================

COLLECTION
    ↓
Group of objects
    ↓
COLLECTION FRAMEWORK
    ↓
-----------------------------
|            |              |
List         Set           Queue
 |
ArrayList
 |
Dynamic Array
 |
Features:
-----------------------------
✓ Dynamic size
✓ Ordered
✓ Allows duplicates
✓ Allows null
✓ Index based
✓ Generic
✓ Object based
✓ Not synchronized by default


IMPORTANT METHODS:

add()
    ↓
Add

get()
    ↓
Access

set()
    ↓
Update

remove()
    ↓
Delete

contains()
    ↓
Search

size()
    ↓
Number of elements

isEmpty()
    ↓
Check empty

clear()
    ↓
Remove everything

indexOf()
    ↓
First occurrence

lastIndexOf()
    ↓
Last occurrence


============================================================
                ONE-LINE MEMORY TRICKS
============================================================

ArrayList
    → Dynamic array

List
    → Ordered + duplicates allowed

get()
    → Get element

set()
    → Set/replace element

add()
    → Add element

remove()
    → Remove element

size()
    → Number of elements

contains()
    → Check existence

clear()
    → Remove all

indexOf()
    → First occurrence

lastIndexOf()
    → Last occurrence

Collection
    → Interface

Collections
    → Utility class

ArrayList<Integer>
    → Wrapper class required

get(index)
    → O(1) average

contains()
    → O(n)


============================================================
                 END OF ARRAYLIST
============================================================
*/