
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
