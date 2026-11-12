
"""
LeetCode 138: Copy List with Random Pointer

Question:
Given a linked list where each node contains:
1. val
2. next pointer
3. random pointer

Create a deep copy of the linked list.

Approach: HashMap

1. Create a new node for every original node.
2. Store original -> copied node in a dictionary.
3. Connect the next and random pointers of copied nodes.
4. Return the head of the copied list.

Time Complexity: O(n)
Space Complexity: O(n)
"""

# Node definition
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = x
        self.next = next
        self.random = random


# Function to copy the linked list
def copyRandomList(head):

    if head is None:
        return None

    old_to_new = {}

    current = head

    # First pass: Create copies of all nodes
    while current:
        old_to_new[current] = Node(current.val)
        current = current.next

    current = head

    # Second pass: Connect next and random pointers
    while current:
        copy = old_to_new[current]

        copy.next = old_to_new.get(current.next)
        copy.random = old_to_new.get(current.random)

        current = current.next

    return old_to_new[head]


# Function to print the linked list
def printList(head):
    current = head

    while current:
        random_value = current.random.val if current.random else None

        print("Value:", current.val, "| Random:", random_value)

        current = current.next


# Create original linked list
node1 = Node(7)
node2 = Node(13)
node3 = Node(11)
node4 = Node(10)
node5 = Node(1)

# Connect next pointers
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

# Connect random pointers
node1.random = None
node2.random = node1
node3.random = node5
node4.random = node3
node5.random = node1

# Original linked list
head = node1

print("Original Linked List:")
printList(head)

# Create deep copy
copied_head = copyRandomList(head)

print("\nCopied Linked List:")
printList(copied_head)
