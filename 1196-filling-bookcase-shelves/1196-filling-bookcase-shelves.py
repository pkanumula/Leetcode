class Solution(object):
    def minHeightShelves(self, books, shelfWidth):
        """
        :type books: List[List[int]]
        :type shelfWidth: int
        :rtype: int
        """
        n = len(books)
        dp = [0] * (n + 1)  # dp[i] represents the minimum height for the first i books

        for i in range(1, n + 1):
            width = 0
            height = 0
            dp[i] = float('inf')

            # Place books[i-1] on the shelf and try to include previous books in the same shelf
            for j in range(i, 0, -1):
                width += books[j-1][0]
                if width > shelfWidth:
                    break
                height = max(height, books[j-1][1])
                dp[i] = min(dp[i], dp[j-1] + height)

        return dp[n]