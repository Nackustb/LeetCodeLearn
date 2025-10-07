class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [0] * k
        self.k = k
        self.front = 0
        self.rear = 0
        self.size = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.queue[self.rear] = value
        self.size += 1
        self.rear = (self.rear +1) %self.k
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.front = (self.front+1) %self.k
        self.size -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty:
            return -1
        return self.queue[self.front]

    def Rear(self) -> int:
        if self.isEmpty:
            return -1
        return self.queue[self.rear - 1 ]        


    def isEmpty(self) -> bool:
        return self.size == 0


    def isFull(self) -> bool:
        return self.size == self.k



if __name__ == "__main__":
    queue = MyCircularQueue(3)
    print(queue.enQueue(1))  # True
    print(queue.enQueue(2))  # True
    print(queue.enQueue(3))  # True
    print(queue.enQueue(4))  # False, queue is full
    print(queue.Rear())       # 3
    print(queue.isFull())     # True
    print(queue.deQueue())    # True
    print(queue.enQueue(4))   # True
    print(queue.Rear())       # 4
    print(queue.Front())      # 2