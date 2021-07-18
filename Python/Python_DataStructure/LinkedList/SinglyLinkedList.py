class SinglyLinkedList:
    class _Node:
        __slots__ = '_element','_next'
        def __init__(self,element, next_):
            self._element = element
            self._next = next_
    
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0
    def __len__(self):
        return self._size
    def is_empty(self):
        return self._size == 0
    def add_first(self, e):
        newest = self._Node(e, self._head)
        if self.is_empty():
            self._tail = newest
        self._head = newest
        self._size += 1
    def add_last(self, e):
        newest = self._Node(e, None)
        if self.is_empty():
            self._head = newest
        else:
            self._tail._next = newest
        self._tail = newest
        self._size += 1
    def remove_first(self):
        if self.is_empty():
            raise Empty('Linked list is empty')
        self._head = self._head._next
        self._size -= 1
    def remove_last(self):
        if self.is_empty():
            raise Empty('Linked list is empty')
        new_last = self._traverse(self._size-1)
        self._tail = new_last
        self._tail._next = None
    def _traverse(self, n):
        current = self._head
        for _ in range(1,n):
            current = current._next
        return current
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

s = SinglyLinkedList()
print(s)

s.add_first("MSP")
print(s)
s.add_last("ATL")
print(s)
s.add_first("LAX")
print(s)
s.add_last("BOS")
print(s)
s.remove_first()
s.remove_last()
print(s)