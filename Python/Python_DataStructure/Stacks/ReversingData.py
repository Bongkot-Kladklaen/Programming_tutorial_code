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
            raise Empty('stack is empty')
        return self._data.pop()

def reverse_file(filename):
    s = ArrayStack()
    original = open(filename)
    for line in original:
        s.push(line.rstrip('\n'))
    original.close()

    output = open(filename, 'w')
    while not s.is_empty():
        output.write(s.pop() + '\n')
    output.close()

output = reverse_file('data.txt')