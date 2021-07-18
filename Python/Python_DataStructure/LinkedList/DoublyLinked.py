class DoublyLinkedBase:
    class _Node:
        __slots__ = '_element','_prev','_next'
        def __init__(self,element,prev,next_):
            self._element = element
            self._prev = prev
            self._next = next_
    def __init__(self):
        self._header = self._Node(None,None,None)
        self._trailer = self._Node(None,self._header,None)
        self._header._next = self._trailer
        self._size = 0
    def __len__(self):
        return self._size
    def is_empty(self):
        return self._size == 0
    def _insert_between(self, e, predecessor, successor):
        newest = self._Node(e,predecessor,successor)
        predecessor._next=newest
        successor._prev=newest
        self._size += 1
        return newest
    def _delete_node(self,node):
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        element = node._element
        node._prev = node._next = node._element = None
        return element
    def __str__(self):
        if self.is_empty():
            return "[]"
        expr = []
        current = self._header
        expr.append(current._element)
        while current._next != self._trailer:
            current = current._next
            expr.append(current._element)
        return str(expr)

s = DoublyLinkedBase()
print(s)

s._insert_between(0,s._header,s._trailer)
print(s)
s._insert_between(1,s._header._next,s._trailer)
print(s)
s._delete_node(s._header._next)
print(s)