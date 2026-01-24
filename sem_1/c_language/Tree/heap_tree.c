#include <stdio.h>

// Swap two elements using pointers
void swap(int *a, int *b) {
    int temp = *a;   // store value of a
    *a = *b;         // put b into a
    *b = temp;       // put temp (old a) into b
}

// Heapify UP (used during insertion)
void upheapify(int heap[], int index) {
    int parent = (index - 1) / 2;

    // Move up until heap property is restored
    while (index > 0 && heap[parent] < heap[index]) {
        swap(&heap[parent], &heap[index]);
        index = parent;
        parent = (index - 1) / 2;
    }
}

// Insert element into Max Heap
void insert(int heap[], int *size, int value) {
    heap[*size] = value;       // insert at last position
    upheapify(heap, *size);    // fix heap property
    (*size)++;                 // increase heap size
}

// Heapify DOWN (used during deletion / heap sort)
void downheapify(int heap[], int size, int index) {
    int largest = index;
    int left = 2 * index + 1;
    int right = 2 * index + 2;

    if (left < size && heap[left] > heap[largest])
        largest = left;

    if (right < size && heap[right] > heap[largest])
        largest = right;

    if (largest != index) {
        swap(&heap[index], &heap[largest]);
        downheapify(heap, size, largest);
    }
}

// Print Heap (Level Order)
void printHeap(int heap[], int size) {
    printf("Max Heap: ");
    for (int i = 0; i < size; i++)
        printf("%d ", heap[i]);
    printf("\n");
}

int main() {
    int heap[100];
    int size = 0;

    insert(heap, &size, 10);
    insert(heap, &size, 20);
    insert(heap, &size, 15);
    insert(heap, &size, 30);
    insert(heap, &size, 40);

    printHeap(heap, size);

    return 0;
}


/*
✅ STEP 2: EXPLAIN EVERYTHING (PICTURIZED 🧠)
🌳 WHAT IS A HEAP (FIRST CONCEPT)

A heap is:

Complete Binary Tree

Follows Heap Property

MAX HEAP PROPERTY

👉 Parent ≥ Children

        40
       /  \
     30    20
    /  \
  10   15

🧠 WHY ARRAY IS USED FOR HEAP

Because heap is a complete binary tree.

Array mapping (0-based indexing):

Index:   0   1   2   3   4
Value:  40  30  20  10  15

FORMULAS (VERY IMPORTANT)

If node is at index i:

Relation	Formula
Parent	(i - 1) / 2
Left Child	2*i + 1
Right Child	2*i + 2
🔁 swap() FUNCTION (BASIC)
void swap(int *a, int *b)


👉 Uses pointers to exchange values

🧠 Picture:

a = 10     b = 20
↓ swap ↓
a = 20     b = 10

⬆️ upheapify() (MOST IMPORTANT)

Used ONLY DURING INSERTION

WHY NEEDED?

When you insert a new value:

It goes at the last position

Heap property may break

So we move it UP

int parent = (index - 1) / 2;


🧠 Picture:

Insert 40

        30
       /  \
     20    15
    /
  10


Insert at last → compare with parent → swap → repeat

➕ insert() FUNCTION (CORE)
heap[*size] = value;
upheapify(heap, *size);
(*size)++;

Step-by-step:

Insert value at end of array

Call upheapify

Increase size

🧠 Like putting a student in last bench → then pushing him forward if he’s taller 😄

⬇️ downheapify() (USED IN DELETE / SORT)

Used when:

Root is removed

Heap sort

Build heap

Picture:
        10   ❌
       /  \
     40    30


Root is wrong → push it down

🖨️ printHeap()

Just prints array → which is level order traversal

🚀 MAIN FUNCTION FLOW
insert(heap, &size, 10);
insert(heap, &size, 20);
insert(heap, &size, 15);
insert(heap, &size, 30);
insert(heap, &size, 40);

Step-by-step heap building:

1️⃣ Insert 10 → [10]
2️⃣ Insert 20 → [20,10]
3️⃣ Insert 15 → [20,10,15]
4️⃣ Insert 30 → [30,20,15,10]
5️⃣ Insert 40 → [40,30,20,10,15]

📌 FINAL OUTPUT
Max Heap: 40 30 20 10 15
*/