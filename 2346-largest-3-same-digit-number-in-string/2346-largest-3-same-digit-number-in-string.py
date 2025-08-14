class Solution:
    def largestGoodInteger(self, num: str) -> str:
        best = ""
        for i in range(len(num) - 2):
            if num[i] == num[i+1] == num[i+2]:
                triple = num[i] * 3
                if best == "" or triple > best:
                    best = triple
        return best
