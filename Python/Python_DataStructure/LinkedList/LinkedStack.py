class LinkedStack:
    class _Node:
        __slots__ = '_element','_next'
        def __init__(self,element, next_):
            self._element = element
            self._next = next_
    def __init__(self):
        self._head = None
        self._size = 0
    def __len__(self):
        return self._size
    def is_empty(self):
        return self._size == 0
    def top(self):
        if self.is_empty():
            raise Empty('stack is empty')
        return self._head._element
    def push(self, e):
        self._head = self._Node(e, self._head)
        self._size += 1
    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        return answer
    def __str__(self):
        expr = []
        if self.is_empty():
            return "[]"
        current = self._head
        expr.append(current._element)
        while current._next != None:
            current = current._next
            expr.append(current._element)
        return str(expr)

s = LinkedStack()
print(s)

s.push("BOS")
s.push("ATL")
print(s)

s.push("MPS")
s.push("LAX")
print(s)

s.pop()
s.pop()
print(s)