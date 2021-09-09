from collections import deque


class Stack:
    def __init__(self, *data):
        self.data = deque(data)

    def push(self, element) -> None:
        self.data.append(element)

    def pop(self):
        popped_el = self.data.pop()
        return popped_el

    def top(self):
        # wrong
        return self.data[-1]

    def is_empty(self):
        if len(self.data) > 0:
            return False
        return True

    def __str__(self):
        return str(self.data)


stack = Stack(1, 2, 3, 4, 5)
print(stack.pop())
print(stack.push(6))
print(stack.top())
print(stack.is_empty())