from collections import Counter

class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        # If k is greater than the length of the string, it's impossible
        if k > len(s):
            return False

        # Count the frequency of each character in the string
        char_count = Counter(s)

        # Count the number of characters with odd frequencies
        odd_count = sum(freq % 2 for freq in char_count.values())

        # We can form at most 'len(s)' palindromes and at least 'odd_count' palindromes
        return odd_count <= k
