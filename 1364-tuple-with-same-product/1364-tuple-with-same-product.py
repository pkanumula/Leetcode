from collections import defaultdict
from typing import List

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        product_count = defaultdict(int)
        n = len(nums)
        
        # Count pairs with the same product
        for i in range(n):
            for j in range(i + 1, n):
                product = nums[i] * nums[j]
                product_count[product] += 1

        # Calculate the number of valid tuples
        result = 0
        for count in product_count.values():
            if count > 1:
                # For each product appearing in `count` pairs, the number of valid tuples is:
                # 8 * C(count, 2) = 8 * (count * (count - 1) // 2)
                result += 8 * (count * (count - 1) // 2)

        return result
