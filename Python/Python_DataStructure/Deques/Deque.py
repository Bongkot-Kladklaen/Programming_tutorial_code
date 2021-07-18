class Deque(object):
    def __init__(self, limit = 10):
        self.queue = []
        self.limit = limit
    def __str__(self):
        return ' '.join([str(i) for i in self.queue])
    def isEmpty(self):
        return len(self.queue) <= 0
    def isFull(self):
        return len(self.queue) >= self.limit

    def insertRear(self, data):
        if self.isFull():
            return
        else:
            self.queue.insert(0, data)
    def insertFront(self, data):
        if self.isFull():
            return
        else:
            self.queue.append(data)
    def deleteRear(self):
        if self.isEmpty():
            return
        else:
            self.queue.pop(0)
    def deleteFront(self):
        if self.isFull():
            return
        else:
            self.queue.pop()

if __name__ == "__main__":
    myDeque = Deque()
    myDeque.insertFront(6)
    myDeque.insertRear(9)
    myDeque.insertFront(3)
    myDeque.insertRear(12)
    print(myDeque)
    myDeque.deleteRear()
    print(myDeque)
    myDeque.deleteFront()
    print(myDeque)

