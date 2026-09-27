class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def print_list(head):
    current = head

    while current != None:
        print(current.data, end="->")
        current = current.next

    print("None")


def insert_at_begning(head, data):
    new_node = Node(data)

    new_node.next = head
    return new_node

def insert_end(head, data):
    new_node = Node(data)

    if head is None:
        return new_node

    current = head

    while current.next:
        current = current.next

    current.next = new_node
    return head


    


list1 = Node(10)
list1.next = Node(20)
list1.next.next = Node(30)
list1.next.next.next = Node(40)

print_list(list1)

# insert at beginning
list1 = insert_at_begning(list1, 5)

print_list(list1)