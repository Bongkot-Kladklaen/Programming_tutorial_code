class LinkedQueue:
    class _Node:
        __slots__ = '_element','_next'
        def __init__(self,e,next_):
            self._element = e
            self._next = next_
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0
    def __len__(self):
        return self._size
    def is_empty(self):
        return self._size == 0
    def first(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._head._element
    def enqueue(self, e):
        newest = self._Node(e, None)
        if self.is_empty():
            self._head = newest
        else:
            self._tail._next = newest
        self._tail = newest
        self._size += 1
    def dequeue(self):
        if self.is_empty():
            raise Empty("Queue is empty")
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None
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

s = LinkedQueue()
print(s)

s.enqueue("LAX")
s.enqueue("MPS")
print(s)

s.dequeue()
print(s)
print('First: ', s.first())

s.enqueue("ATL")
print(s)