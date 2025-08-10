class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        def sig(x: int):
            cnt = [0]*10
            while x:
                cnt[x % 10] += 1
                x //= 10
            return tuple(cnt)
        
        target = sig(n)
        # 2^0 to 2^30 covers up to 10 digits (2^30 = 1,073,741,824)
        return any(sig(1 << k) == target for k in range(31))
