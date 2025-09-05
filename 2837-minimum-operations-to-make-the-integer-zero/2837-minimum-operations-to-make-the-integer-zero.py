class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        for k in range(1, 61):  # check up to 60 steps
            target = num1 - k * num2
            if target < k:  # cannot represent
                continue
            if target >= 0 and target.bit_count() <= k:
                return k
        return -1
