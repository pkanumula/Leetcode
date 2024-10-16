import heapq

class Solution(object):
    def longestDiverseString(self, a, b, c):
        # Create a max heap based on the counts of 'a', 'b', 'c'
        max_heap = []
        if a > 0:
            heapq.heappush(max_heap, (-a, 'a'))
        if b > 0:
            heapq.heappush(max_heap, (-b, 'b'))
        if c > 0:
            heapq.heappush(max_heap, (-c, 'c'))

        result = []

        while max_heap:
            # Get the character with the highest remaining count
            count1, char1 = heapq.heappop(max_heap)
            # If last two characters in result are same as char1, use next character
            if len(result) >= 2 and result[-1] == result[-2] == char1:
                if not max_heap:
                    break
                count2, char2 = heapq.heappop(max_heap)
                result.append(char2)
                count2 += 1  # Decrease count for char2
                if count2 < 0:
                    heapq.heappush(max_heap, (count2, char2))
                # Push back char1 with its original count
                heapq.heappush(max_heap, (count1, char1))
            else:
                # Append char1 to the result
                result.append(char1)
                count1 += 1  # Decrease count for char1
                if count1 < 0:
                    heapq.heappush(max_heap, (count1, char1))

        return ''.join(result)
