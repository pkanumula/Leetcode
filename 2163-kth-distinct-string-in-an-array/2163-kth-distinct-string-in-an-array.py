class Solution(object):
    def kthDistinct(self, arr, k):
        """
        :type arr: List[str]
        :type k: int
        :rtype: str
        """
        from collections import Counter
        
        # Count the frequency of each string in the array
        frequency = Counter(arr)
        
        # Iterate through the array and find the k-th distinct string
        distinct_count = 0
        for string in arr:
            if frequency[string] == 1:
                distinct_count += 1
                if distinct_count == k:
                    return string
        
        # If there are fewer than k distinct strings, return an empty string
        return ""
