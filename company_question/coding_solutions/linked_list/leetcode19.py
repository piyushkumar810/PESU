
"""
LeetCode 19: Remove Nth Node From End of List

Question:
Given the head of a linked list, remove the nth node
from the end of the list and return its head.

Example:
Input:
head = 1 -> 2 -> 3 -> 4 -> 5
n = 2

Output:
1 -> 2 -> 3 -> 5

Approach: Two Pointers

1. Create a dummy node.
2. Initialize slow and fast at dummy.
3. Move fast ahead by n + 1 steps.
4. Move both pointers until fast becomes None.
5. Delete the node after slow.

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import Optional


# Linked List Node
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next: Optional["ListNode"] = next


class Solution:
    def removeNthFromEnd(
        self, head: Optional[ListNode], n: int
    ) -> Optional[ListNode]:

        # Create dummy node
        dummy = ListNode(0)
        dummy.next = head

        # Initialize two pointers
        slow = dummy
        fast = dummy

        # Move fast ahead by n + 1 steps
        for i in range(n + 1):
            assert fast is not None
            fast = fast.next

        # Move both pointers together
        while fast is not None:
            assert slow.next is not None
            slow = slow.next
            fast = fast.next

        # Delete the required node
        assert slow.next is not None
        slow.next = slow.next.next

        return dummy.next


# Function to print linked list
def printList(head: Optional[ListNode]):
    current = head

    while current is not None:
        print(current.val, end=" -> ")
        current = current.next

    print("None")


# Create linked list
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

# Position from the end
n = 2

print("Original Linked List:")
printList(head)

solution = Solution()
result = solution.removeNthFromEnd(head, n)

print("\nUpdated Linked List:")
printList(result)
