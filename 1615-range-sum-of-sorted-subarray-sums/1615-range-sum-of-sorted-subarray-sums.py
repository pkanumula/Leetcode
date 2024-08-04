class Solution(object):
    def rangeSum(self, nums, n, left, right):
        """
        :type nums: List[int]
        :type n: int
        :type left: int
        :type right: int
        :rtype: int
        """
        MOD = 10**9 + 7

        # Compute all subarray sums
        subarray_sums = []
        for i in range(n):
            current_sum = 0
            for j in range(i, n):
                current_sum += nums[j]
                subarray_sums.append(current_sum)

        # Sort the subarray sums
        subarray_sums.sort()

        # Calculate the sum of the numbers from index left to right (1-based index)
        result = sum(subarray_sums[left-1:right]) % MOD

        return result
