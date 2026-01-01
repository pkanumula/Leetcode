from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Start from the least significant digit
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0  # was 9, becomes 0 and carry continues

        # If we got here, all digits were 9 (e.g., 9, 99, 999)
        return [1] + digits
