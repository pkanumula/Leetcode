class Solution(object):
    def minimumDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Number of 'a's encountered so far
        a_count = s.count('a')
        # Minimum deletions initialized to the total number of 'a's
        # as worst case all 'a's need to be deleted
        min_deletions = a_count
        # Number of 'b's encountered so far
        b_count = 0

        for char in s:
            if char == 'a':
                # If the current character is 'a', decrease the count of 'a's remaining
                a_count -= 1
            else:
                # If the current character is 'b', increment the count of 'b's
                b_count += 1
            # The minimum deletions to make the string balanced is the minimum of:
            # 1. Keeping all the 'a's encountered so far and deleting all the remaining 'b's.
            # 2. Keeping all the 'b's encountered so far and deleting all the remaining 'a's.
            min_deletions = min(min_deletions, a_count + b_count)

        return min_deletions
