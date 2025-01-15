class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        # Count the number of set bits in num2
        set_bits = bin(num2).count('1')
        
        # Create a result variable
        result = 0
        
        # Fill bits of result to match num1's set bits where possible
        for i in range(31, -1, -1):
            if set_bits > 0 and (num1 & (1 << i)):
                result |= (1 << i)
                set_bits -= 1
        
        # Fill remaining set bits with the lowest unset bits in result
        for i in range(32):
            if set_bits > 0 and not (result & (1 << i)):
                result |= (1 << i)
                set_bits -= 1
        
        return result
