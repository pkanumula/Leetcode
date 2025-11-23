from typing import List

class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        total = sum(nums)

        # Store the two smallest numbers with remainder 1 and 2
        # Initialize with large values
        rem1 = [10**15, 10**15]  # smallest, second smallest with num % 3 == 1
        rem2 = [10**15, 10**15]  # smallest, second smallest with num % 3 == 2

        for x in nums:
            r = x % 3
            if r == 1:
                if x < rem1[0]:
                    rem1[1] = rem1[0]
                    rem1[0] = x
                elif x < rem1[1]:
                    rem1[1] = x
            elif r == 2:
                if x < rem2[0]:
                    rem2[1] = rem2[0]
                    rem2[0] = x
                elif x < rem2[1]:
                    rem2[1] = x

        if total % 3 == 0:
            return total

        ans = 0
        if total % 3 == 1:
            # Option 1: remove one rem1
            option1 = total - rem1[0] if rem1[0] < 10**15 else 0
            # Option 2: remove two rem2
            if rem2[1] < 10**15:
                option2 = total - (rem2[0] + rem2[1])
            else:
                option2 = 0
            ans = max(option1, option2)
        else:  # total % 3 == 2
            # Option 1: remove one rem2
            option1 = total - rem2[0] if rem2[0] < 10**15 else 0
            # Option 2: remove two rem1
            if rem1[1] < 10**15:
                option2 = total - (rem1[0] + rem1[1])
            else:
                option2 = 0
            ans = max(option1, option2)

        return ans
