// linear queue using static array

#include<stdio.h>
#define MAX 10

// Structure
typedef struct QueueADT {
    int arr[MAX];
    int front, rear;
} Queue;


// Initialize
void init(Queue *q) {
    q->front = 0;
    q->rear = -1;
}


// Check Empty
int isEmpty(Queue *q) {
    return (q->rear < q->front);
}


// Check Full
int isFull(Queue *q) {
    return (q->rear == MAX - 1);
}


// Enqueue
void enqueue(Queue *q, int x) {
    if(isFull(q))
        printf("\nOverflow");
    else {
        q->arr[++q->rear] = x;
    }
}


// Dequeue
int dequeue(Queue *q) {
    if (isEmpty(q)) {
        printf("\nUnderflow");
        return -1;
    }
    return q->arr[q->front++];
}


// Display
void display(Queue *q) {
    if (isEmpty(q))
        printf("\nEmpty Queue");
    else {
        printf("\nQueue: ");
        for (int i = q->front; i <= q->rear; i++)
            printf("%d ", q->arr[i]);
    }
}


// ⭐ Simple main() (No menu)
int main() {
    Queue q;
    init(&q);

    enqueue(&q, 10);
    enqueue(&q, 20);
    enqueue(&q, 30);

    display(&q);

    printf("\nDequeued: %d", dequeue(&q));

    display(&q);

    return 0;
}