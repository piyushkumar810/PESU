
"""
LeetCode 141: Linked List Cycle

Question:
Given the head of a singly linked list, determine
if the linked list has a cycle.

A cycle exists if some node can be reached again
by continuously following the next pointer.

Return True if a cycle exists.
Otherwise, return False.

Approach: Floyd's Cycle Detection Algorithm

1. Initialize slow and fast pointers at head.
2. Move slow by one step.
3. Move fast by two steps.
4. If both pointers meet, a cycle exists.
5. If fast reaches None, no cycle exists.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def hasCycle(self, head):

        # Initialize both pointers at the head
        slow = head
        fast = head

        # Continue while fast and fast.next are not None
        while fast and fast.next:

            # Slow moves one step
            slow = slow.next

            # Fast moves two steps
            fast = fast.next.next

            # If both pointers meet, a cycle exists
            if slow == fast:
                return True

        # Fast reached the end, so no cycle exists
        return False
