class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        # Find indices where characters differ
        diff_indices = [i for i in range(len(s1)) if s1[i] != s2[i]]

        # If no differences, strings are already equal
        if not diff_indices:
            return True

        # If there are exactly two differences, check if swapping can make strings equal
        if len(diff_indices) == 2:
            i, j = diff_indices
            return s1[i] == s2[j] and s1[j] == s2[i]

        # More than two differences make it impossible
        return False
