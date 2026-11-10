
"""
LeetCode 21: Merge Two Sorted Lists

Question:
You are given the heads of two sorted linked lists,
list1 and list2.

Merge both lists into one sorted linked list.
The merged list should be created by connecting
the existing nodes.

Return the head of the merged linked list.

Example:
Input:
list1 = 1 -> 2 -> 4
list2 = 1 -> 3 -> 4

Output:
1 -> 1 -> 2 -> 3 -> 4 -> 4

Approach:
1. Create a dummy node.
2. Use current to build the merged list.
3. Compare the values of list1 and list2.
4. Attach the smaller node to current.next.
5. Move the pointer of the selected list.
6. Attach the remaining nodes.

Time Complexity: O(n + m)
Space Complexity: O(1)
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1, list2):

        dummy = ListNode(-1)
        current = dummy

        while list1 and list2:

            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next

            else:
                current.next = list2
                list2 = list2.next

            current = current.next

        if list1:
            current.next = list1

        if list2:
            current.next = list2

        return dummy.next


# Create first linked list: 1 -> 2 -> 4
list1 = ListNode(1, ListNode(2, ListNode(4)))

# Create second linked list: 1 -> 3 -> 4
list2 = ListNode(1, ListNode(3, ListNode(4)))

# Create Solution object
solution = Solution()

# Merge both linked lists
result = solution.mergeTwoLists(list1, list2)

# Print the merged linked list
while result:
    print(result.val, end=" -> ")
    result = result.next

print("None")
