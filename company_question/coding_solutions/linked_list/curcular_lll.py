
"""
LeetCode 92: Reverse Linked List II

Question:
Given the head of a singly linked list and two positions
left and right, reverse the nodes from position left to right.

Example:
Input:
head = 1 -> 2 -> 3 -> 4 -> 5
left = 2
right = 4

Output:
1 -> 4 -> 3 -> 2 -> 5

Approach:
1. Create a dummy node.
2. Move prev to the node before left.
3. Set current to the first node of the section.
4. Move the next node after current to the beginning.
5. Repeat right - left times.

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        dummy = ListNode(0)
        dummy.next = head

        prev = dummy

        for i in range(left - 1):
            assert prev.next is not None
            prev = prev.next

        current = prev.next
        assert current is not None

        for i in range(right - left):

            next_node = current.next
            assert next_node is not None

            current.next = next_node.next

            next_node.next = prev.next

            prev.next = next_node

        return dummy.next


def printList(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")


# Create linked list
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

solution = Solution()

result = solution.reverseBetween(head, 2, 4)

printList(result)
