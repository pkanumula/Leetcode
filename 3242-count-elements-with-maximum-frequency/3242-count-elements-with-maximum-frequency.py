class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = [0]*101                           # 1 <= nums[i] <= 100 [web:11]
        for x in nums:
            freq[x] += 1                         # count occurrences [web:15]
        mx = max(freq)                           # maximum frequency [web:15]
        return sum(f for f in freq if f == mx)   # sum of max-frequency counts [web:15]
