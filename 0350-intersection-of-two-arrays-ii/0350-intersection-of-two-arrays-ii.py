from collections import Counter

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # Create counters for both arrays
        counter1 = Counter(nums1)
        counter2 = Counter(nums2)
        
        # Find the intersection of the two counters
        intersection = counter1 & counter2
        
        # Convert the intersection to a list
        result = []
        for num in intersection:
            result.extend([num] * intersection[num])
        
        return result
        