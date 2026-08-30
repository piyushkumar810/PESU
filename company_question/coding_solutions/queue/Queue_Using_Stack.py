class QueueUsingStacks:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def enqueue(self, x):
        self.in_stack.append(x)

    def dequeue(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())

        if not self.out_stack:
            return -1

        return self.out_stack.pop()

    def peek(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())

        if not self.out_stack:
            return -1

        return self.out_stack[-1]

    def is_empty(self):
        return not self.in_stack and not self.out_stack

q = QueueUsingStacks()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print(q.dequeue())  # 10
print(q.dequeue())  # 20

q.enqueue(40)

print(q.peek())     # 30
print(q.dequeue())  # 30
print(q.dequeue())  # 40
print(q.dequeue())  # -1