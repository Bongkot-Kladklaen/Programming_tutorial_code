class CircularQueue:
    class _Node:
        __slots__ = '_element','_next'
        def __init__(self,e,next_):
            self._element = e
            self._next = next_
    def __init__(self):
        self._head = None
        self._size = 0
    def __len__(self):
        return self._size
    def is_empty(self):
        return self._size == 0
    def first(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        head = self._tail._next
        return head._element
    def dequeue(self):
        if self.is_empty():
            raise Empty("Queue is empty")
        oldhead = self._tail._next
        self._size -= 1
        if self._size == 0:
            self._tail = None
        else:
            self._tail._next = oldhead._next
        return oldhead._element
    def enqueue(self, e):
        newest = self._Node(e, None)
        if self.is_empty():
            newest._next = newest
        else:
            newest._next = self._tail._next
            self._tail._next = newest
        self._tail = newest
        self._size += 1
    def rotate(self):
        if self._size > 0:
            self._tail = self._tail._next
    def __str__(self):
        expr = []
        if self.is_empty():
            return "[]"
        current = self._tail._next
        expr.append(current._element)
        while current._next != self._tail._next:
            current = current._next
            expr.append(current._element)
        return str(expr)

q = CircularQueue()
print(q)

q.enqueue("LAX")
q.enqueue("MPS")
print(q)

q.dequeue()
print(q)

q.enqueue("ATL")
print('First: ',q.first())

q.enqueue("BOS")
print(q)

q.rotate()
