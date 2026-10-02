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

'''
3. Example

Suppose we do:

push(1)
push(2)
push(3)

Initially:

stack1 = []
stack2 = []
push(1)
stack1 = [1]
stack2 = []
push(2)
stack1 = [1, 2]
stack2 = []
push(3)
stack1 = [1, 2, 3]
stack2 = []

Now we want:

pop() → 1

But stack1 gives us:

3

That's the opposite of what a queue wants.
'''