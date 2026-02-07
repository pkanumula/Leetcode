class Solution:
    def minimumDeletions(self, s: str) -> int:
        # deletions = minimum deletions needed for processed prefix
        deletions = 0
        # count of 'b' seen so far
        b_count = 0

        for ch in s:
            if ch == 'b':
                b_count += 1
            else:  # ch == 'a'
                # Option 1: delete this 'a' -> deletions + 1
                # Option 2: delete all previous 'b' -> b_count
                deletions = min(deletions + 1, b_count)

        return deletions
