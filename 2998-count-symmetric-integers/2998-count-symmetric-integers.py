class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        def is_symmetric(n: int) -> bool:
            s = str(n)
            if len(s) % 2 != 0:
                return False
            mid = len(s) // 2
            return sum(map(int, s[:mid])) == sum(map(int, s[mid:]))
        
        return sum(is_symmetric(i) for i in range(low, high + 1))
