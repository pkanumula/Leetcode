from typing import List

class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        from collections import defaultdict
        
        value_map = defaultdict(int)
        
        # Accumulate values from nums1
        for id1, val1 in nums1:
            value_map[id1] += val1
        
        # Accumulate values from nums2
        for id2, val2 in nums2:
            value_map[id2] += val2
        
        # Create sorted result based on id
        return [[id, value] for id, value in sorted(value_map.items())]
