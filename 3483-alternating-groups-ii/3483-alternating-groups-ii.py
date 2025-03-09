class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        n = len(colors)
        colors += colors[:k-1]
        count = 0
        alt = 0

        for i in range(len(colors)):
            if i > 0 and colors[i] != colors[i-1]:
                alt += 1
            else:
                alt = 1

            if alt >= k:
                count += 1

        return count