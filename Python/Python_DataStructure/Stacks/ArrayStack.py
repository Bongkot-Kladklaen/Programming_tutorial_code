class ArrayStack:
    def __init__(self):
        self._data = []
    def __len__(self):
        return len(self._data)
    def is_empty(self):
        return len(self._data) == 0
    def push(self,e):
        self._data.append(e)
    def top(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]
    def pop(self):
        if self.is_empty():
            raise Empty('stack is empy')
        return self._data.pop()

s = ArrayStack()
s.push(5)
s.push(3)
print(len(s))
print(s.pop())
print(s.is_empty())
print(s.pop())
print(s.is_empty())
s.push(7)
s.push(9)
print(s.top())
s.push(4)
print(len(s))
print(s.pop())
s.push(6)
print(s._data)
