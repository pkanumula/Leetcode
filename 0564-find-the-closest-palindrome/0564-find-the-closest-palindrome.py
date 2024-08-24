class Solution(object):
    def nearestPalindromic(self, n):
        """
        :type n: str
        :rtype: str
        """
        length = len(n)
        prefix = int(n[:(length + 1) // 2])
        candidates = set()

        # Case 1: Palindromes by mirroring the first half
        for diff in (-1, 0, 1):
            new_prefix = str(prefix + diff)
            if length % 2 == 0:
                candidate = new_prefix + new_prefix[::-1]
            else:
                candidate = new_prefix + new_prefix[-2::-1]
            candidates.add(candidate)

        # Case 2: All 9's to 100...001 (e.g., "999" -> "1001")
        candidates.add('1' + '0' * (length - 1) + '1')

        # Case 3: All 0's except the last digit as 9 (e.g., "1000" -> "999")
        candidates.add('9' * (length - 1))

        # Remove the original number if it's in the set
        candidates.discard(n)

        # Filter out any empty strings or invalid entries
        candidates = {x for x in candidates if x and x.isdigit()}

        # Find the closest palindrome
        closest_palindrome = min(candidates, key=lambda x: (abs(int(x) - int(n)), int(x)))

        return closest_palindrome
