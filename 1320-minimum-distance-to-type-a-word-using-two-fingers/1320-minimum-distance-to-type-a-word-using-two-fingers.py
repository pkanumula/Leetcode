class Solution:
    def minimumDistance(self, word: str) -> int:

        def get_pos(c):
            i = ord(c) - ord('A')
            return (i // 6, i % 6)

        def distance(c1, c2):
            if c1 == -1:  # finger not placed yet, movement is free
                return 0
            x1, y1 = get_pos(c1)
            x2, y2 = get_pos(c2)
            return abs(x1 - x2) + abs(y1 - y2)

        n = len(word)
        memo = {}

        def dp(idx, finger1, finger2):
            if idx == n:
                return 0

            state = (idx, finger1, finger2)
            if state in memo:
                return memo[state]

            curr = word[idx]

            # Option 1: Move finger 1 to current character
            cost1 = distance(finger1, curr) + dp(idx + 1, curr, finger2)

            # Option 2: Move finger 2 to current character
            cost2 = distance(finger2, curr) + dp(idx + 1, finger1, curr)

            memo[state] = min(cost1, cost2)
            return memo[state]

        return dp(0, -1, -1)