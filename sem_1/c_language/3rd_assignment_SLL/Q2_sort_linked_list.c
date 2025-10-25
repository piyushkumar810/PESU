/*
Write a C Program to do the following 

Construct a Basic Node: Define a structure in C that represents a single node in a linked list containing an integer data and a pointer to the next node.
■ Hint: Use struct in C to define your node. The node typically contains data of type int and a pointer to the next struct.
Initialization Function: Write a function that initializes a linked list and returns a pointer to the head node.
■ Hint: This function should return a NULL pointer to signify that the list is empty at the beginning.
Insert in Order: Assuming the linked list stores integers, write a function that inserts a new node in such a way that the linked list remains sorted in increasing order.
■ Hint: Traverse the list to find the appropriate position where the new node’s value fits, then insert the node at this position.
Sort Linked List Using New Header: Implement a function that sorts a linked list of integers by creating a new header node and transferring nodes from the original list to the new list in sorted order.
■ Hint: Traverse the original list, remove the first node, and insert it into the new list at the correct position. Continue this process until the original list is empty.

typedef struct mynode {
      int data; 
      structure dynode *link;
} *NODE;

*/
