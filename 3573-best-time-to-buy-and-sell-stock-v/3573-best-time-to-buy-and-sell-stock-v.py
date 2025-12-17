from typing import List

class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        NEG = -(10**30)

        # flat[t]  = max profit after processing current day, with t completed transactions, holding nothing
        # long[t]  = max profit after processing current day, with t completed transactions, holding a long (bought, not sold)
        # short[t] = max profit after processing current day, with t completed transactions, holding a short (sold, not bought back)
        flat = [NEG] * (k + 1)
        long = [NEG] * (k + 1)
        short = [NEG] * (k + 1)
        flat[0] = 0

        for p in prices:
            prev_flat = flat[:]
            prev_long = long[:]
            prev_short = short[:]

            # carry over (do nothing today)
            flat = prev_flat[:]
            long = prev_long[:]
            short = prev_short[:]

            for t in range(k + 1):
                # open a position today (doesn't complete a transaction)
                if prev_flat[t] != NEG:
                    long[t] = max(long[t], prev_flat[t] - p)   # buy to open long
                    short[t] = max(short[t], prev_flat[t] + p) # sell to open short

                # close a position today (completes 1 transaction)
                if t + 1 <= k:
                    if prev_long[t] != NEG:
                        flat[t + 1] = max(flat[t + 1], prev_long[t] + p)   # sell to close long
                    if prev_short[t] != NEG:
                        flat[t + 1] = max(flat[t + 1], prev_short[t] - p)  # buy to close short

        return max(flat)
