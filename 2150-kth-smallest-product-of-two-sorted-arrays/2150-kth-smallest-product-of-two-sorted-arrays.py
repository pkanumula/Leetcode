from bisect import bisect_left, bisect_right

class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        def countLessEqual(x: int) -> int:
            count = 0
            for a in nums1:
                if a == 0:
                    if x >= 0:
                        count += len(nums2)
                elif a > 0:
                    # a * b <= x => b <= x // a
                    count += bisect_right(nums2, x // a)
                else:  # a < 0
                    # a * b <= x => b >= ceil(x / a)
                    # Use exact math for ceil(x / a)
                    l = 0
                    r = len(nums2)
                    while l < r:
                        mid = (l + r) // 2
                        if a * nums2[mid] <= x:
                            r = mid
                        else:
                            l = mid + 1
                    count += len(nums2) - l
            return count

        left, right = -10**10, 10**10
        while left < right:
            mid = (left + right) // 2
            if countLessEqual(mid) < k:
                left = mid + 1
            else:
                right = mid
        return left
