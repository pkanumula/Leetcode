from collections import Counter
from typing import List

class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        # Step 1: Identify the dominant element
        count = Counter(nums)
        dominant = max(count, key=count.get)  # The element with the highest frequency
        total_count = count[dominant]  # Total occurrences of the dominant element
        
        # Step 2: Iterate through the array to find the minimum index for a valid split
        left_count = 0  # Count of dominant element in the left subarray
        for i in range(len(nums) - 1):  # Ensure i < n - 1
            if nums[i] == dominant:
                left_count += 1
            
            right_count = total_count - left_count  # Count of dominant in right subarray
            
            # Check if both sides have the dominant element as dominant
            if left_count * 2 > (i + 1) and right_count * 2 > (len(nums) - i - 1):
                return i
        
        return -1
