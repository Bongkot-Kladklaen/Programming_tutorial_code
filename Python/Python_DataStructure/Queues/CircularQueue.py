class CircularQueue(object):
    def __init__(self,limit = 10):
        self.front = None
        self.rear = None
        self.limit = limit
        self.queue = []
    def __str__(self):
        return ' '.join([str(i) for i in self.queue])
    def isEmpty(self):
        return self.queue == []
    def isFull(self):
        return len(self.queue) == self.limit
    def enqueue(self,data):
        if self.isFull():
            print('Queue is Full')
        elif self.isEmpty():
            self.front = self.rear = 0
            self.queue.append(data)
        else:
            self.rear += 1
            self.queue.append(data)
    def dequeue(self):
        if self.isEmpty():
            print('Queue is Empty!')
        else:
            self.front += 1
            return self.queue.pop(0)

if __name__ == "__main__":
    myCQ = CircularQueue(5)
    myCQ.enqueue(29)
    myCQ.enqueue(23)
    myCQ.enqueue(17)
    myCQ.enqueue(18)
    print('Queue:',myCQ)
    myCQ.dequeue()
    myCQ.dequeue()
    print('Queue:',myCQ)
    myCQ.enqueue(9)
    myCQ.enqueue(20)
    myCQ.enqueue(6)
    myCQ.enqueue(6)
    print('Queue:',myCQ)
