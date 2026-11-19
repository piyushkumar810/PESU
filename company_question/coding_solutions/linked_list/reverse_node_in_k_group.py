
"""
LeetCode 25: Reverse Nodes in k-Group

Question:
Given the head of a linked list, reverse the nodes
of the list k at a time and return the modified list.

If the remaining nodes are fewer than k,
leave them unchanged.

Example:
Input:
head = 1 -> 2 -> 3 -> 4 -> 5
k = 2

and 


Output:
2 -> 1 -> 4 -> 3 -> 5

Approach:
1. Create a dummy node.
2. Find the kth node of each group.
3. If fewer than k nodes remain, stop.
4. Reverse the group using three pointers.
5. Connect the reversed group.
6. Continue with the next group.

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import Optional


# Definition of Linked List Node
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        dummy = ListNode(0)
        dummy.next = head

        group_prev = dummy

        while True:

            # Find the kth node
            kth = group_prev

            for i in range(k):
                if kth.next is None:
                    return dummy.next

                kth = kth.next

            # Save the node after the group
            group_next = kth.next

            # Reverse the current group
            prev = group_next
            current = group_prev.next

            assert current is not None

            while current is not group_next:

                assert current is not None

                next_node = current.next

                current.next = prev

                prev = current
                current = next_node

            # Save the original first node of the group
            old_group_start = group_prev.next
            assert old_group_start is not None

            # Connect the reversed group
            group_prev.next = kth

            # Move to the next group
            group_prev = old_group_start


# Function to print linked list
def printList(head):
    current = head

    while current:
        print(current.val, end=" -> ")
        current = current.next

    print("None")


# Create linked list
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

k = 2

print("Original Linked List:")
printList(head)

solution = Solution()

result = solution.reverseKGroup(head, k)

print("\nReversed Linked List:")
printList(result)
