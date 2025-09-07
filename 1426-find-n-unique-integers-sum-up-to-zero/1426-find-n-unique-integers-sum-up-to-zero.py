class Solution:
    def sumZero(self, n: int) -> list[int]:
        res = []
        # add pairs (i, -i)
        for i in range(1, n // 2 + 1):
            res.extend([i, -i])
        # if n is odd, add 0
        if n % 2 == 1:
            res.append(0)
        return res
