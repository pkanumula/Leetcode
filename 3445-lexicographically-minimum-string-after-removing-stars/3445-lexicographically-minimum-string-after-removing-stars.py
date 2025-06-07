import heapq

class Solution:
  """
  Solves the Lexicographically Minimum String After Removing Stars problem.
  """
  def clearStars(self, s: str) -> str:
    """
    Removes stars from a string by deleting the leftmost star and the smallest
    non-star character to its left, aiming for the lexicographically smallest result.

    Args:
      s: The input string containing lowercase English letters and '*'.

    Returns:
      The lexicographically smallest string after all stars are removed.
    """
    n = len(s)
    # A min-heap to store tuples of (character, -index).
    # Using -index ensures that for the same smallest character, the one
    # with the largest index (rightmost) is prioritized.
    min_heap = []
    
    # A boolean array to mark characters for removal.
    removed = [False] * n
    
    for i, char in enumerate(s):
      if char == '*':
        # Mark the star itself for removal.
        removed[i] = True
        # If the heap is not empty, find and mark the character to remove.
        if min_heap:
          # Pop the smallest character; tie-breaking by the largest index.
          _, neg_index = heapq.heappop(min_heap)
          original_index = -neg_index
          removed[original_index] = True
      else:
        # For a letter, add it to the heap.
        heapq.heappush(min_heap, (char, -i))

    # Build the final result string from the characters that were not removed.
    result_builder = []
    for i in range(n):
      if not removed[i]:
        result_builder.append(s[i])
            
    return "".join(result_builder)