class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        """
        Returns the number of ways to distribute n candies among 3 children
        so that no child gets more than 'limit' candies.
        Uses inclusion–exclusion on the constraint xi <= limit.
        """

        def count_solutions(m: int) -> int:
            """
            Number of nonnegative integer solutions to a + b + c = m,
            which is C(m + 2, 2), provided m >= 0. Otherwise 0.
            """
            if m < 0:
                return 0
            # C(m + 2, 2) = (m + 2) * (m + 1) // 2
            return (m + 2) * (m + 1) // 2

        total = 0
        # Inclusion–exclusion over how many variables exceed 'limit'.
        # For k = 0..3, choose k variables to force xi > limit by writing
        # xi = yi + (limit + 1). Then sum(yi) + remaining = n - k*(limit+1).
        # Count of those is C((n - k*(limit+1)) + 2, 2) if nonnegative.
        # Multiply by C(3, k) and alternate signs.
        from math import comb

        for k in range(4):
            m = n - k * (limit + 1)
            ways = count_solutions(m)
            total += ((-1) ** k) * comb(3, k) * ways

        return total
