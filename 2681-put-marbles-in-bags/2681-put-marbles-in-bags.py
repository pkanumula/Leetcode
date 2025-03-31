class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        n = len(weights)
        
        # Edge case when k == 1, the only possible split is one bag.
        if k == 1:
            return 0
        
        # Create a list of costs for adjacent weights
        diffs = [weights[i] + weights[i + 1] for i in range(n - 1)]
        
        # Sort the diffs to pick the (k-1) largest and (k-1) smallest differences
        diffs.sort()
        
        # Max score comes from the largest (k-1) differences
        max_score = sum(diffs[-(k - 1):])
        
        # Min score comes from the smallest (k-1) differences
        min_score = sum(diffs[:(k - 1)])
        
        return max_score - min_score
