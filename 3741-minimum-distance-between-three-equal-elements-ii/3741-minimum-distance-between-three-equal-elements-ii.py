class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        # Group indices by their values
        indices_map = {}
        for i, num in enumerate(nums):
            if num not in indices_map:
                indices_map[num] = []
            indices_map[num].append(i)

        min_distance = float('inf')

        # For each value, check all triplets
        for indices in indices_map.values():
            # Need at least 3 occurrences
            if len(indices) < 3:
                continue

            # Use sliding window of 3 consecutive indices
            # Key insight: optimal triplet uses consecutive indices in sorted list
            for i in range(len(indices) - 2):
                a = indices[i]
                b = indices[i + 1]
                c = indices[i + 2]
                # Distance = 2 * (max - min) when sorted
                distance = 2 * (c - a)
                min_distance = min(min_distance, distance)

        return min_distance if min_distance != float('inf') else -1