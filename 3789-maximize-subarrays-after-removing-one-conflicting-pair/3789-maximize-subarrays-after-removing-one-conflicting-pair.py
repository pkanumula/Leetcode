import collections

class Solution:
    def maxSubarrays(self, n: int, conflictingPairs: list[list[int]]) -> int:
        """
        Calculates the maximum number of non-empty subarrays possible after removing 
        exactly one conflicting pair.
        """
        
        # Group conflicts by their right endpoint
        adj = collections.defaultdict(list)
        for u, v in conflictingPairs:
            l, r = min(u, v), max(u, v)
            adj[r].append(l)

        # For each right endpoint r, find the largest (m_vals) and second largest (m_prime_vals) left endpoint
        m_vals = [0] * (n + 1)
        m_prime_vals = [0] * (n + 1)
        for r in range(1, n + 1):
            if r in adj and adj[r]:
                ls = sorted(adj[r], reverse=True)
                m_vals[r] = ls[0]
                if len(ls) > 1:
                    m_prime_vals[r] = ls[1]

        # Calculate max_l[j] = max l over all conflicts with r <= j
        max_l = [0] * (n + 1)
        for j in range(1, n + 1):
            max_l[j] = max(max_l[j - 1], m_vals[j])

        # Calculate the base number of valid subarrays with all conflicts present
        base_valid_subarrays = 0
        for j in range(1, n + 1):
            base_valid_subarrays += j - max_l[j]

        # For each m_vals[i], find the next index j > i with m_vals[j] >= m_vals[i]
        # This helps limit the range of gain calculation.
        next_ge = [n + 1] * (n + 2)
        stack = []
        for i in range(n, 0, -1):
            while stack and m_vals[stack[-1]] < m_vals[i]:
                stack.pop()
            if stack:
                next_ge[i] = stack[-1]
            stack.append(i)
        
        max_gain = 0
        
        # Iterate through each possible primary conflict to remove
        for r in range(1, n + 1):
            if m_vals[r] == 0:
                continue

            l = m_vals[r]

            # Gain is 0 if removing the conflict doesn't lower the constraint at r
            if l <= max_l[r - 1]:
                continue

            j_end = next_ge[r]
            
            # The new constraint at r after removing the primary conflict
            C = max(max_l[r - 1], m_prime_vals[r])
            
            # Gain for subarrays ending at r
            gain = l - C
            
            # Calculate gain for subarrays ending at j > r, up to j_end
            sum_of_new_max_l = 0
            running_new_max_l = C
            for j in range(r + 1, j_end):
                running_new_max_l = max(running_new_max_l, m_vals[j])
                sum_of_new_max_l += running_new_max_l
                
            # The old constraint for j in [r+1, j_end-1] was l
            gain += (j_end - 1 - r) * l - sum_of_new_max_l
            
            max_gain = max(max_gain, gain)

        return base_valid_subarrays + max_gain