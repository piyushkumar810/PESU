// #define QUEUE_MAX_SIZE 100

// typedef struct {
//     int items[QUEUE_MAX_SIZE];
//     int front, rear;
// } Queue;

// // Function to initialize the queue
// void initializeQueue(Queue *q) {
//     q->front = -1;
//     q->rear = -1;
// }

// // Check if the queue is empty
// int isEmpty(Queue *q) {
//     return q->rear == -1;
// }

// // Check if the queue is full
// int isFull(Queue *q) {
//     return q->rear == QUEUE_MAX_SIZE - 1;
// }

// // Add an element to the queue
// void enqueue(Queue *q, int value) {
//     if (isFull(q)) {
//         printf("Queue is full. Cannot insert %d\n", value);
//     } else {
//         if (q->front == -1) { // First element
//             q->front = 0;
//         }
//         q->rear++;
//         q->items[q->rear] = value;
//     }
// }

// // Remove and return the front element
// int dequeue(Queue *q) {
//     if (isEmpty(q)) {
//         printf("Queue is empty. Cannot dequeue\n");
//         return -1;
//     } else {
//         int item = q->items[q->front];
//         q->front++;
//         if (q->front > q->rear) { // Queue becomes empty
//             initializeQueue(q);
//         }
//         return item;
//     }
// }

// // Get the front element without removing it
// int peek(Queue *q) {
//     if (isEmpty(q)) {
//         printf("Queue is empty. No front element\n");
//         return -1;
//     } else {
//         return q->items[q->front];
//     }
// }

// // Display the queue elements
// void displayQueue(Queue *q) {
//     if (isEmpty(q)) {
//         printf("Queue is empty\n");
//     } else {
//         printf("Queue elements are:\n");
//         for (int i = q->front; i <= q->rear; i++)
//             printf("%d ", q->items[i]);
//         printf("\n");
//     }
// }

// // Demonstration
// int main() {
//     Queue q;
//     initializeQueue(&q);

//     enqueue(&q, 10);
//     enqueue(&q, 20);
//     enqueue(&q, 30);

//     displayQueue(&q);

//     int item = dequeue(&q);
//     printf("Dequeued item: %d\n", item);

//     displayQueue(&q);

//     return 0;
// }



#include <stdio.h>
#define MAX 5

typedef struct {
    int items[MAX];
    int front, rear;
} Queue;

// Initialize the queue
void initializeQueue(Queue *q) {
    q->front = -1;
    q->rear = -1;
}

// Check if the queue is full
int isFull(Queue *q) {
    return (q->front == (q->rear + 1) % MAX);
}

// Check if the queue is empty
int isEmpty(Queue *q) {
    return (q->front == -1);
}

// Add an element to the queue
void enqueue(Queue *q, int value) {
    if (isFull(q)) {
        printf("Queue is full. Cannot insert %d\n", value);
        return;
    }
    if (isEmpty(q)) {
        q->front = 0;
        q->rear = 0;
    } else {
        q->rear = (q->rear + 1) % MAX;
    }
    q->items[q->rear] = value;
    printf("Enqueued %d\n", value);
}

// Remove and return the front element
int dequeue(Queue *q) {
    if (isEmpty(q)) {
        printf("Queue is empty. Cannot dequeue\n");
        return -1;
    }
    int item = q->items[q->front];
    if (q->front == q->rear) {
        // Queue has only one element, reset
        q->front = -1;
        q->rear = -1;
    } else {
        q->front = (q->front + 1) % MAX;
    }
    return item;
}

// Display the queue
void displayQueue(Queue *q) {
    if (isEmpty(q)) {
        printf("Queue is empty\n");
        return;
    }
    printf("Queue elements: ");
    int i = q->front;
    while (1) {
        printf("%d ", q->items[i]);
        if (i == q->rear) break;
        i = (i + 1) % MAX;
    }
    printf("\n");
}

// Demonstration
int main() {
    Queue q;
    initializeQueue(&q);

    enqueue(&q, 10);
    enqueue(&q, 20);
    enqueue(&q, 30);
    enqueue(&q, 40);
    enqueue(&q, 50); // This will show "Queue is full"

    displayQueue(&q);

    printf("Dequeued: %d\n", dequeue(&q));
    displayQueue(&q);

    enqueue(&q, 60); // Wraps around
    displayQueue(&q);

    return 0;
}