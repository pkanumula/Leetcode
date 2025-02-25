class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        mod = 10**9 + 7
        even, odd = 1, 0  # even count includes initial prefix sum 0
        res = 0
        prefix = 0
        for num in arr:
            prefix = (prefix + num) % 2
            if prefix:
                res = (res + even) % mod
                odd += 1
            else:
                res = (res + odd) % mod
                even += 1
        return res
