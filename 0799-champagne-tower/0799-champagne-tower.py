class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        # dp[c] = amount of champagne arriving at column c in the current row
        dp = [0.0] * (query_row + 2)  # +2 avoids index issues at c+1
        dp[0] = float(poured)

        # Process row by row until query_row
        for r in range(query_row):
            nxt = [0.0] * (query_row + 2)
            for c in range(r + 1):
                # Overflow from this glass (only if above 1 cup)
                overflow = (dp[c] - 1.0) / 2.0
                if overflow > 0:
                    nxt[c] += overflow
                    nxt[c + 1] += overflow
            dp = nxt

        # A glass can hold at most 1 cup
        return min(1.0, dp[query_glass])
