from typing import List

class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # sentinel for "bit b never appears again"
        INF = n
        
        # next_pos[b] = the smallest index >= i where nums[...] has bit b set
        next_pos = [INF] * 32  
        
        answer = [0] * n
        
        # scan from right to left
        for i in range(n - 1, -1, -1):
            # update next_pos for any bits set in nums[i]
            x = nums[i]
            while x:
                # isolate lowest set bit
                lowbit = x & -x
                b = lowbit.bit_length() - 1
                next_pos[b] = i
                x ^= lowbit
            
            # we need to cover every bit that will ever appear in the suffix
            farthest = i
            for pos in next_pos:
                if pos != INF:
                    farthest = max(farthest, pos)
            
            # minimal length from i is farthest − i + 1
            answer[i] = farthest - i + 1
        
        return answer
