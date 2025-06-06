import collections

class Solution:
  def robotWithString(self, s: str) -> str:
    """
    Finds the lexicographically smallest string that can be written on paper.

    This solution uses a greedy approach. At each step, it decides whether to
    move a character from the input string `s` to a temporary stack `t`, or
    from `t` to the result string `p`.

    To make the optimal greedy choice, we precompute the minimum character for
    every suffix of `s`. This allows us to compare the character at the top of
    the stack with the smallest character we might encounter in the future from `s`.

    The logic is as follows:
    1. A character `t.top()` is moved to `p` only if it's less than or equal
       to the minimum of all remaining characters in `s`.
    2. Otherwise, we must move a character from `s` to `t` to get closer to
       the future smallest character.

    This ensures that we always append the smallest possible character to the result
    at any given time.
    """
    
    # suffix_min[i] will store the minimum character in s[i:]
    suffix_min = [''] * (len(s) + 1)
    # Use a sentinel value larger than any lowercase letter
    suffix_min[len(s)] = '~' 
    
    # Precompute the suffix minimums in O(n)
    for i in range(len(s) - 1, -1, -1):
      suffix_min[i] = min(s[i], suffix_min[i+1])
      
    # `t` acts as the robot's temporary string (stack)
    t = [] 
    # `p` will build the final result string
    p = []
    
    # Iterate through the input string s
    for i in range(len(s)):
      # Operation 1: Move the character from s to t
      t.append(s[i])
      
      # Operation 2: Greedily move characters from t to p
      # We pop from t if its top character is less than or equal to the
      # minimum character in the rest of s (s[i+1:])
      while t and t[-1] <= suffix_min[i+1]:
        p.append(t.pop())
        
    # Append any remaining characters from the stack t
    while t:
      p.append(t.pop())
      
    return "".join(p)