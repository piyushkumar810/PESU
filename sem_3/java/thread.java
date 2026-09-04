/*
===========================================================
                    THREADS IN JAVA
===========================================================

Thread:
-------
A thread is a lightweight unit of execution inside a
program.

A thread allows a program to perform multiple tasks
concurrently.

Example:
    One thread downloads a file.
    Another thread plays music.
    Another thread handles user input.

Multithreading:
---------------
Multithreading means executing multiple threads
concurrently within a single program.

Example:

    Thread 1 → Download file
    Thread 2 → Play music
    Thread 3 → Display progress

All these threads can execute concurrently.


===========================================================
                  WHY USE THREADS?
===========================================================

1. Better CPU utilization
2. Faster execution of independent tasks
3. Improved application responsiveness
4. Multiple tasks can run concurrently
5. Useful for background tasks


===========================================================
              THREAD LIFE CYCLE
===========================================================

A thread generally goes through these states:

        NEW
         |
         | start()
         ↓
      RUNNABLE
         |
         | CPU scheduling
         ↓
      RUNNING
       /    \
      /      \
     ↓        ↓
 WAITING   BLOCKED
     |        |
     |        |
     └──→ RUNNABLE
              |
              ↓
         TERMINATED


Important Thread States:
------------------------

1. NEW
-------
Thread object has been created but start() has not
been called.

2. RUNNABLE
-----------
Thread is ready to run and waiting for CPU time.

3. RUNNING
-----------
Thread is currently executing.

Note:
Java officially combines ready-to-run and running
under the RUNNABLE state in Thread.State.

4. BLOCKED
-----------
Thread is waiting to acquire a monitor lock.

5. WAITING
-----------
Thread waits indefinitely until another thread performs
a particular action.

Methods that can cause WAITING:
    wait()
    join()

6. TIMED_WAITING
----------------
Thread waits for a specified amount of time.

Methods:
    sleep()
    wait(time)
    join(time)

7. TERMINATED
-------------
Thread has completed its execution.


===========================================================
              CREATING A THREAD IN JAVA
===========================================================

There are TWO common ways:

1. Extending Thread class
2. Implementing Runnable interface


===========================================================
       1. EXTENDING THE THREAD CLASS
===========================================================

Steps:
------
1. Create a class that extends Thread.
2. Override run().
3. Create object of the class.
4. Call start().

IMPORTANT:
----------
run() contains the task that the thread performs.

start() creates a new thread and then executes run().

Do NOT normally call run() directly when you want
multithreading.

start() → creates a new thread
run()   → contains the code executed by that thread
*/


class MyThread extends Thread {

    public void run() {
        System.out.println("Thread is running");
    }

    public static void main(String[] args) {

        MyThread t1 = new MyThread();

        t1.start();
    }
}


/*
===========================================================
             2. IMPLEMENTING RUNNABLE
===========================================================

Steps:
------
1. Create a class that implements Runnable.
2. Override run().
3. Create object of the class.
4. Create Thread object.
5. Call start().

Runnable is generally preferred when the class needs to
extend another class because Java does not support
multiple class inheritance.
*/


class MyRunnable implements Runnable {

    public void run() {
        System.out.println("Thread is running");
    }

    public static void main(String[] args) {

        MyRunnable obj = new MyRunnable();

        Thread t1 = new Thread(obj);

        t1.start();
    }
}


/*
===========================================================
             IMPORTANT THREAD METHODS
===========================================================

1. start()
-----------
Starts a new thread.

It internally causes the run() method to execute.

Syntax:
    t1.start();


2. run()
---------
Contains the code that the thread executes.

Calling run() directly does NOT create a new thread.


3. sleep()
----------
Pauses the currently executing thread for a specified
amount of time.

Syntax:
    Thread.sleep(1000);

1000 milliseconds = 1 second.

sleep() is a static method.


4. join()
---------
Makes the current thread wait until another thread
finishes its execution.

Example:
    t1.join();

If main() calls t1.join(), main waits for t1 to finish.


5. getName()
------------
Returns the name of the thread.


6. setName()
------------
Changes the name of the thread.


7. getPriority()
----------------
Returns the priority of a thread.


8. setPriority()
----------------
Sets the priority of a thread.


9. currentThread()
------------------
Returns the currently executing thread.

Syntax:
    Thread.currentThread();


10. isAlive()
-------------
Checks whether a thread is still alive.

Returns:
    true
    false


===========================================================
                  THREAD PRIORITY
===========================================================

Thread priority tells the scheduler the relative
importance of a thread.

Java provides:

    Thread.MIN_PRIORITY     = 1
    Thread.NORM_PRIORITY    = 5
    Thread.MAX_PRIORITY    = 10

Default priority:
    5

Example:
    t1.setPriority(10);


IMPORTANT:
----------
Thread priority does NOT guarantee which thread will
execute first.

It is only a scheduling hint.


===========================================================
                  DAEMON THREAD
===========================================================

A daemon thread is a background thread.

It generally performs background tasks.

Examples:
    Garbage collection
    Background monitoring

Method:
    setDaemon(true)

IMPORTANT:
----------
setDaemon(true) must be called before start().


===========================================================
                  SYNCHRONIZATION
===========================================================

Problem:
--------
When multiple threads access the same shared resource
at the same time, incorrect results can occur.

This is called a race condition.

Example:

    Thread 1 → increases balance
    Thread 2 → increases balance

Both threads may access the same data simultaneously.

Synchronization:
----------------
Synchronization allows only one thread at a time to
execute a critical section for a particular lock.

It helps prevent race conditions.

Keyword:
    synchronized

Example:
*/


class Counter {

    int count = 0;

    synchronized void increment() {
        count++;
    }
}


/*
===========================================================
                 CRITICAL SECTION
===========================================================

Critical section:
-----------------
The part of a program where shared resources are accessed
or modified.

Example:
    count++;
    balance = balance + 100;

Synchronization is commonly used to protect critical
sections.


===========================================================
              THREAD COMMUNICATION
===========================================================

Thread communication means allowing one thread to
communicate or coordinate with another thread.

Java provides three important methods:

1. wait()
2. notify()
3. notifyAll()

These methods belong to the Object class.


===========================================================
                      wait()
===========================================================

wait():
-------
Causes the current thread to wait until another thread
notifies it.

When wait() is called:

    1. Thread enters WAITING state.
    2. Thread releases the object's monitor lock.
    3. Another thread can acquire the lock.
    4. Thread waits for notification.

Important:
----------
wait() must be called while the thread owns the object's
monitor, usually inside synchronized code.


===========================================================
                    notify()
===========================================================

notify():
---------
Wakes up one thread that is waiting on the same object's
monitor.

If multiple threads are waiting, only one waiting thread
is selected to wake up.


===========================================================
                  notifyAll()
===========================================================

notifyAll():
------------
Wakes up all threads waiting on the same object's monitor.

After being awakened, the threads compete to acquire
the monitor lock.


===========================================================
             WAIT() vs SLEEP()
===========================================================

wait():
-------
1. Belongs to Object class.
2. Releases the lock.
3. Used for thread communication.
4. Usually used inside synchronized block/method.
5. Can wait until notify()/notifyAll().


sleep():
--------
1. Belongs to Thread class.
2. Does NOT release the lock held by the thread.
3. Used for pausing execution.
4. Does not require synchronized code.
5. Waits for specified time.


===========================================================
             WAIT() / NOTIFY() EXAMPLE
===========================================================
*/


class Communication {

    synchronized void waitingMethod() {

        try {
            System.out.println("Thread is waiting");

            wait();

            System.out.println("Thread resumed");

        } catch (InterruptedException e) {
            System.out.println("Interrupted");
        }
    }

    synchronized void notifyingMethod() {

        System.out.println("Sending notification");

        notify();
    }
}


/*
===========================================================
              PRODUCER-CONSUMER CONCEPT
===========================================================

Producer:
---------
Produces data and puts it into a shared resource.

Consumer:
---------
Takes data from the shared resource.

Problem:
--------
If the resource is empty, consumer should wait.

If the resource is full, producer should wait.

Thread communication using:

    wait()
    notify()
    notifyAll()

can be used to coordinate producer and consumer.


Example:

    Producer
       |
       ↓
   Shared Buffer
       |
       ↓
    Consumer

Producer → produces data
Consumer → consumes data


===========================================================
                 RACE CONDITION
===========================================================

Race condition:
---------------
A race condition occurs when multiple threads access
shared data at the same time and the final result depends
on the order in which the threads execute.

Example:

    int count = 0;

    Thread 1 → count++
    Thread 2 → count++

Without synchronization, the expected result may not
always be obtained.

Solution:
    synchronized


===========================================================
             DEADLOCK
===========================================================

Deadlock:
---------
A deadlock occurs when two or more threads wait forever
for resources/locks held by each other.

Example:

    Thread 1 holds Lock A
        ↓
    waits for Lock B

    Thread 2 holds Lock B
        ↓
    waits for Lock A

Neither thread can continue.

        Thread 1
        Lock A
           ↓
       waits for
        Lock B
           ↑
       held by
        Thread 2

This creates a deadlock.


===========================================================
       MULTITHREADING vs MULTITASKING
===========================================================

Multitasking:
-------------
Running multiple processes/tasks.

Example:
    Browser + Music Player + Calculator


Multithreading:
---------------
Running multiple threads within a process.

Example:
    Browser:
        Thread 1 → UI
        Thread 2 → Download
        Thread 3 → Network


===========================================================
            THREAD vs PROCESS
===========================================================

Process:
--------
An independent program in execution.

Thread:
-------
A lightweight unit of execution inside a process.

One process can have multiple threads.

Example:

    Process
       |
       |---- Thread 1
       |---- Thread 2
       |---- Thread 3


===========================================================
                 IMPORTANT MCQ POINTS
===========================================================

1. A thread is a lightweight unit of execution.

2. Multithreading means executing multiple threads
   concurrently.

3. Thread class belongs to:
       java.lang

4. Runnable interface belongs to:
       java.lang

5. run() contains the task performed by a thread.

6. start() starts a new thread.

7. Calling run() directly does NOT create a new thread.

8. sleep() is a static method of Thread class.

9. sleep() does NOT release the lock.

10. wait() belongs to Object class.

11. wait() releases the object's monitor lock.

12. notify() wakes one waiting thread.

13. notifyAll() wakes all waiting threads.

14. wait(), notify(), and notifyAll() are used for
    thread communication.

15. wait(), notify(), and notifyAll() are methods of
    Object class.

16. synchronized is used to control access to shared
    resources.

17. Synchronization helps prevent race conditions.

18. Thread priority ranges from 1 to 10.

19. MIN_PRIORITY = 1.

20. NORM_PRIORITY = 5.

21. MAX_PRIORITY = 10.

22. Default thread priority is 5.

23. Thread priority does not guarantee execution order.

24. join() makes the current thread wait for another
    thread to finish.

25. isAlive() checks whether a thread is alive.

26. currentThread() returns the currently executing
    thread.

27. setDaemon(true) creates a daemon thread.

28. setDaemon(true) must be called before start().

29. Deadlock means threads wait forever for each other's
    locks/resources.

30. Race condition occurs due to unsafe concurrent access
    to shared data.

31. Runnable is an interface.

32. Thread is a class.

33. Java supports multithreading.

34. Java does not support multiple inheritance of classes,
    so implementing Runnable can be useful when a class
    already needs to extend another class.


===========================================================
              MOST IMPORTANT DIFFERENCES
===========================================================

              start()              run()
              -------              -----

Creates a new thread       Does not create a new thread

Calls run() internally     Executes like a normal method

Used for                   Used to define
multithreading             thread's task


-----------------------------------------------------------

              wait()               sleep()
              ------               -------

Object class               Thread class

Releases lock              Does not release lock

Thread communication       Pauses thread

Needs monitor/             No synchronized requirement
synchronized context

Can be resumed by          Automatically resumes after
notify/notifyAll            specified time


-----------------------------------------------------------

             notify()             notifyAll()
             --------             ----------

Wakes one waiting          Wakes all waiting
thread                     threads

Used for communication    Used for communication


===========================================================
                    QUICK REVISION
===========================================================

THREAD
  ↓
Lightweight unit of execution
  ↓
MULTITHREADING
  ↓
Multiple threads execute concurrently
  ↓
THREAD CREATION
  ↓
-------------------------
|                       |
extends Thread      implements Runnable
  |
run()
  |
start()
  ↓
THREAD COMMUNICATION
  ↓
---------------------------
|          |              |
wait()    notify()    notifyAll()
  ↓
Synchronization
  ↓
synchronized
  ↓
Prevents race conditions

===========================================================
*/