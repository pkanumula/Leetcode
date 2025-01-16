class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        xor1, xor2 = 0, 0

        # XOR all elements in nums1
        for num in nums1:
            xor1 ^= num

        # XOR all elements in nums2
        for num in nums2:
            xor2 ^= num

        # If nums2 has an odd length, nums1's contribution to nums3 is xor1 repeated.
        # If nums1 has an odd length, nums2's contribution to nums3 is xor2 repeated.
        result = 0
        if len(nums2) % 2 == 1:
            result ^= xor1
        if len(nums1) % 2 == 1:
            result ^= xor2

        return result