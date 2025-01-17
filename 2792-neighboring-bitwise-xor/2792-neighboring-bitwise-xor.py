class Solution:
    def doesValidArrayExist(self, derived: list[int]) -> bool:
        xor_sum = 0
        for num in derived:
            xor_sum ^= num
        return xor_sum == 0