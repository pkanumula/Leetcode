class MyCircularDeque:

    def __init__(self, k):
        self.deque = [0] * k  # Initialize a fixed-size array
        self.k = k  # Maximum size of the deque
        self.front = 0  # Pointer to the front element
        self.rear = 0  # Pointer to the rear element
        self.size = 0  # Current size of the deque

    def insertFront(self, value):
        if self.isFull():
            return False
        self.front = (self.front - 1) % self.k  # Move front pointer back
        self.deque[self.front] = value
        self.size += 1
        return True

    def insertLast(self, value):
        if self.isFull():
            return False
        self.deque[self.rear] = value
        self.rear = (self.rear + 1) % self.k  # Move rear pointer forward
        self.size += 1
        return True

    def deleteFront(self):
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.k  # Move front pointer forward
        self.size -= 1
        return True

    def deleteLast(self):
        if self.isEmpty():
            return False
        self.rear = (self.rear - 1) % self.k  # Move rear pointer back
        self.size -= 1
        return True

    def getFront(self):
        if self.isEmpty():
            return -1
        return self.deque[self.front]

    def getRear(self):
        if self.isEmpty():
            return -1
        return self.deque[(self.rear - 1) % self.k]  # Rear points to the next empty slot, so get the last element

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.k
