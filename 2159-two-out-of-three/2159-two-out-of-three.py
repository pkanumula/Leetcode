class Solution(object):
    def twoOutOfThree(self, nums1, nums2, nums3):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :rtype: List[int]
        """
        from collections import Counter
        
        # Count the unique appearances of each number in the arrays
        count = Counter(set(nums1)) + Counter(set(nums2)) + Counter(set(nums3))
        
        # Return the numbers that appear in at least two of the three arrays
        return [num for num, freq in count.items() if freq > 1]
