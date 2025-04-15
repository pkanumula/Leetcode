class FenwickTree:
    def __init__(self, size):
        self.tree = [0] * (size + 1)

    def update(self, index, delta):
        index += 1
        while index < len(self.tree):
            self.tree[index] += delta
            index += index & -index

    def query(self, index):
        # sum from 0 to index
        index += 1
        res = 0
        while index:
            res += self.tree[index]
            index -= index & -index
        return res

class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        pos2 = [0] * n
        for i, num in enumerate(nums2):
            pos2[num] = i

        mapped = [pos2[num] for num in nums1]

        left_tree = FenwickTree(n)
        right_tree = FenwickTree(n)
        count_right = [0] * n

        # Count how many numbers to the right are greater than current
        for i in range(n - 1, -1, -1):
            count_right[i] = right_tree.query(n - 1) - right_tree.query(mapped[i])
            right_tree.update(mapped[i], 1)

        ans = 0
        for i in range(n):
            left_count = left_tree.query(mapped[i] - 1)
            ans += left_count * count_right[i]
            left_tree.update(mapped[i], 1)

        return ans
