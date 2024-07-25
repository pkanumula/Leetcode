class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def merge_sort(start, end):
            if end - start <= 1:
                return
            
            mid = (start + end) // 2
            merge_sort(start, mid)
            merge_sort(mid, end)
            merge(start, mid, end)
        
        def merge(start, mid, end):
            left = nums[start:mid]
            right = nums[mid:end]
            i = j = 0
            k = start
            
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    nums[k] = left[i]
                    i += 1
                else:
                    nums[k] = right[j]
                    j += 1
                k += 1
            
            while i < len(left):
                nums[k] = left[i]
                i += 1
                k += 1
            
            while j < len(right):
                nums[k] = right[j]
                j += 1
                k += 1
        
        merge_sort(0, len(nums))
        return nums