from typing import List, Dict

class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        ball_colors: Dict[int, int] = {}
        color_count: Dict[int, int] = {}
        result = []

        for x, y in queries:
            if x in ball_colors:
                # Decrement the count of the old color
                old_color = ball_colors[x]
                color_count[old_color] -= 1
                if color_count[old_color] == 0:
                    del color_count[old_color]

            # Update ball color and increment the count of the new color
            ball_colors[x] = y
            if y not in color_count:
                color_count[y] = 0
            color_count[y] += 1

            # Append the number of distinct colors to the result
            result.append(len(color_count))

        return result
