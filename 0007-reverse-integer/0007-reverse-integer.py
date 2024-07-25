class Solution(object):
    def reverse(self, x):
        sign = -1 if x < 0 else 1
        x *= sign

        reversed_num = 0
        while x:
            reversed_num = reversed_num * 10 + x % 10
            x //= 10

        if reversed_num > 2**31 - 1:
            return 0

        return sign * reversed_num