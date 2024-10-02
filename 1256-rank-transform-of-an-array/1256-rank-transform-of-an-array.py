class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        # Create a sorted version of the array with unique elements
        sorted_arr = sorted(set(arr))
        
        # Create a dictionary to map each element to its rank
        rank_map = {num: i + 1 for i, num in enumerate(sorted_arr)}
        
        # Replace each element in the original array with its corresponding rank
        return [rank_map[num] for num in arr]
