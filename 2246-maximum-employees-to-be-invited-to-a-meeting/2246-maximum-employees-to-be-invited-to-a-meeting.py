from collections import defaultdict, deque

class Solution:
    def maximumInvitations(self, favorite: list[int]) -> int:
        n = len(favorite)
        indegree = [0] * n
        for f in favorite:
            indegree[f] += 1

        # Step 1: Process nodes with zero indegree (not part of any cycle)
        queue = deque(i for i in range(n) if indegree[i] == 0)
        longest_chain = [0] * n

        while queue:
            curr = queue.popleft()
            nxt = favorite[curr]
            longest_chain[nxt] = max(longest_chain[nxt], longest_chain[curr] + 1)
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                queue.append(nxt)

        # Step 2: Find cycles and calculate the result
        visited = [False] * n
        max_cycle = 0
        two_chain_sum = 0

        for i in range(n):
            if not visited[i]:
                cycle = []
                curr = i

                while not visited[curr]:
                    visited[curr] = True
                    cycle.append(curr)
                    curr = favorite[curr]

                if curr in cycle:  # Found a cycle
                    cycle_start = cycle.index(curr)
                    cycle_length = len(cycle) - cycle_start
                    if cycle_length == 2:  # Special case for 2-cycles
                        a, b = cycle[cycle_start], favorite[cycle[cycle_start]]
                        two_chain_sum += 2 + longest_chain[a] + longest_chain[b]
                    else:
                        max_cycle = max(max_cycle, cycle_length)

        return max(max_cycle, two_chain_sum)