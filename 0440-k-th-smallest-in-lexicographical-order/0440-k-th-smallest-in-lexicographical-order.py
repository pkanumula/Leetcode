class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def countSteps(prefix, n):
            steps = 0
            first = prefix
            last = prefix
            while first <= n:
                steps += min(last, n) - first + 1
                first *= 10
                last = last * 10 + 9
            return steps

        curr = 1
        k -= 1  # we start from 1, so skip the first number
        
        while k > 0:
            steps = countSteps(curr, n)
            if steps <= k:
                k -= steps
                curr += 1  # move to next sibling
            else:
                k -= 1
                curr *= 10  # move to first child

        return curr
