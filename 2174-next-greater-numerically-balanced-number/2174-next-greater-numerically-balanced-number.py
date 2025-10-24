class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        # Generate all balanced numbers with total length <= 7 (covers n <= 1e6 comfortably).
        # Digits allowed are 1..7 (using 8 requires 8 digits already; still fine but unnecessary here).
        from bisect import bisect_right

        # Build once per call (still tiny: only a few thousand numbers).
        balanced = []

        # Step 1: choose which digits to include; if we include digit d, it appears exactly d times.
        def choose_digits(d: int, total_len: int, counts: dict):
            # Record a complete "digit multiset" and generate permutations as actual integers.
            if 1 <= total_len <= 7:
                generate_numbers_from_counts(counts)

            # Try adding next digits d..7 (subset generation with pruning by total length)
            for nd in range(d, 8):  # digits 1..7
                if total_len + nd <= 7:
                    counts[nd] = nd
                    choose_digits(nd + 1, total_len + nd, counts)
                    counts.pop(nd)

        # Step 2: from a digit->count map, generate all distinct permutations (no leading zero issues here).
        def generate_numbers_from_counts(counts: dict):
            digits = sorted(counts.keys())            # unique digits (1..7)
            left = {k: counts[k] for k in digits}     # remaining counts
            target_len = sum(left.values())
            curr = []

            def backtrack():
                if len(curr) == target_len:
                    # build integer (faster than join)
                    val = 0
                    for d in curr:
                        val = val * 10 + d
                    balanced.append(val)
                    return
                for d in digits:
                    if left[d] > 0:
                        left[d] -= 1
                        curr.append(d)
                        backtrack()
                        curr.pop()
                        left[d] += 1

            backtrack()

        choose_digits(1, 0, {})

        # unique + sorted
        balanced = sorted(set(balanced))

        # Step 3: pick the smallest number > n
        i = bisect_right(balanced, n)
        return balanced[i]
