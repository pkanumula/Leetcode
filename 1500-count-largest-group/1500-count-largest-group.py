class Solution:
    def countLargestGroup(self, n: int) -> int:
        from collections import defaultdict

        group_counts = defaultdict(int)

        for i in range(1, n + 1):
            digit_sum = sum(int(d) for d in str(i))
            group_counts[digit_sum] += 1

        max_size = max(group_counts.values())
        return sum(1 for count in group_counts.values() if count == max_size)
