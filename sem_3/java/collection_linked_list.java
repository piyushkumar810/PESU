/*
============================================================
                  LINKEDLIST IN JAVA
============================================================

LinkedList:
-----------

LinkedList is a class in Java that implements the List
and Deque interfaces.

Package:

    java.util.LinkedList


LinkedList stores elements using LINKED NODES.

Unlike ArrayList, which uses a dynamic array, LinkedList
uses nodes connected to each other.


============================================================
              BASIC STRUCTURE OF LINKEDLIST
============================================================

Conceptually, a LinkedList looks like:

    [10] <-> [20] <-> [30] <-> [40]

Each node contains:

    1. Data
    2. Reference to the previous node
    3. Reference to the next node

Conceptually:

    [prev | data | next]

Because each node is connected to another node, we call
it a LINKED LIST.


============================================================
             TYPES OF LINKED LIST
============================================================

Common types of linked lists are:

1. Singly Linked List
2. Doubly Linked List
3. Circular Linked List


Java's LinkedList is based on a DOUBLY LINKED LIST.

Conceptually:

    null
     ↓
    [10] <-> [20] <-> [30] <-> [40]
                                  ↓
                                 null


============================================================
             ARRAYLIST vs LINKEDLIST
============================================================

ArrayList:
----------

Uses a dynamic array.

    [10][20][30][40]


LinkedList:
-----------

Uses linked nodes.

    [10] <-> [20] <-> [30] <-> [40]


Main difference:

    ArrayList → Dynamic Array

    LinkedList → Doubly Linked List


============================================================
             CREATING A LINKEDLIST
============================================================

Syntax:

    LinkedList<DataType> list =
        new LinkedList<>();


Example:
*/

// import java.util.LinkedList;

// class LinkedListExample {

//     public static void main(String[] args) {

//         LinkedList<Integer> numbers =
//             new LinkedList<>();

//         numbers.add(10);
//         numbers.add(20);
//         numbers.add(30);

//         System.out.println(numbers);
//     }
// }


/*
Output:

[10, 20, 30]


============================================================
              FEATURES OF LINKEDLIST
============================================================

1. Maintains insertion order.

2. Allows duplicate elements.

3. Allows null values.

4. Dynamic size.

5. Supports index-based access.

6. Implements List.

7. Implements Deque.

8. Can be used as a Queue.

9. Can be used as a Stack-like structure.

10. Internally uses a doubly linked list.

11. Not synchronized by default.


============================================================
                  ADD ELEMENT
============================================================

add() adds an element to the end.

Example:
*/

// import java.util.LinkedList;

// class LinkedAddExample {

//     public static void main(String[] args) {

//         LinkedList<String> names =
//             new LinkedList<>();

//         names.add("Piyush");
//         names.add("Rahul");
//         names.add("Aman");

//         System.out.println(names);
//     }
// }


/*
Output:

[Piyush, Rahul, Aman]


============================================================
          ADD ELEMENT AT SPECIFIC INDEX
============================================================

Syntax:

    list.add(index, element)

Example:
*/

// import java.util.LinkedList;

// class LinkedAddIndexExample {

//     public static void main(String[] args) {

//         LinkedList<String> names =
//             new LinkedList<>();

//         names.add("Piyush");
//         names.add("Rahul");

//         names.add(1, "Aman");

//         System.out.println(names);
//     }
// }


/*
Output:

[Piyush, Aman, Rahul]


============================================================
                    get()
============================================================

get(index) returns the element at the specified index.

Example:

    list.get(0)

IMPORTANT:

Unlike ArrayList, LinkedList does NOT provide fast
random access.

To reach an index, LinkedList may need to traverse
the nodes.

Therefore:

    get(index) → O(n)


============================================================
                    set()
============================================================

set() replaces an existing element.

Syntax:

    list.set(index, value)

Example:
*/

// import java.util.LinkedList;

// class LinkedSetExample {

//     public static void main(String[] args) {

//         LinkedList<String> names =
//             new LinkedList<>();

//         names.add("Piyush");
//         names.add("Rahul");

//         names.set(1, "Rohit");

//         System.out.println(names);
//     }
// }


/*
Output:

[Piyush, Rohit]


============================================================
                   remove()
============================================================

LinkedList supports remove().

Examples:

    list.remove(1)

    list.remove("Piyush")


remove(index)
    → Removes element at index.

remove(object)
    → Removes specified object.


============================================================
                  FIRST ELEMENT
============================================================

LinkedList provides special methods for the first element:

    addFirst()
    getFirst()
    removeFirst()


Example:
*/

// import java.util.LinkedList;

// class FirstExample {

//     public static void main(String[] args) {

//         LinkedList<Integer> numbers =
//             new LinkedList<>();

//         numbers.add(20);
//         numbers.add(30);

//         numbers.addFirst(10);

//         System.out.println(numbers);

//         System.out.println(numbers.getFirst());

//         numbers.removeFirst();

//         System.out.println(numbers);
//     }
// }


/*
Output:

[10, 20, 30]
10
[20, 30]


============================================================
                  LAST ELEMENT
============================================================

LinkedList also provides:

    addLast()
    getLast()
    removeLast()


Example:
*/

// import java.util.LinkedList;

// class LastExample {

//     public static void main(String[] args) {

//         LinkedList<Integer> numbers =
//             new LinkedList<>();

//         numbers.add(10);
//         numbers.add(20);

//         numbers.addLast(30);

//         System.out.println(numbers);

//         System.out.println(numbers.getLast());

//         numbers.removeLast();

//         System.out.println(numbers);
//     }
// }


/*
Output:

[10, 20, 30]
30
[10, 20]


============================================================
              LINKEDLIST AS A DEQUE
============================================================

Deque means:

    Double Ended Queue

It allows insertion and removal from BOTH ends.

LinkedList implements Deque.

Therefore we can use:

    addFirst()
    addLast()

    removeFirst()
    removeLast()

    getFirst()
    getLast()


Conceptually:

        FRONT                  REAR
          ↓                      ↓
    [10] <-> [20] <-> [30] <-> [40]
      ↑                          ↑
    first                       last


============================================================
              LINKEDLIST AS A QUEUE
============================================================

A Queue generally follows:

    FIFO

FIFO:

    First In
    First Out


Example:

    Add:
    10 → 20 → 30

    Remove:
    10 first
    then 20
    then 30


LinkedList can be used as a Queue because it implements
the Queue interface.


Important Queue methods:

    offer()
    poll()
    peek()


============================================================
              offer()
============================================================

offer() adds an element to the queue.

Example:
*/

// import java.util.LinkedList;
// import java.util.Queue;

// class QueueExample {

//     public static void main(String[] args) {

//         Queue<Integer> queue =
//             new LinkedList<>();

//         queue.offer(10);
//         queue.offer(20);
//         queue.offer(30);

//         System.out.println(queue);
//     }
// }


/*
Output:

[10, 20, 30]


============================================================
                    poll()
============================================================

poll() removes and returns the HEAD element.

Example:

    [10, 20, 30]

    poll()

returns:

    10

Remaining:

    [20, 30]


IMPORTANT:

poll() returns null if the queue is empty.


============================================================
                    peek()
============================================================

peek() returns the HEAD element without removing it.

Example:

    [10, 20, 30]

    peek()

returns:

    10

List remains:

    [10, 20, 30]


IMPORTANT:

peek() returns null if the queue is empty.


============================================================
             QUEUE EXAMPLE
============================================================
*/

// import java.util.LinkedList;
// import java.util.Queue;

// class QueueMethodsExample {

//     public static void main(String[] args) {

//         Queue<Integer> queue =
//             new LinkedList<>();

//         queue.offer(10);
//         queue.offer(20);
//         queue.offer(30);

//         System.out.println(queue);

//         System.out.println(queue.peek());

//         System.out.println(queue);

//         System.out.println(queue.poll());

//         System.out.println(queue);
//     }
// }


/*
Output:

[10, 20, 30]
10
[10, 20, 30]
10
[20, 30]


============================================================
              LINKEDLIST AS A STACK
============================================================

Stack generally follows:

    LIFO

LIFO:

    Last In
    First Out


LinkedList can perform stack-like operations using:

    push()
    pop()
    peek()


Example:

    push(10)
    push(20)
    push(30)

Stack:

    [30]
    [20]
    [10]

pop():

    30 is removed first.


============================================================
             STACK-LIKE EXAMPLE
============================================================
*/

// import java.util.LinkedList;

// class StackLikeExample {

//     public static void main(String[] args) {

//         LinkedList<Integer> stack =
//             new LinkedList<>();

//         stack.push(10);
//         stack.push(20);
//         stack.push(30);

//         System.out.println(stack);

//         System.out.println(stack.pop());

//         System.out.println(stack);
//     }
// }


/*
Output:

[30, 20, 10]
30
[20, 10]


============================================================
            IMPORTANT LINKEDLIST METHODS
============================================================

add(element)
    → Adds at the end.

add(index, element)
    → Adds at specified index.

addFirst(element)
    → Adds at beginning.

addLast(element)
    → Adds at end.

get(index)
    → Gets element at index.

getFirst()
    → Gets first element.

getLast()
    → Gets last element.

set(index, element)
    → Replaces element.

remove(index)
    → Removes element at index.

remove(object)
    → Removes specified object.

removeFirst()
    → Removes first element.

removeLast()
    → Removes last element.

size()
    → Number of elements.

contains(object)
    → Checks whether element exists.

clear()
    → Removes all elements.

peek()
    → Returns first/head element without removing.

poll()
    → Removes and returns first/head element.

offer(element)
    → Adds element to queue.

push(element)
    → Adds element to front.

pop()
    → Removes and returns first element.


============================================================
          ARRAYLIST vs LINKEDLIST
============================================================

                    ArrayList       LinkedList
                    ---------       ----------

Internal structure  Dynamic array   Doubly linked list

Random access       Fast            Slow

get(index)          O(1)            O(n)

Add at end          O(1) amortized  O(1)

Add at beginning    O(n)            O(1)

Remove beginning    O(n)            O(1)

Memory               Usually less    Usually more

Implements List     YES             YES

Implements Deque    NO              YES

Duplicates          YES             YES

Null                YES             YES

Insertion order     YES             YES

Dynamic size        YES             YES


IMPORTANT:

Do not simply say:

"LinkedList is always faster for insertion."

More accurately, insertion/removal can be efficient once
the relevant node position is known, but finding a position
by index can itself take O(n).


============================================================
                WHEN TO USE ARRAYLIST?
============================================================

Use ArrayList when:

1. You frequently access elements using index.

2. You mostly add elements at the end.

3. You need fast random access.

4. You don't frequently insert/remove elements from the
   beginning or middle.


Example:

    Student records
    Product list
    List of names


============================================================
               WHEN TO USE LINKEDLIST?
============================================================

LinkedList can be useful when:

1. You need frequent insertion/removal at the ends.

2. You need Deque operations.

3. You need Queue-like operations.

4. You need both List and Deque functionality.

For general random-access list usage, ArrayList is often
the better choice.


============================================================
               LINKEDLIST AND NULL
============================================================

LinkedList allows null values.

Example:
*/

// import java.util.LinkedList;

// class LinkedNullExample {

//     public static void main(String[] args) {

//         LinkedList<String> names =
//             new LinkedList<>();

//         names.add("Piyush");
//         names.add(null);
//         names.add("Rahul");

//         System.out.println(names);
//     }
// }


/*
Output:

[Piyush, null, Rahul]


============================================================
             LINKEDLIST AND DUPLICATES
============================================================

LinkedList allows duplicate elements.

Example:
*/

// import java.util.LinkedList;

// class LinkedDuplicateExample {

//     public static void main(String[] args) {

//         LinkedList<Integer> numbers =
//             new LinkedList<>();

//         numbers.add(10);
//         numbers.add(20);
//         numbers.add(10);

//         System.out.println(numbers);
//     }
// }


/*
Output:

[10, 20, 10]


============================================================
                 LINKEDLIST GENERICS
============================================================

Generics specify the type of elements.

Example:

    LinkedList<String>

    LinkedList<Integer>

    LinkedList<Double>


Primitive types cannot be used directly.

Wrong:

    LinkedList<int>

Correct:

    LinkedList<Integer>


============================================================
             LINKEDLIST TIME COMPLEXITY
============================================================

Access by index:

    get(index)

    O(n)


Search:

    contains()
    indexOf()

    O(n)


Add at beginning:

    addFirst()

    O(1)


Remove from beginning:

    removeFirst()

    O(1)


Add at end:

    addLast()

    O(1)


Remove from end:

    removeLast()

    O(1)


Insertion/removal after locating a node:

    O(1)

But finding that node by index may take O(n).


============================================================
              LINKEDLIST THREAD SAFETY
============================================================

LinkedList is NOT synchronized by default.

Therefore, it is not inherently thread-safe for concurrent
modification by multiple threads.


============================================================
                  IMPORTANT MCQs
============================================================

1. LinkedList belongs to:

       java.util


2. LinkedList implements:

       List
       Deque


3. Java's LinkedList is based on:

       Doubly linked list


4. LinkedList maintains:

       Insertion order


5. LinkedList allows:

       Duplicate elements


6. LinkedList allows:

       null values


7. LinkedList supports:

       Dynamic size


8. LinkedList provides:

       Index-based access


9. get(index) in LinkedList is generally:

       O(n)


10. addFirst() is generally:

       O(1)


11. removeFirst() is generally:

       O(1)


12. LinkedList can be used as:

       List
       Queue
       Deque
       Stack-like structure


13. Queue follows:

       FIFO


14. Stack follows:

       LIFO


15. peek():

       Returns head without removing it.


16. poll():

       Removes and returns head.


17. offer():

       Adds an element to the queue.


18. push():

       Adds an element to the front.


19. pop():

       Removes and returns the first element.


20. LinkedList is:

       Not synchronized by default.


21. ArrayList is better for:

       Random access.


22. LinkedList can be better for:

       Frequent operations at the ends.


23. ArrayList uses:

       Dynamic array.


24. LinkedList uses:

       Doubly linked list.


============================================================
           VERY IMPORTANT INTERVIEW QUESTION
============================================================

QUESTION:

Why is ArrayList faster than LinkedList for get(index)?

ANSWER:

ArrayList stores elements in an array-like structure.

Therefore, it can directly calculate/access the position
using the index.

So:

    ArrayList get(index)
        → O(1)


LinkedList stores nodes.

To reach a particular index, it may need to traverse
through nodes.

So:

    LinkedList get(index)
        → O(n)


============================================================
             ANOTHER IMPORTANT QUESTION
============================================================

QUESTION:

Why does LinkedList use more memory than ArrayList?

ANSWER:

ArrayList mainly stores the elements in an internal array.

LinkedList nodes need additional references for links
between nodes.

Conceptually:

    LinkedList node:

    [previous | data | next]

Therefore, LinkedList generally has more memory overhead.


============================================================
                QUICK REVISION
============================================================

                    LIST
                     |
             ------------------
             |                |
         ArrayList        LinkedList
             |                |
       Dynamic array    Doubly linked list
             |                |
       Fast get(index)  Slower get(index)
             |                |
       Good random      Good operations
       access            at ends
                              |
                         Also implements
                              |
                            Deque
                              |
                    -----------------------
                    |          |          |
                  Queue      Deque    Stack-like


============================================================
                 MEMORY TRICK
============================================================

ArrayList:

    ARRAY → FAST ACCESS

LinkedList:

    LINKS → EASY END OPERATIONS


Queue:

    FIFO

    First In → First Out


Stack:

    LIFO

    Last In → First Out


Deque:

    Double Ended Queue

    Add/remove from both ends.


============================================================
               FINAL COMPARISON
============================================================

ArrayList
    ↓
Dynamic Array
    ↓
Fast index access
    ↓
O(1) get()
    ↓
Good for reading/accessing


LinkedList
    ↓
Doubly Linked List
    ↓
Slower index access
    ↓
O(n) get()
    ↓
O(1) operations at ends
    ↓
Also supports Queue/Deque operations


============================================================
                    END
============================================================
*/