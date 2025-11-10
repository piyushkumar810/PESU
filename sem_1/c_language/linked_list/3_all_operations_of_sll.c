// ------------- lets do it sll all operation
// 1. create node
// 2.display
// 3. insert front
// 4. insert end
// 5. insert_position
// 6. delete last
// 7. delete position
// 8. delete value
// 9. count node
// 10. search value
// ----------- advance-----------
// 11. reverse the linked list
// 12. sort the linked list
// 13. merge two linked list
// 14. detect loop in the linked list
// 15. middle element using slow fast pointer

#include<stdio.h>
#include<stdlib.h>

typedef struct node{
    int data;
    struct node *next;
}*NODE;

void cretae_node(int data){
    NODE temp=(NODE)malloc(sizeof(struct node));

}