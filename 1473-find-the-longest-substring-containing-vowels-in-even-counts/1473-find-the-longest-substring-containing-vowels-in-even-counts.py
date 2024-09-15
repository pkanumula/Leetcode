class Solution:
    def findTheLongestSubstring(self, s):
        # Dictionary to store the first occurrence of a bitmask
        # We start with bitmask 0 at index -1
        pos = {0: -1}
        
        # Bitmask to track the parity (even or odd) of vowels
        mask = 0
        max_len = 0
        
        # Map vowels to their respective bit positions in the bitmask
        vowels = {'a': 1, 'e': 2, 'i': 4, 'o': 8, 'u': 16}
        
        # Iterate through the string
        for i, char in enumerate(s):
            # If the character is a vowel, flip the corresponding bit
            if char in vowels:
                mask ^= vowels[char]
            
            # If this mask has been seen before, calculate the length of the substring
            if mask in pos:
                max_len = max(max_len, i - pos[mask])
            else:
                # Otherwise, store the first occurrence of this mask
                pos[mask] = i
        
        return max_len
