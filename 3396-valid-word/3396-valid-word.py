class Solution:
    def isValid(self, word: str) -> bool:
        # 1) Length check
        if len(word) < 3:
            return False
        
        # 2) All characters must be alphanumeric (letters or digits)
        #    str.isalnum() returns True iff the string is non-empty
        #    and every character is either a letter or a digit. 
        if not word.isalnum():  
            return False  # contains symbols like '@', '#', '$', etc.
        
        # 3) Vowel definition
        vowels = set('aeiouAEIOU')
        
        # 4) Must have at least one vowel…
        has_vowel = any(ch in vowels for ch in word)
        # …and at least one consonant (alphabetic but not vowel)
        has_consonant = any(ch.isalpha() and ch not in vowels for ch in word)
        
        return has_vowel and has_consonant
