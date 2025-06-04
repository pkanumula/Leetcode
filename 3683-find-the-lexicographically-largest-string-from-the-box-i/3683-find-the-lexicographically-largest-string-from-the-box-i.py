class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        """
        Given a string `word` of length n and an integer `numFriends` = m, we consider all ways
        to split `word` into `m` non-empty contiguous parts (rounds).  We collect every piece
        from every valid split into a box, and finally return the lexicographically largest
        string in that box.

        Observation:
        A substring S = word[i : j+1] can appear as one of the m parts in some partition if and
        only if there exists an index k (1 ≤ k ≤ m) such that:
            1) If k = 1, then i = 0 and the suffix length (n-1 - j) ≥ m - 1.
            2) If k = m, then j = n-1 and the prefix length i ≥ m - 1.
            3) If 1 < k < m, then:
                   i ≥ (k - 1)   (enough characters to form k−1 pieces before it),
               and (n - 1 - j) ≥ (m - k).  (enough chars to form m−k pieces after it).
        By analyzing these constraints, one finds that the maximum feasible length L for a substring
        starting at index i is:
          • If m = 1, the only valid piece is the entire word, so return `word` directly.
          • Otherwise, let n = len(word) and B = n - m + 1.
            – For 0 ≤ i ≤ m - 1, a substring of length B starting at i is feasible:
                L_i = B.
            – For i ≥ m, the largest feasible piece is the suffix of length (n - i):
                L_i = n - i.
        Hence, we only need to look at substrings that begin at positions i where word[i] equals
        the global maximum character.  For each such i:
            • If i ≤ m - 1: take `word[i : i + B]`.
            • If i ≥ m: take `word[i : n]`.
        Finally, pick the lexicographically largest among these candidates.

        Time Complexity: O(n^2) in the worst case (all characters are equal), which is acceptable
        for n ≤ 5000.
        """
        n = len(word)
        m = numFriends

        # Special case: only one friend → the only valid split is the entire word
        if m == 1:
            return word

        # Precompute the cutoff length B = n - m + 1
        B = n - m + 1

        # Find the maximum character in the string
        max_char = max(word)

        best = ""  # will hold the lexicographically largest feasible piece

        # Iterate over all positions where word[i] == max_char
        for i, ch in enumerate(word):
            if ch != max_char:
                continue

            # Determine the maximum feasible length L_i for a piece starting at i
            if i <= m - 1:
                L_i = B
            else:
                L_i = n - i

            # Extract that substring
            candidate = word[i : i + L_i]

            # Compare and keep the lexicographically largest
            if candidate > best:
                best = candidate

        return best
