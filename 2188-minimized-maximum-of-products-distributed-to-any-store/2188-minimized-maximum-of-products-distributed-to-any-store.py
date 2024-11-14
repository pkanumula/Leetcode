from typing import List

class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        def can_distribute(max_products: int) -> bool:
            # Check if it's possible to distribute with max_products per store
            stores_needed = 0
            for quantity in quantities:
                stores_needed += -(-quantity // max_products)  # Ceiling division
                if stores_needed > n:
                    return False
            return True

        # Binary search for the minimum possible maximum
        left, right = 1, max(quantities)
        while left < right:
            mid = (left + right) // 2
            if can_distribute(mid):
                right = mid
            else:
                left = mid + 1

        return left