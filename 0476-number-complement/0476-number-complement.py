class Solution(object):
    def findComplement(self, num):
        num_bits = num.bit_length()
        mask = (1 << num_bits) - 1
        return num ^ mask
