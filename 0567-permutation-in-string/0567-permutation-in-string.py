class Solution(object):
    def checkInclusion(self, s1, s2):
        from collections import Counter
        
        # Lengths of the strings
        len_s1, len_s2 = len(s1), len(s2)
        
        # If s1 is longer than s2, it's impossible for s2 to contain a permutation of s1
        if len_s1 > len_s2:
            return False
        
        # Frequency counter for s1 and the first window of s2
        s1_count = Counter(s1)
        s2_count = Counter(s2[:len_s1])
        
        # Sliding window over s2
        for i in range(len_s2 - len_s1):
            if s1_count == s2_count:
                return True
            
            # Move the window: remove the character going out and add the new character
            s2_count[s2[i]] -= 1
            if s2_count[s2[i]] == 0:
                del s2_count[s2[i]]
            s2_count[s2[i + len_s1]] += 1
        
        # Check the last window
        return s1_count == s2_count
