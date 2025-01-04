class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        # Dictionary to store the first and last occurrences of each character
        first_occurrence = {}
        last_occurrence = {}
        
        # Determine the first and last occurrence of each character
        for i, char in enumerate(s):
            if char not in first_occurrence:
                first_occurrence[char] = i
            last_occurrence[char] = i
        
        # Set to store unique palindromic subsequences
        unique_palindromes = set()
        
        # Iterate over each unique character
        for char in first_occurrence:
            start = first_occurrence[char]
            end = last_occurrence[char]
            
            # If there is a valid range to form a palindrome
            if end - start > 1:
                # Collect all unique characters between the start and end indices
                middle_chars = set(s[start + 1:end])
                for mid_char in middle_chars:
                    # Form the palindrome and add it to the set
                    unique_palindromes.add((char, mid_char, char))
        
        # Return the count of unique palindromes
        return len(unique_palindromes)
