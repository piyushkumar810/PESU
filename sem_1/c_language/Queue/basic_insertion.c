// queue implementation usins arrayy implementation

#include<stdio.h>
#define MAX 5

int queue[MAX];
int front=-1;
int rear=-1;

/*
Steps inside enqueue():

Check if rear reached MAX-1 (means queue full)
If inserting the first element → front becomes 0
Increase rear → rear++
Store the value inside queue[rear]
 */
void enqueue(int value){
    if(rear==MAX-1){
        printf("Queue is full\n");
    }else{
        if(front==-1){
            front=0;
        }
        rear++;
        queue[rear]=value;
        printf("%d inserted\n", value);
    }
}

void dequeue(){
    if(front==-1 || front > rear){
        printf("Queue is empty\n");
    }else{
        printf("%d removed \n", queue[front]);
        front++;

        if(front>rear){
            front=rear-1;
        }
    }
}
