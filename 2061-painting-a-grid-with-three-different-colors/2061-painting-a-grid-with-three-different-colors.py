class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        from collections import defaultdict
        MOD = 10**9 + 7

        def generate_valid_columns(m):
            def dfs(pos, path):
                if pos == m:
                    valid_columns.append(tuple(path))
                    return
                for color in range(3):
                    if pos == 0 or color != path[-1]:
                        path.append(color)
                        dfs(pos + 1, path)
                        path.pop()
            valid_columns = []
            dfs(0, [])
            return valid_columns

        def is_compatible(col1, col2):
            return all(a != b for a, b in zip(col1, col2))

        valid_columns = generate_valid_columns(m)
        transitions = defaultdict(list)
        for i, col1 in enumerate(valid_columns):
            for j, col2 in enumerate(valid_columns):
                if is_compatible(col1, col2):
                    transitions[i].append(j)

        dp = [1] * len(valid_columns)
        for _ in range(n - 1):
            new_dp = [0] * len(valid_columns)
            for i, count in enumerate(dp):
                for j in transitions[i]:
                    new_dp[j] = (new_dp[j] + count) % MOD
            dp = new_dp

        return sum(dp) % MOD
