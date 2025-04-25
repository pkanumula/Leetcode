from collections import defaultdict

class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        count = 0
        prefix = 0
        freq = defaultdict(int)
        freq[0] = 1  # Initial prefix sum is 0
        
        for num in nums:
            # Check if current number satisfies the condition
            prefix = (prefix + (1 if num % modulo == k else 0)) % modulo
            # Looking for prefix that satisfies: (prefix - target) % modulo == 0 => prefix == target (mod modulo)
            target = (prefix - k) % modulo
            count += freq[target]
            freq[prefix] += 1
            
        return count
