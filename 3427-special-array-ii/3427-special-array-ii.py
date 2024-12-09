class Solution:
    def isArraySpecial(self, nums, queries):
        # Precompute the parity of adjacent pairs
        n = len(nums)
        special = [0] * n
        for i in range(n - 1):
            # Record whether adjacent numbers have different parity
            special[i] = 1 if (nums[i] % 2 != nums[i + 1] % 2) else 0

        # Prefix sum for quick range sum calculation
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + special[i]

        # Process each query
        result = []
        for start, end in queries:
            # Check if all pairs in the range [start, end] are special
            if prefix_sum[end] - prefix_sum[start] == (end - start):
                result.append(True)
            else:
                result.append(False)

        return result
