# ==========================================
# SINGLY LINKED LIST - IMPORTANT OPERATIONS
# ==========================================


# 1. Create Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# 2. Print / Traverse Linked List
def print_list(head):
    current = head

    while current:
        print(current.data, end=" -> ")
        current = current.next

    print("None")


# 3. Insert at Beginning
def insert_beginning(head, data):
    new_node = Node(data)

    new_node.next = head
    return new_node


# 4. Insert at End
def insert_end(head, data):
    new_node = Node(data)

    if head is None:
        return new_node

    current = head

    while current.next:
        current = current.next

    current.next = new_node

    return head


# 5. Delete a Node
def delete_node(head, key):

    if head is None:
        return None

    # Delete head
    if head.data == key:
        return head.next

    current = head

    while current.next:

        if current.next.data == key:
            current.next = current.next.next
            break

        current = current.next

    return head


# 6. Search an Element
def search(head, key):
    current = head

    while current:

        if current.data == key:
            return True

        current = current.next

    return False


# 7. Find Length
def length(head):
    count = 0
    current = head

    while current:
        count += 1
        current = current.next

    return count


# 8. Reverse Linked List
def reverse(head):
    prev = None
    current = head

    while current:

        next_node = current.next
        current.next = prev

        prev = current
        current = next_node

    return prev


# 9. Find Middle Node
def find_middle(head):
    slow = head
    fast = head

    while fast and fast.next:

        slow = slow.next
        fast = fast.next.next

    return slow


# 10. Detect Cycle
def has_cycle(head):
    slow = head
    fast = head

    while fast and fast.next:

        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False


# 11. Find Nth Node from End
def nth_from_end(head, n):

    slow = head
    fast = head

    # Move fast n steps
    for _ in range(n):

        if fast is None:
            return None

        fast = fast.next

    # Move both
    while fast:
        slow = slow.next
        fast = fast.next

    return slow


# 12. Remove Duplicates
def remove_duplicates(head):

    seen = set()
    current = head
    previous = None

    while current:

        if current.data in seen:
            previous.next = current.next

        else:
            seen.add(current.data)
            previous = current

        current = current.next

    return head


# 13. Merge Two Sorted Linked Lists
def merge_sorted_lists(l1, l2):

    dummy = Node(0)
    current = dummy

    while l1 and l2:

        if l1.data <= l2.data:
            current.next = l1
            l1 = l1.next

        else:
            current.next = l2
            l2 = l2.next

        current = current.next

    if l1:
        current.next = l1

    else:
        current.next = l2

    return dummy.next


# ==========================================
# MAIN PROGRAM
# ==========================================

# Create Linked List
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
head.next.next.next.next = Node(50)


# ------------------------------------------
# 1. Print Linked List
# ------------------------------------------

print("Original Linked List:")
print_list(head)


# ------------------------------------------
# 2. Insert at Beginning
# ------------------------------------------

head = insert_beginning(head, 5)

print("\nAfter inserting 5 at beginning:")
print_list(head)


# ------------------------------------------
# 3. Insert at End
# ------------------------------------------

head = insert_end(head, 60)

print("\nAfter inserting 60 at end:")
print_list(head)


# ------------------------------------------
# 4. Search
# ------------------------------------------

print("\nSearching for 30:")

if search(head, 30):
    print("30 Found")
else:
    print("30 Not Found")


# ------------------------------------------
# 5. Length
# ------------------------------------------

print("\nLength of Linked List:")
print(length(head))


# ------------------------------------------
# 6. Delete Node
# ------------------------------------------

head = delete_node(head, 30)

print("\nAfter deleting 30:")
print_list(head)


# ------------------------------------------
# 7. Find Middle
# ------------------------------------------

middle = find_middle(head)

print("\nMiddle Node:")
print(middle.data)


# ------------------------------------------
# 8. Nth Node from End
# ------------------------------------------

n = 2

node = nth_from_end(head, n)

print(f"\n{n}nd Node from End:")

if node:
    print(node.data)
else:
    print("Node does not exist")


# ------------------------------------------
# 9. Reverse Linked List
# ------------------------------------------

head = reverse(head)

print("\nAfter Reversing:")
print_list(head)


# ------------------------------------------
# 10. Detect Cycle
# ------------------------------------------

print("\nDoes Linked List contain Cycle?")

if has_cycle(head):
    print("Yes")
else:
    print("No")


# ------------------------------------------
# 11. Remove Duplicates
# ------------------------------------------

head.next.next.next.data = head.next.data

print("\nBefore Removing Duplicates:")
print_list(head)

head = remove_duplicates(head)

print("After Removing Duplicates:")
print_list(head)


# ==========================================
# 12. Merge Two Sorted Linked Lists
# ==========================================

list1 = Node(1)
list1.next = Node(3)
list1.next.next = Node(5)

list2 = Node(2)
list2.next = Node(4)
list2.next.next = Node(6)

merged = merge_sorted_lists(list1, list2)

print("\nMerged Sorted Linked Lists:")
print_list(merged)