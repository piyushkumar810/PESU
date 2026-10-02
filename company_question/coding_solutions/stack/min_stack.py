
'''
2. Min Stack ⭐⭐⭐⭐⭐
Problem

Design a stack that supports:

push()
pop()
top()
getMin()

And getMin() should return the minimum element efficiently.

Example:

push(5)
push(3)
push(7)
push(2)

getMin() → 2
Simple idea

Maintain two stacks:

stack     → normal values
min_stack → minimum values
'''


class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


# Example
stack = MinStack()

stack.push(-2)
stack.push(0)
stack.push(-3)

print("Minimum:", stack.getMin())

stack.pop()

print("Top:", stack.top())
print("Minimum:", stack.getMin())