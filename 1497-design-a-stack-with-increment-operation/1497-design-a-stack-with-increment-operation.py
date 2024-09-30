class CustomStack(object):

    def __init__(self, maxSize):
        self.stack = []
        self.maxSize = maxSize
        self.incrementArr = [0] * maxSize  # Auxiliary array to store increments

    def push(self, x):
        if len(self.stack) < self.maxSize:
            self.stack.append(x)

    def pop(self):
        if not self.stack:
            return -1
        idx = len(self.stack) - 1
        increment_value = self.incrementArr[idx]
        if idx > 0:
            # Pass the increment down to the next element
            self.incrementArr[idx - 1] += self.incrementArr[idx]
        self.incrementArr[idx] = 0  # Reset the increment at this index
        return self.stack.pop() + increment_value

    def increment(self, k, val):
        limit = min(k, len(self.stack))
        if limit > 0:
            # Only increment the element at limit - 1
            self.incrementArr[limit - 1] += val
