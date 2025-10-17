import collections

class Solution:
  def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
    n = len(s)
    memo = {}

    def solve(index: int, mask: int, change_used: bool) -> int:
      """
      Calculates the maximum number of partitions for the suffix s[index:].
      
      Args:
        index: The starting index of the suffix.
        mask: A bitmask of distinct characters in the current partition.
        change_used: A boolean indicating if the one-time change has been used.
        
      Returns:
        The maximum number of partitions.
      """
      if index == n:
        return 1
      
      state = (index, mask, change_used)
      if state in memo:
        return memo[state]

      # --- Option 1: Don't change s[index] ---
      char_bit = 1 << (ord(s[index]) - ord('a'))
      new_mask_no_change = mask | char_bit
      
      res = 0
      if new_mask_no_change.bit_count() > k:
        # Start a new partition with s[index]
        res = 1 + solve(index + 1, char_bit, change_used)
      else:
        # Continue the current partition
        res = solve(index + 1, new_mask_no_change, change_used)

      # --- Option 2: Change s[index] (if allowed) ---
      if not change_used:
        # Iterate through all 26 possible lowercase letters to change to.
        for i in range(26):
          new_char_bit = 1 << i
          new_mask_with_change = mask | new_char_bit
          
          if new_mask_with_change.bit_count() > k:
            # The change forces a new partition.
            res = max(res, 1 + solve(index + 1, new_char_bit, True))
          else:
            # The change allows continuing the current partition.
            res = max(res, solve(index + 1, new_mask_with_change, True))
      
      memo[state] = res
      return res

    # Initial call: start at index 0, with an empty mask, and the change is available.
    return solve(0, 0, False)