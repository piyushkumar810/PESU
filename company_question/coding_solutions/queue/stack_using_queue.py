from collections import deque

class MyStack:

    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)

        # Move all previous elements behind x
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self) -> int:
        return self.q.popleft()

    def top(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return len(self.q) == 0

my = MyStack()

my.push(10)
my.push(20)
my.push(30)

print(my.top())      # 30

print(my.pop())      # 30
print(my.pop())      # 20

print(my.empty())    # False

print(my.pop())      # 10

print(my.empty())    # True