class Solution:
    def reverseBits(self, n: int) -> int:
        n &= 0xFFFFFFFF  # keep only 32 bits (safe for signed/unsigned handling)
        ans = 0
        
        for _ in range(32):
            ans = (ans << 1) | (n & 1)  # append current last bit of n
            n >>= 1                     # move to next bit
        
        return ans
